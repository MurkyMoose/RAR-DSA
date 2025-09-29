
from definitions.coding_manuals import system_manual, system_prompt_topic
from definitions.instructions import inference_instructions_topic
from src.utils import consolidate_reasoning_chain
from src.dependencies import client
import asyncio
from definitions.models import AttributionResponse, ReviewResponse, reduce_model_to_field
import json
import os
from src.with_retrieval import get_closest_3


topics = list(system_manual.keys())

# ---- Async logic to run per topic ----
async def run_topic_reflect_inference(
    topic: str,
    initial_response: list[dict],
    entry: dict,
    base_messages_instance: dict,
    model_name: str,
    temp: float,
    add_references: bool,
    runs: int = 3
) -> dict:
    """
    Run reflection-based inference for a single topic, with optional reference retrieval and multiple rounds of review/revision.
    Returns the final parsed JSON response as a dictionary.
    """
    base_messages = [
        {
            "role": "system",
            "content": system_prompt_topic(topic)
        },
        {
            "role": "user",
            "content": f"Test Case Interview Transcript:\n{entry['transcript']}"
        },
        {
            "role": "user",
            "content": "INSTRUCTIONS: " + inference_instructions_topic(topic)
        }
    ]

    base_messages.append({
        "role": "assistant",
        "content": f"Attribution Analysis (round 1):\n{consolidate_reasoning_chain(initial_response)[topic]}"
    })

    counter = 1

    if add_references:
        base_messages.append({
            "role": "user",
            "content": get_closest_3(id, topic, top_n=3)
        })


    # Step 2+: Reflection cycles
    for reflect_round in range(1, runs ):
        base_messages.append({
            "role": "user",
            "content": f"""
Review Attribution Analysis (round {counter}) per the PASS manual.
- Flag attribution misclassifications
- Suggest additions/removals
- Ensure inclusion/exclusion criteria are met
"""
        })

        def review_response():
            return client.chat.completions.parse(
                model=model_name,
                messages=base_messages,
                response_format=ReviewResponse,
                temperature=temp,
                top_p=1,
                presence_penalty=0,
                frequency_penalty=0,
                seed=42,
            )

        review = await asyncio.to_thread(review_response)


        base_messages.append({
            "role": "assistant",
            "content": f"Review of Attribution Analysis (round {counter}):\n{review.choices[0].message.content}"
        })

        if json.loads(review.choices[0].message.content)['reviews'] is None:
            base_messages.append({
            "role": "assistant",
            "content": f"Review of Attribution Analysis (round {counter}):\n"+ "{\"reviews\":[]}"
        })
            break
        elif len(json.loads(review.choices[0].message.content)['reviews'])==0:
            base_messages.append({
                "role": "assistant",
                "content": f"Review of Attribution Analysis (round {counter}):\n{review.choices[0].message.content}"
            })
            break

        base_messages.append({
            "role": "user",
            "content": f"""
Revise Attribution Analysis (round {counter}) using feedback in the review.
- If feedback is valid, update attributions.
- If not valid, explain why in 'reasoning'.
"""
        })

        def revise_response():
            return client.chat.completions.parse(
                model=model_name,
                messages=base_messages,
                response_format=reduce_model_to_field(AttributionResponse, topic),
                temperature=temp,
                top_p=1,
                presence_penalty=0,
                frequency_penalty=0,
                seed=42,
            )

        completion = await asyncio.to_thread(revise_response)
        base_messages.append({
            "role": "assistant",
            "content": f"Attribution Analysis (round {counter + 1}):\n{completion.choices[0].message.content}"
        })

        counter += 1
        await asyncio.sleep(1)

    base_messages_instance[topic] = base_messages

    try:
        return json.loads(completion.choices[0].message.content)
    except:
        return {topic: consolidate_reasoning_chain(initial_response)[topic]}

# ---- Async loop over entries and runs ----
async def process_entry_with_reflect(
    entry: dict,
    run_id: str,
    model_name: str,
    temp: float,
    add_references: bool
) -> None:
    """
    Run reflection-based inference for all topics for a given entry and save results to file.
    """
    file_name = f"{entry['subject_code']}.json"
    file_folder = f"ai_json_output/{run_id}"
    os.makedirs(file_folder, exist_ok=True)
    file_path = os.path.join(file_folder, file_name)
    file_path_reflection = os.path.join(file_folder, f"reflection/reflection_{file_name}")

    with open(f"{file_folder}/{file_name}", "r", encoding="utf-8") as f:
        initial_response = json.load(f)

    class BaseMessages:
        def __init__(self, topic, messages):
            self.topic = topic
            self.messages = messages

    if os.path.exists(file_path):
        print(f"Skipping {file_name}, already exists.")
        return

    compiled = []
    base_messages_instance = {} 
    tasks = [run_topic_reflect_inference(topic, initial_response, entry, base_messages_instance, model_name, temp, add_references) for topic in topics]
    results = await asyncio.gather(*tasks)
    this_run = {}
    [this_run.update(result) for result in results]
    #print(f"Run {run_index + 1} for {entry['subject_code']} completed.")
    compiled.append(this_run)
    await asyncio.sleep(1)

    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(compiled, f, indent=2, ensure_ascii=False)
    with open(file_path_reflection, "w", encoding="utf-8") as f:
        json.dump(base_messages_instance, f, indent=2, ensure_ascii=False)
        await asyncio.sleep(10)

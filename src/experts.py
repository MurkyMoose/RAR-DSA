
from definitions.coding_manuals import system_manual, system_prompt_topic
from definitions.instructions import inference_instructions_topic
from src.utils import consolidate_reasoning_chain
from src.dependencies import client
import asyncio
from definitions.models import AttributionResponse, ReviewResponse, reduce_model_to_field
import json
import os
from typing import Dict, Any, Type, List

topics = list(system_manual.keys())

# ---- Async logic to run per topic ----
async def run_topic_inference(
    topic: str,
    entry: Dict[str, Any],
    model_name: str,
    temp: float | None
) -> Dict[str, Any]:
    """
    Run inference for a single topic and entry using the specified model and temperature.
    Returns the parsed JSON response as a dictionary.
    """
    messages = [
        {
            "role": "system",
            "content": system_prompt_topic(topic),
        },
        {"role": "user", "content": f"Test Case Interview Transcript: \n{entry['transcript']}"},
        {"role": "user", "content": "INSTRUCTIONS: " + inference_instructions_topic(topic)},
    ]
    if temp is None:
        def blocking_completion() -> Any:
            return client.chat.completions.parse(
                model=model_name,
                messages=messages,
                response_format=reduce_model_to_field(AttributionResponse, topic),
                top_p=1,
                presence_penalty=0,
                frequency_penalty=0,
                seed=42,
            )
    else:
        def blocking_completion() -> Any:
            return client.chat.completions.parse(
                model=model_name,
                messages=messages,
                response_format=reduce_model_to_field(AttributionResponse, topic),
                temperature=temp,
                top_p=1,
                presence_penalty=0,
                frequency_penalty=0,
                seed=42,
            )

    completion = await asyncio.to_thread(blocking_completion)
    return json.loads(completion.choices[0].message.content)

# ---- Async loop over entries and runs ----
async def process_entry(
    entry: Dict[str, Any],
    run_id: str,
    model_name: str,
    temp: float | None,
    file_path: str,
    runs: int = 3
) -> None:
    """
    Run inference for all topics for a given entry, multiple times, and save results to file.
    """
    compiled: list[dict[str, Any]] = []
    file_name = f"{entry['subject_code']}.json"
    file_folder = f"ai_json_output/{run_id}"
    os.makedirs(file_folder, exist_ok=True)
    file_path = os.path.join(file_folder, file_name)

    for run_index in range(runs):
        tasks = [run_topic_inference(topic, entry, model_name, temp) for topic in topics]
        results = await asyncio.gather(*tasks)
        this_run: dict[str, Any] = {}
        [this_run.update(result) for result in results]
        compiled.append(this_run)
        await asyncio.sleep(1)

    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(compiled, f, indent=2, ensure_ascii=False)
        await asyncio.sleep(10)

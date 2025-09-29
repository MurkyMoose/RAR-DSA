import chromadb
import json
from src.dependencies import client
import asyncio

def create_collection_codings(human_coding_with_transcript: list[dict]) -> object:
    """
    Create a ChromaDB collection from human coding data with embeddings and metadata.
    Args:
        human_coding_with_transcript: List of dictionaries with transcript and coding info.
    Returns:
        ChromaDB collection object.
    """
    chroma_client =  chromadb.PersistentClient(path="chromadb")

    try:
        chroma_client.delete_collection(name="human-coding-db")
    except:
        pass
    # Create collection. get_collection, get_or_create_collection, delete_collection also available!
    collection = chroma_client.create_collection("human-coding-db")

    for anEntry in human_coding_with_transcript:
        collection.add(
            embeddings=[anEntry['embeddings']],
            metadatas=[{
    "LOCUS_OF_CONTROL": str({
        "Locus_External": [{"quoted_statement": a_statement} for a_statement in anEntry['Human_LOC_E']] ,
        "Locus_Internal_Bad_Unlikeable": [{"quoted_statement": a_statement} for a_statement in anEntry['Human_LOC_IBU']],
        "Locus_Internal_Good_Likeable": [{"quoted_statement": a_statement} for a_statement in anEntry['Human_LOC_IGL']]
    }),
    "PERMANENCE": str({
        "Stable_Unchangeable": [{"quoted_statement": a_statement} for a_statement in anEntry['Human_Perm_SU']],
        "Fluctuate_Changeable": [{"quoted_statement": a_statement} for a_statement in anEntry['Human_Perm_FC']]
    }),
    "INTENTIONALITY": str({
        "Deliberate": [{"quoted_statement": a_statement} for a_statement in anEntry['Human_Int_D']],
        "Unintentional": [{"quoted_statement": a_statement} for a_statement in anEntry['Human_Int_U']]
    }),
    "CONTROLLABILITY": str({
        "Controllable_Regulated": [{"quoted_statement": a_statement} for a_statement in anEntry['Human_Con_CR']],
        "Uncontrollable_Unregulated": [{"quoted_statement": a_statement} for a_statement in anEntry['Human_Con_UU']]
    })
    }],
        documents = [anEntry['transcript']],
            ids=[anEntry["subject_code"]]
        )

    collection = chroma_client.get_collection(
        name="human-coding-db",
        embedding_function=None
    )
    return collection

# create embeddings and save to file
with open("data/human_coding/human_coding_with_transcript.json", "r", encoding="utf-8") as f:
    data = json.load(f)
for one_entry in data:
    emb = client.embeddings.create(
    model="text-embedding-ada-002",
    input=one_entry['transcript'],
    encoding_format="float"
    )
    one_entry['embeddings'] = emb.data[0].embedding
with open("data/human_coding/human_coding_with_transcript_with_embeddings.json", "w", encoding="utf-8") as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

# read embeddings from file and create chromadb collection
with open("data/human_coding/human_coding_with_transcript_with_embeddings.json", "r", encoding="utf-8") as f:
    human_coding_with_transcript = json.load(f)

reference_collection = create_collection_codings(human_coding_with_transcript)

def get_closest_3(id: str, topic: str, top_n: int = 3) -> str:
    """
    Retrieve the top_n most similar transcripts by embedding for a given id and topic.
    Args:
        id: Subject code to match.
        topic: Coding topic to retrieve examples for.
        top_n: Number of examples to return (default: 3).
    Returns:
        String containing formatted reference examples for prompting.
    """
    current_embedding = [a for a in human_coding_with_transcript if a['subject_code'] == id][0]['embeddings']

    results = reference_collection.query(
        query_embeddings=[current_embedding],
        n_results=4
    )

    sample_string = "Refer to these examples for coding for " + topic + " and derive how it aligns with the PASS Manual, the linguistic coding thresholds. Use these insights to enhance the Attribution Analysis for the Test Case Interview Transcript. Note that while some examples may not include codings for their transcripts, the Test Case Interview Transcript may still yields valid codings. Do not take presence of codings as a requirement for the Test Case Interview Transcript to yield valid codings."
    #print(results['ids'][0][1:])
    for i in range(top_n):
        sample_string += f"\n<example id='Example {i+1}'> \nInterview Transcript:\n{results['documents'][0][1:][i]}\n"
        sample_string += f"Quoted Statement: \n{results['metadatas'][0][1:][i][topic]}\n</example id='Example {i+1}'>"

    return sample_string


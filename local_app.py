import time
import numpy as np
import streamlit as st
from connection_local import MilvusConnection

fmt = "\n=== {:30} ===\n"
search_latency_fmt = "search latency = {:.4f}s"
num_entities, dim = 1, 8

st.header('Hello Milvus!')

conn = st.experimental_connection("milvus", type=MilvusConnection)

st.write("""This Streamlit application is for demonstration purposes. 
         It was created as a contribution to the Streamlit Connection Hackathon August 2023. 
         A Streamlit experimental connector has been adapted with pymilvus, 
         the Milvus Python SDK, and connects the Streamlit user interface to the Milvus vector database.""")

st.write("The following collections are inside the Milvus database:")
collections_list = conn.list_collections()
for i, collection in enumerate(collections_list):
    st.code(f"{i} {collection} contains {conn.count_entities(collection)} entities")

hello_milvus = conn.get_collection("hello_milvus")
schema = hello_milvus.schema
schema = medium_articles.schema
fields = schema.fields

# create random entity as example vector to query the database
rng = np.random.default_rng(seed=19530)
entities = [
    # provide the pk field because `auto_id` is set to False
    [str(i) for i in range(num_entities)],
    rng.random(num_entities).tolist(),  # field random, only supports list
    rng.random((num_entities, dim)),    # field embeddings, supports numpy.ndarray and list
]

vectors_to_search = entities[-1][-2:]

search_params = {
    "metric_type": "L2",
    "params": {"nprobe": 10},
}

start_time = time.time()
result = hello_milvus.search(vectors_to_search, "embeddings", search_params, limit=5, output_fields=["random"])
end_time = time.time()

if st.button("Perform L2 distance vector search"):
    st.code(f"search vector: {vectors_to_search[0]}")

    for hits in result:
        for i, hit in enumerate(hits):
            st.write(hit)
    
    st.code(search_latency_fmt.format(end_time - start_time))

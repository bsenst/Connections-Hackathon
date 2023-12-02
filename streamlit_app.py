import time
import numpy as np
import streamlit as st
from connection import MilvusConnection

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
    # st.code(f"{i} {collection} contains {conn.count_entities(collection)} entities")
    st.code(f"{i} {collection}")

medium_articles = conn.get_collection("medium_articles")

id = st.slider('Choose a Medium Article', 0, 5978, 5978)

res = medium_articles.query(
  expr = f"id == {id}", 
  output_fields = ["id", "title_vector", "publication", "link"]
)

st.write(f'{id} {res[0]["link"]}')

vectors_to_search = [res[0]["title_vector"]]

search_params = {
    "metric_type": "L2",
    "params": {"nprobe": 10},
}

start_time = time.time()
result = medium_articles.search(vectors_to_search, "title_vector", search_params, limit=6, output_fields=["publication", "link"])
end_time = time.time()

if st.button("Perform L2 distance vector search"):

    type(result)

    # for hits in result:
    #     skip = [0]
    #     for i, hit in enumerate(hits):
    #         if i not in skip:
    #             st.write(hit)
    
    st.code(search_latency_fmt.format(end_time - start_time))

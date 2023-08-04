import streamlit as st
from streamlit.connections import ExperimentalBaseConnection
from streamlit.runtime.caching import cache_data

from pymilvus import (
    connections,
    utility,
    Collection
)

milvus_uri = st.secrets.db_credentials["uri"]
token = st.secrets.db_credentials["token"]

class MilvusConnection(ExperimentalBaseConnection[connections]):
    def _connect(self, **kwargs):
        return connections.connect("default", uri=milvus_uri, token=token) # streamlit cloud deployment
    
    def has_collection(self, collection_name):
        return utility.has_collection(collection_name)
    
    def list_collections(self):
        return utility.list_collections()

    def count_entities(self, collection_name):
        return Collection(collection_name).num_entities
    
    def get_collection(self, collection_name):
        return Collection(collection_name)

import streamlit as st
from connection import Connection

st.write('Hello world!')

conn = st.experimental_connection("spaceflightnewsapi", type="Connection", max_entries=None, ttl=None, **kwargs)

st.write(conn)
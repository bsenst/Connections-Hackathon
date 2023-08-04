from streamlit.connections import ExperimentalBaseConnection
from streamlit.runtime.caching import cache_data

class Connection(ExperimentalBaseConnection[duckdb.DuckDBPyConnection]):
    
    def _connect(self, **kwargs):
        return "_connect"
    
    def query(self, query: str, ttl: int = 3600, **kwargs):
        @cache_data(ttl=ttl)
        def _query(query: str, **kwargs):
            return query
        
        return _query(query, **kwargs)
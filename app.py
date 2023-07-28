import streamlit as st
from llama_index import StorageContext, load_index_from_storage
"""
# TaxChat
### @ Streamlit GitHub Lapyl
- [GitHub Repository](https://github.com/Lapyl/Kaleido)
- [Streamlit Dcumentation](https://docs.streamlit.io)
- [Streamlit Forums](https://discuss.streamlit.io)
"""

with st.echo(code_location='below'):
    def chatbot(zask="Where is Florida?"):
        storage_context = StorageContext.from_defaults(persist_dir='Meta_Index/FloridaSutLaws')
        index = load_index_from_storage(storage_context)
        query_engine = index.as_query_engine()
        response = query_engine.query(zask)
        return response
    chatbot()

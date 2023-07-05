from llama_index import StorageContext, load_index_from_storage
import gradio as gr

def chatbot(zask="Where is Florida?"):
    storage_context = StorageContext.from_defaults(persist_dir='Meta_Index\FloridaSutLaws')
    index = load_index_from_storage(storage_context)
    query_engine = index.as_query_engine()
    response = query_engine.query(zask)
    return response

iface = gr.Interface(fn=chatbot,
                     inputs=gr.components.Textbox(lines=7, label="Input Text"),
                     outputs=gr.components.Textbox(lines=7, label="Output Text"),
                     title="Chatbot regarding Florida Sales & Use Tax Statutes and Codes")

iface.launch(share=True)


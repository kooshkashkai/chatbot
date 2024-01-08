import streamlit as st
from llama_index import VectorStoreIndex, ServiceContext, Document
from llama_index.llms import OpenAI
import openai
from llama_index import SimpleDirectoryReader
#from llama_index.readers import download_loader
import os
import requests
from bs4 import BeautifulSoup
import url_data


openai.api_key = st.secrets.openai_key


# Code used for generating sub Url's:
# # Get sub url's from website:
# url = 'https://solumxplain.github.io/docs.xplainfinancial/'
# reqs = requests.get(url)
# soup = BeautifulSoup(reqs.text, 'html.parser')
 
# urls = []
# for link in soup.find_all('a'):
#     urls.append(link.get('href'))
# urls = ['https://solumxplain.github.io/docs.xplainfinancial' + s for s in urls if s[0:1] != "#"]

#urls=['https://solumxplain.github.io/docs.xplainfinancial/']

st.header("Xplain docs interactive chatbot 💬 🧐 🐶")

if "messages" not in st.session_state.keys():
    st.session_state.messages = [
        {"role": "assistant", "content": "Ask me a question about Xplain!"}
    ]

@st.cache_resource(show_spinner=False)

def load_data():
    with st.spinner(text="Loading and indexing the Xplain docs..."):
        #SimpleWebPageReader = download_loader("SimpleWebPageReader", custom_path=".cache/llamahub_modules")
        #loader = SimpleWebPageReader()
        #docs = loader.load_data(urls=url_data.url_data)
        reader = SimpleDirectoryReader(input_dir="./data", recursive=True)
        docs = reader.load_data()
        service_context = ServiceContext.from_defaults(llm=OpenAI(model="gpt-3.5-turbo", temperature=0.5, system_prompt="You are an expert on the Xplain docs and your job is to answer technical questions. Assume that all questions are related to the Xplain docs. Give full details in your answers rather than referring to the Xplain docs. Keep your answers technical and based on facts – do not hallucinate features."))
        index = VectorStoreIndex.from_documents(docs, service_context=service_context)
        return index


index = load_data()

if "chat_engine" not in st.session_state.keys():
        st.session_state.chat_engine = index.as_chat_engine(chat_mode="condense_question", verbose=True)

if prompt := st.chat_input("Your question"): 
    st.session_state.messages.append({"role": "user", "content": prompt})

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

if st.session_state.messages[-1]["role"] != "assistant":
    with st.chat_message("assistant"):
        with st.spinner("Let me think about that..."):
            response = st.session_state.chat_engine.chat(prompt)
            st.write(response.response)
            message = {"role": "assistant", "content": response.response}
            st.session_state.messages.append(message)


import os
from dotenv import load_dotenv
load_dotenv()
import streamlit as st

from langchain_groq import ChatGroq
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.embeddings import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain.chains import create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
os.environ['Groq_api_key']=os.getenv('groq_api_key')
llm=ChatGroq(model='mixtral-8x7b-32768')

prompt=ChatPromptTemplate.from_template(
    '''
    You are context aware assistant so give response of question from contenxt
    <context>
    {context}
    </context>
    Question:{input}
    '''
)

def generate_embedding():
    if 'vectors' not in st.session_state:
        st.session_state.embeddings=OpenAIEmbeddings()
        st.session_state.loader=PyPDFLoader('attention.pdf').load()
        st.session_state.text_splitter=RecursiveCharacterTextSplitter(chunk_size=1000,chunk_overlap=100)
        st.session_state.split_docs=st.session_state.text_splitter.split_documents(st.session_state.loader)
        st.session_state.vectors=FAISS.from_documents(st.session_state.split_docs,st.session_state.embeddings)
question=st.text_input('message')
embedding=st.button('Embedding')
if embedding:
    generate_embedding()
    st.write('embedding is completed now you can ask any question')


if question:
        parser=StrOutputParser()
        document_chain=create_stuff_documents_chain(llm,prompt)
        retriever=st.session_state.vectors.as_retriever()
        retrival_chain=create_retrieval_chain(retriever,document_chain)
        response=retrival_chain.invoke({'input':question})
        st.write(response['answer'])


#Importing necessary libraries
import os 
import streamlit as st
from PyPDF2 import PdfReader
from dotenv import load_dotenv
from langchain_community.vectorstores.faiss import FAISS
from langchain_community.llms import GooglePalm
from langchain.text_splitter import CharacterTextSplitter
from sentence_transformers import SentenceTransformer
from langchain_google_genai import GoogleGenerativeAI
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain.chains.question_answering import load_qa_chain


# main function
def main():
  load_dotenv()
  google_api_key = os.environ.get("GOOGLE_API_KEY")
  
  st.set_page_config(page_title="Chat with PDF",page_icon=':books:')
  st.header("Chat with PDFs📑")

  # upload file
  pdf = st.file_uploader("Please upload your file here.", type="pdf")

  # extract the text
  if pdf is not None:
    pdf_reader = PdfReader(pdf)
    text = ""
    for page in pdf_reader.pages:
      text += page.extract_text()

    # split into chunks
    text_splitter = CharacterTextSplitter(
        separator="\n",
        chunk_size=1000,
        chunk_overlap=200,
        length_function=len
    )
    chunks = text_splitter.split_text(text)

    # create embeddings
    embeddings = HuggingFaceEmbeddings(model_name='paraphrase-MiniLM-L6-v2')
    knowledge_base = FAISS.from_texts(chunks, embeddings)

    # show user input
    user_question = st.text_input("Ask a question about your PDF:")
    if user_question:
      docs = knowledge_base.similarity_search(user_question)
      
      # model
      model =  GoogleGenerativeAI(model="models/text-bison-001", google_api_key=google_api_key)
      chain = load_qa_chain(llm=model, chain_type="stuff")
      
      #response
      response = chain.run(input_documents=docs, question=user_question)
      st.write(response)

if __name__ == '__main__':
  main()

#import langchain dependencies
from langchain.document_loaders import PyPDFLoader
from langchain.indexes import VectorstoreIndexCreator
from langchain.chains import RetrievalQA
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter

#Bring in streamlit for UI dev
import streamlit as st 

#Bring in watsonx interface
from watsonxlangchain import LangChainInterface

#Setup credentials dictionary
creds={
    'apikey':'ZNPRw05jup0f2sFOCFkAtfZskeCPL6fESGaYAq1EWRp7',
     'url':'https://us-south.ml.cloud.ibm.com'
}

#Create LLM using Langchain
llm=LangChainInterface(
    credentials=creds,
    model='meta-llama/llama-2-70b-chat',
    params={
        'decoding_method':'sample',
        'max_new_tokens':200,
        'temperature':0.5
        },
    project_id='dd58941e-28cc-4abe-9189-0bebc2f2edec')
    #this function loads a pdf of your chosing
@st.cache_resource
def load_pdf():
    #update PDF name here to whatever you like
    pdf_name='what is generative ai.pdf'
    loaders=[PyPDFLoader(pdf_name)]
    #create index-aka vector database-aka chromadb
    index=VectorstoreIndexCreator(
        embedding=HuggingFaceEmbeddings(model_name='all-MiniLM-L12-v2'),
        text_splitter=RecursiveCharacterTextSplitter(chunk_size=100,chunk_overlap=0)
        
    ).from_loaders(loaders)
    #return the vector database
    return index
#load er on up
index=load_pdf()

#create a Q&A chain
chain=RetrievalQA.from_chain_type(
    LLm=llm,
    chain_type='stuff',
    retriever=index.vectorstore.as_retriver())

    
  #setup the app title 
st.title('Ask watsonx') 

#
    
  
        
        



#Setup the app title
st.title('Ask watsonx')

#Setup a session state message vaiable to hold all the old messages
if 'messages' not in st.session_state:
    st.session_state.messages
    

#build a prompt input template to display the prompts
prompt=st.chat_input('pass your Prompt here')

#if the user hits enter then
if prompt:
    #display the prompt
    st.chat_message('user').markdown(prompt)
    #store the user prompt in state
    st.session_state.messages.append({'role':'user','content':prompt})
    #send the prompt to the llm
    response=llm(prompt)
    #show the llm response
    st.chat_message('assistant').markdown(response)
    #store the llm response in state
    st.session_state.messages.append(
        {'role':'assistant','content':response})
    
    
    
    
    
    
    


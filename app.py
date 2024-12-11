from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
import streamlit as st
import os
import openai
from dotenv import load_dotenv

load_dotenv()
# os.environ['OPENAI_API_KEY'] = os.getenv('OPENAI_API_KEY')
os.environ['LANGCHAIN_API_KEY'] = os.getenv('LANGCHAIN_API_KEY')
os.environ['LANGCHAIN_PROJECT'] = "SIMPLE CHAT APP USING OPENAI"
os.environ['LANGCHAIN_TRACING_V2'] = "true"

#Prompt template
prompt=ChatPromptTemplate.from_messages([
    ("system","You are a helpfull assistant, Please respond to the question asked"),
    ("user","{question}")
])

def generate_response(question,model,temperature,max_token,api_key):
    openai.api_key=api_key
    llm=ChatOpenAI(model=model)
    output_parser = StrOutputParser()
    chain=prompt|llm|output_parser
    response=chain.invoke({'question':question})
    return response

st.title("Chatbot with OpenAI")
api_key=st.sidebar.text_input("Enter your API key",type='password')

model= st.sidebar.selectbox("Select your OpenAI model ",["gpt-4o","gpt-4o-mini"])

temperature= st.sidebar.slider("Temperature",min_value=0.0,max_value=1.0,value=0.7)
max_token= st.sidebar.slider("Max Token",min_value=50,max_value=300,value=150)

st.write("Enter you question!")
user_input = st.text_input("Question ")

if user_input:
    response = generate_response(user_input,model,temperature,max_token,api_key)
    st.write(response)
else:
    st.write("Please provide the question")
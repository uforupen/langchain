import streamlit as st
from langchain_core.messages import HumanMessage
from langchain_openai import ChatOpenAI 

st.title("Medium Article Generator")
topic = st.text_input("Input your topic of interest")

llm = ChatOpenAI(
    # model="google/gemma-7b-it",  
    model="deepseek/deepseek-r1-0528-qwen3-8b",
    base_url="http://localhost:1234/v1",
    api_key="not-needed",        # still required by LangChain, even if dummy
    temperature=0.9,
    #streaming=True,
)

if topic:
    response = llm.invoke([HumanMessage(content=topic)])
    st.write(response.content)


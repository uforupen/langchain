import sys
import argparse
import streamlit as st
from langchain_core.messages import HumanMessage
from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate

# ----- Parse command-line args -----
parser = argparse.ArgumentParser()
parser.add_argument("--stream", action="store_true", help="Enable streaming mode")
args, _ = parser.parse_known_args()
stream = args.stream or True

title_template = PromptTemplate(
    input_variables=['topic', 'lang'],
    template="Give me a medium article title on {topic} in {language}"
)

# ----- Streamlit UI -----
st.title("Medium Article Generator")
topic = st.text_input("Input your topic of interest")

llm = ChatOpenAI(
    model="google/gemma-7b-it",  
    # model="deepseek/deepseek-r1-0528-qwen3-8b",
    base_url="http://localhost:1234/v1",
    api_key="not-needed",
    temperature=0.9,
    streaming=stream,
)

if topic:
    if stream:
        # Streaming output
        output_area = st.empty()
        streamed_output = ""
        for chunk in llm.stream(title_template.format(topic=topic, language='french')):
            streamed_output += chunk.content or ""
            output_area.markdown(streamed_output)
    else:
        # Normal response
        response = llm.invoke(title_template.format(topic=topic, language='english'))
        st.write(response.content)
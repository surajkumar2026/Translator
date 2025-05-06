import streamlit as st


from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_groq import ChatGroq

from dotenv import load_dotenv
load_dotenv()
import os

groq_api_key = os.getenv("GROQ_API_KEY")

##set up the model 
model = ChatGroq(model="Gemma2-9b-It", groq_api_key=groq_api_key)

system_template = "translate the follwing into {language}"
text = ""  # Initialize text variable
prompt_template = ChatPromptTemplate.from_messages([
    ('system', system_template),
    ('user', '{text}')
])

parser= StrOutputParser()

##define the chain

chain= prompt_template | model|parser

st.title("Language Translator")

text= st.text_area("Enter the text to be translated")
language= st.text_input("Enter target language (e.g.,Hindi, Spanish, French):")

if st.button("Translate"):
        try:
                output = chain.invoke({"text": text, "language": language})
                st.success("Translation Complete:")
                st.write(output)
        except Exception as e:
                st.error(f"Error: {e}")
else:
             st.warning("Please enter both text and target language.")
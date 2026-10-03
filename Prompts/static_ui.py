from langchain_groq import ChatGroq
import streamlit as st
from dotenv import load_dotenv
load_dotenv()




model=ChatGroq(model="openai/gpt-oss-20b")

st.header("Reasearch Tool")

user_input=st.text_input("Enter Your Prompt")

if st.button("Summarize"):
    #model invoke -> with user prompt
    result=model.invoke(user_input)
    #show result -> st.write
    st.write(result.content)
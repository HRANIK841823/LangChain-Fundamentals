from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain.messages import HumanMessage,AIMessage,SystemMessage
import streamlit as st

load_dotenv()

#Model
model=ChatGroq(model="openai/gpt-oss-20b",temperature=0)

#Chat History
chat_history=[ SystemMessage(content="You are a helpful assistant.Always Answer in a short Paragraph (2-4) sentences")]

#chatbot
while True:
    user_input=input('You :')
    chat_history.append(HumanMessage(content=user_input))

    if user_input=="exit":
        break;

    result=model.invoke(chat_history)
    chat_history.append(AIMessage(content=result.content))
    print("AI :",result.content)
print(chat_history)
import streamlit as st
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage,AIMessage,SystemMessage
load_dotenv()


st.header("Chatbot")
#Model
model=ChatGroq(model="openai/gpt-oss-20b",temperature=0)

#Create the chat history only once

if "chat_history" not in st.session_state:
    st.session_state.chat_history=[
        SystemMessage(content="You are a helpful assistant. Always answer in a short paragraph (2-4 sentences).")
    ]


#Display the Previous Message
for message in st.session_state.chat_history:
    if isinstance(message, HumanMessage):
        with st.chat_message("human"):
            st.write(message.content)

    elif isinstance(message, AIMessage):
        with st.chat_message("assistant"):
            st.write(message.content)

#Sidebar
with st.sidebar:
    st.subheader("Chat History")
    if not st.session_state.chat_history:
        st.write("(Empty)")
    else:
        for message in st.session_state.chat_history:
            if isinstance(message, HumanMessage):
                     st.write(f"*Human* : {message.content}")
            
            elif isinstance(message, AIMessage):
                    st.write(f"*AI* : {message.content}")

#take user input

user_input=st.chat_input("Type your message")


if user_input:

    if user_input.strip().lower()=="exit":
        st.stop()
    #store the user's message
    st.session_state.chat_history.append(
        HumanMessage(content=user_input)
    )
    #display the user msg immidiately
    with st.chat_message("human"):
        st.write(user_input)

    result=model.invoke(st.session_state.chat_history)

    st.session_state.chat_history.append(AIMessage(content=result.content))

    with st.chat_message("assistant"):
        st.write(result.content)

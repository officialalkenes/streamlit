import openai as ai
import streamlit as st


if "messages" not in st.session_state:
    st.session_state.messages = []
 

pormpt = st.chat_input("Enter Your Preferred Command")
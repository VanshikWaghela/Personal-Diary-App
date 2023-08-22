import streamlit as st
import pandas as pd
import random

if "messages" not in st.session_state:
    st.session_state.messages=[]

st.title("Welcome to your diary 🥳")
st.header("Dear Diary is here to help you journal your day")
st.text("Before you begin, tell me, How was your day?")
col1,col2,col3,col4,col5 = st.columns(5)

with col1:
    b1 = st.button('😃')
    msg =''
with col2:
    b2 = st.button('😎')
    msg =''
with col3:
    b3 = st.button('😍')
    msg =''
with col4:
    b4 = st.button('😡')
    msg =''
with col5:
    b5 = st.button('😭')
    msg =''

if prompt := b1:
    msg = st.text("Ohh that's great!")
    st.subheader("Let's write it down")
if prompt := b2:
    msg = st.text("Party scenes huh!!")
    st.subheader("Give me all the details")
if prompt := b3:
    msg = st.text("That's lovelyy")
    st.subheader("Just look at that smile")
if prompt := b4:
    msg = st.text("Chill dude, here, have some ice -🧊")
    st.subheader("Let it all out.")
if prompt := b5:
    msg = st.text("Everything will be alright, don't give up")
    st.subheader("Writing helps you calm down")

msg_list = ["What is up?","Maintaining a diary helps you during fights","Look who's here finally","Write as if your life depends on it (coz sometimes it does)","What is the tea today?","OMG! so you have the time to write your diary"]
random_msg = random.choice(msg_list)

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])


if prompt := st.chat_input(random_msg):
    # Display user message in chat message container
    with st.chat_message("user"):
        st.markdown(prompt)
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})






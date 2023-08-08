from ChatApp import ChatApp
import streamlit as st
from streamlit_chat import message




st.set_page_config(
    page_title="SmartAssistant - DigitalSEO",
    page_icon="	✍️",
    initial_sidebar_state="collapsed",
    layout="centered")


# Storing the chat
if "generated" not in st.session_state:
    st.session_state["generated"] = []

if "past" not in st.session_state:
    st.session_state["past"] = []

# Creating the chatbot interface
st.title("🤖 SmartAssistant Powered by GPT4")
st.subheader("")

def getprev_chat():
    previousmessages =[]
    for i in range(len(st.session_state["generated"]) - 1, -1, -1):
        previousmessages.append({"role": "user", "content": st.session_state["past"][i]})
        previousmessages.append({"role": "system", "content": st.session_state["generated"][i]})
    return previousmessages

def showpage():
    placeholder = st.empty()
    with placeholder.form(key='curation_form', clear_on_submit=False):
        f1, f2 = st.columns([1, 0.5])
        with f1:
            user_input = st.text_input("You: ", "Hello, how are you?", key="input" )
        with f2:
            submit = st.form_submit_button("Submit")

        if submit:
            app = ChatApp()
            gptmessage = getprev_chat()
            gptmessage.append({"role": "user", "content": user_input})
            gptoutput = app.chat(gptmessage)
            print("Output" + str(gptmessage))
            print("=-----------------------------------")
            st.session_state.past.append(user_input)
            st.session_state.generated.append(gptoutput)

        if st.session_state["generated"]:
            for i in range(len(st.session_state["generated"]) - 1, -1, -1):
                message(st.session_state["generated"][i], key=str(i))
                message(st.session_state["past"][i], is_user=True, key=str(i) + "_user")

if "passcode" not in st.session_state:
    st.session_state["passcode"] = "None"

auth_placeholder = st.empty()
passcode = auth_placeholder.text_input("Enter your Passcode:", type="password", max_chars=10, value=st.session_state.passcode,)
st.session_state.passcode = passcode

if st.session_state.passcode in ['Adtagz123','Adtagz2023']:
    auth_placeholder.empty()
    showpage()

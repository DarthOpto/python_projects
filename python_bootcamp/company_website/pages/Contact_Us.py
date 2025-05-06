import pandas as pd
from send_email import send_email
import streamlit as st

topics = pd.read_csv("topics.csv")
st.header("Contact Me")

with st.form(key="contact_form"):
    user_email = st.text_input("Your email address: ")
    topic_dropdown = st.selectbox("What topic do you want to discuss?", topics['topic'])
    user_message = st.text_area("Message")
    msg = f"""\
Subject: New email from {user_email}

From: {user_email}
Topic: {topic_dropdown}
{user_message}"""
    submit_btn = st.form_submit_button("Submit")
    if submit_btn:
        send_email(message=msg)
        st.info("Your email was sent successfully!")
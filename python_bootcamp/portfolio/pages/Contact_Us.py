import streamlit as st
from send_email import send_email

st.header("Contact Me")

with st.form(key="contact_form"):
    user_email = st.text_input("Your email address: ")
    user_message = st.text_area("Message")
    msg = user_message + "\n" + user_email
    submit_btn = st.form_submit_button("Submit")
    if submit_btn:
        send_email(message=msg)
        st.info("Your email was sent successfully!")

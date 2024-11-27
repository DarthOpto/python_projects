import streamlit as st

st.set_page_config()
col1, col2 = st.columns(2)

with col1:
    st.image("images/photo.jpg", width=200)

with col2:
    st.title("Curtis Salisbury")
    content = """Hi, I am Curtis. I have been doing automated and manual software quality assurance
     for 17 years. I am now branching out in hopes of becoming a Python developer. Below is a list of projects I have
     worked on, and a link to their source code."""
    st.info(content)
import pandas
import streamlit as st
import pandas as pd

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

content2 = """Below you can find some of the apps I have built in Python. Feel free to contact me."""
st.write(content2)

data = pd.read_csv("data.csv", sep=";")
col3, empty_col, col4 = st.columns([1.5, 0.5, 1.5])

with col3:
    for index, row in data[:10].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row['image'])
        st.write(f"[Source Code]({row['url']})")

with col4:
    for index, row in data[10:].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row['image'])
        st.write(f"[Source Code]({row['url']})")
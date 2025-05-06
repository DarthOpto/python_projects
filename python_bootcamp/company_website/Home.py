import streamlit as st
import pandas as pd

st.set_page_config(page_title="The Best Company",
                   page_icon="images/company_icon.png",
                   layout="wide")

st.title("The Best Company")
st.write("""Lorem ipsum dolor sit amet, consectetur adipiscing elit. Cras a neque vitae enim accumsan pulvinar feugiat 
quis ante. Nunc commodo at est id dapibus. Mauris et condimentum lacus. Cras vehicula ligula at libero 
imperdiet porttitor. Suspendisse feugiat vulputate ante at euismod. Donec id tortor lobortis ligula faucibus bibendum. 
Sed bibendum euismod posuere.

Mauris mattis mollis purus, eu bibendum augue. Pellentesque quis sapien ut dolor vestibulum bibendum. Nunc rhoncus 
dictum mi, at ullamcorper enim pharetra ac. Nam eget porttitor quam, eget rutrum magna. Etiam imperdiet risus non 
porttitor rutrum. Maecenas id neque vel tellus elementum rhoncus. Nulla id elit accumsan, porta mauris eget, viverra 
erat. Praesent eros ante, pretium vitae purus eu, posuere eleifend ex. Nulla et quam eu ligula varius dictum quis 
tincidunt ex. Nulla facilisi. Praesent nulla metus, euismod quis vehicula in, congue a nunc. 
Nulla sollicitudin efficitur ipsum, in molestie nunc. Aliquam quis arcu sed magna venenatis molestie. Pellentesque in 
eleifend lectus. Vestibulum pellentesque magna sit amet hendrerit pellentesque.""")

st.subheader("Our Team")

data = pd.read_csv('data.csv')
col1, empty1, col2, empty2, col3 = st.columns([1.5, 0.5, 1.5, 0.5, 1.5])

# add items to the first column
with col1:
    for index, row in data[:4].iterrows():
        st.subheader(f"{row['first name'].title()} {row['last name'].title()}")
        st.write(row["role"])
        st.image("images/" + row["image"])

# add items to the first column
with col2:
    for index, row in data[4:8].iterrows():
        st.subheader(f"{row['first name'].title()} {row['last name'].title()}")
        st.write(row["role"])
        st.image("images/" + row["image"])

# add items to the third column
with col3:
    for index, row in data[8:].iterrows():
        st.subheader(f"{row['first name'].title()} {row['last name'].title()}")
        st.write(row["role"])
        st.image("images/" + row["image"])
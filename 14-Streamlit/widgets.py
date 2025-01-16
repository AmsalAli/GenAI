import streamlit as st
import pandas as pd

# you can also streamlit.io fot more streamlit componments

st.title("Strreamlit Text input")

name = st.text_input("Enter your name")

age = st.slider("Enter your age", 0, 100,25)

st.write(f"Your age is {age}")

options = ["Pyhton", "Java", "C++", "javascript"]
choice = st.selectbox("Choose a programming language", options)
st.write(f"You selected {choice}")

if name:
    st.write(f"Assalamu Alaikum {name}")
    
    
data = {
    "Name": ["John", "Anna", "Peter", "Linda"],
    "Age": [28, 45, 33, 30],
    "city": ["New York", "Paris", "Berlin", "London"]
}

df = pd.DataFrame(data)
df.to_csv("sampledata.csv")
st.write(df)

uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write(df)
        
    
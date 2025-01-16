import streamlit as st
import pandas as pd
import numpy as np

st.title("Welcome to My Streamlit Web Page")

st.write("This is a simple web page created using Streamlit.")

# create a simple dataframe

df = pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
})

# Displat the dataframe
st.write("Here is a DataFrame:")
st.write(df)

# create a line chart
chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['a', 'b', 'c']
)

st.line_chart(chart_data)
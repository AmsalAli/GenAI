import streamlit as st

# Set the title of the web page
st.title("Welcome to My Streamlit Web Page")

# Add a header
st.header("This is a header")

# Add a subheader
st.subheader("This is a subheader")

# Add some text
st.text("This is some text on the web page.")

# Add a markdown
st.markdown("### This is a markdown section")

# Add an input box
user_input = st.text_input("Enter some text")

# Display the input text
st.write("You entered:", user_input)

# Add a button
if st.button("Click Me"):
    st.write("Button clicked!")

# Add a slider
slider_value = st.slider("Select a value", 0, 100)
st.write("Slider value:", slider_value)

# Add a selectbox
option = st.selectbox("Select an option", ["Option 1", "Option 2", "Option 3"])
st.write("You selected:", option)
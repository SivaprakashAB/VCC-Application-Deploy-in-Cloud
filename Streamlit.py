import streamlit as st

# Title of the app
st.title("Simple Streamlit App")

# Input text from the user
user_input = st.text_input("Enter your name")

# Button to trigger an action
if st.button("Submit"):
    # Output the input value as a greeting message
    st.write(f"Hello, {user_input}!")

# Add a slider
age = st.slider("Select your age", 1, 100, 25)
st.write(f"Your age is: {age}")

# Display a checkbox
if st.checkbox("Show additional information"):
    st.write("You checked the box!")

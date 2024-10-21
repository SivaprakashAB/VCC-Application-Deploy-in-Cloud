import streamlit as st

# Injecting custom CSS for advanced styling
st.markdown(
    """
    <style>
    .main {
        background-color: #f0f8ff;
    }
    .title {
        font-size: 50px;
        color: #4CAF50;
        text-align: center;
    }
    .info-text {
        font-size: 18px;
        color: #ff6347;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Title of the app
st.markdown('<p class="title">Simple Streamlit App with CSS</p>', unsafe_allow_html=True)

# Input text from the user
user_input = st.text_input("Enter your name")

# Button to trigger an action
if st.button("Submit"):
    # Output the input value as a greeting message
    st.markdown(f'<p class="info-text">Hello, {user_input}!</p>', unsafe_allow_html=True)

# Add a slider for selecting age
age = st.slider("Select your age", 1, 100, 25)
st.markdown(f'<p class="info-text">Your age is: {age}</p>', unsafe_allow_html=True)

# Display a checkbox for additional information
if st.checkbox("Show additional information"):
    st.markdown('<p class="info-text">You checked the box!</p>', unsafe_allow_html=True)

# Additional advanced widget: Color Picker
favorite_color = st.color_picker("Pick your favorite color")
st.write(f"Your favorite color is: {favorite_color}")

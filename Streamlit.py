import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import plotly.express as px

# App Title
st.title("Advanced Streamlit Application")

# Sidebar navigation
st.sidebar.title("Navigation")
options = st.sidebar.radio("Select a page:", ["Home", "User Inputs", "Visualizations", "Contact"])

# Home Page
if options == "Home":
    st.header("Welcome to the Advanced Streamlit App!")
    st.markdown("""
        This app demonstrates:
        - User Input Forms and Sliders
        - Interactive Visualizations (Matplotlib and Plotly)
    """)

# User Inputs Page
elif options == "User Inputs":
    st.header("User Inputs and Forms")

    # Text input form
    user_name = st.text_input("Enter your name")
    st.write(f"Hello, {user_name}!")

    # Age slider
    age = st.slider("Select your age", 1, 100, 25)
    st.write(f"Your age is {age}.")

    # Radio button for selecting gender
    gender = st.radio("Select your gender:", ("Male", "Female", "Other"))
    st.write(f"You selected: {gender}")

    # Multiselect for hobbies
    hobbies = st.multiselect("Select your hobbies:", ['Reading', 'Traveling', 'Sports', 'Music'])
    st.write(f"Your hobbies are: {', '.join(hobbies)}")

    # Numeric input
    number = st.number_input("Pick a number", min_value=0, max_value=100, value=10)
    st.write(f"You selected {number}")

# Visualizations Page
elif options == "Visualizations":
    st.header("Dynamic Visualizations")

    # Matplotlib visualization (Sin wave)
    st.subheader("Matplotlib Sin and Cos Wave")
    x = np.linspace(0, 10, 100)
    y_sin = np.sin(x)
    y_cos = np.cos(x)
    
    plt.figure(figsize=(10, 5))
    plt.plot(x, y_sin, label="Sin(x)", color="blue")
    plt.plot(x, y_cos, label="Cos(x)", color="red")
    plt.legend()
    st.pyplot(plt)

    # Plotly interactive scatter plot
    st.subheader("Plotly Interactive Scatter Plot")
    x = np.random.randn(100)
    y = np.random.randn(100)
    
    fig = px.scatter(x=x, y=y, labels={'x': 'Random X', 'y': 'Random Y'}, title="Random Scatter Plot")
    st.plotly_chart(fig)

# Contact Page
elif options == "Contact":
    st.header("Contact Us")

    with st.form(key="contact_form"):
        name = st.text_input("Name")
        email = st.text_input("Email")
        message = st.text_area("Message")

        submit_button = st.form_submit_button("Submit")
        
        if submit_button:
            st.success("Form submitted successfully!")
            st.write(f"Name: {name}")
            st.write(f"Email: {email}")
            st.write(f"Message: {message}")

# Footer
st.sidebar.markdown("""
    **Developed by:** Your Name  
    **GitHub:** [Your GitHub](https://github.com/yourgithub)
""")

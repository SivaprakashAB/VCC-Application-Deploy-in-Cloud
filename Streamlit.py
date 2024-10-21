import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px

# App Title
st.title("Advanced Streamlit Application")

# Sidebar navigation
st.sidebar.title("Navigation")
options = st.sidebar.radio("Select a page:", ["Home", "Data Upload", "Visualizations", "Contact"])

# Home Page
if options == "Home":
    st.header("Welcome to the Advanced Streamlit App!")
    st.markdown("""
        This app showcases advanced features like:
        - Data Upload and Processing
        - Dynamic Data Visualizations (Matplotlib, Plotly)
        - User Forms and Interactions
    """)

# Data Upload Page
elif options == "Data Upload":
    st.header("Upload Your Dataset")
    
    # File uploader for CSV data
    uploaded_file = st.file_uploader("Choose a CSV file", type="csv")
    
    if uploaded_file is not None:
        # Read CSV and display
        df = pd.read_csv(uploaded_file)
        st.write("Data preview:")
        st.dataframe(df.head())
        
        # Show basic data statistics
        if st.checkbox("Show data statistics"):
            st.write(df.describe())

# Visualizations Page
elif options == "Visualizations":
    st.header("Data Visualizations")
    
    if uploaded_file is not None:
        # Option to select a column for visualization
        columns = df.columns.tolist()
        column_to_plot = st.selectbox("Choose a column to visualize", columns)
        
        # Matplotlib Bar Chart
        st.subheader(f"Matplotlib Bar Chart of {column_to_plot}")
        plt.figure(figsize=(10, 5))
        df[column_to_plot].value_counts().plot(kind='bar', color='skyblue')
        st.pyplot(plt)
        
        # Plotly Scatter Plot
        st.subheader(f"Plotly Scatter Plot of {column_to_plot} vs index")
        fig = px.scatter(df, x=df.index, y=column_to_plot, title=f"Scatter Plot of {column_to_plot}")
        st.plotly_chart(fig)

    else:
        st.warning("Please upload a dataset to visualize.")

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

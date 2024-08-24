import streamlit as st
import graphviz as graphviz
st.title('Graphviz')
# Creating graph object
st.graphviz_chart('''
digraph {
"Training Data" -> "ML Algorithm"
"ML Algorithm" -> "Model"
"Model" -> "Result Forecasting"
"New Data" -> "Model"
}
''')
import streamlit as st

# Use st.markdown to inject custom CSS
st.markdown(
    """
    <style>
    body {
        background-color: red; /* Light blue background */
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Your Streamlit app content goes here

st.write("This page has a custom background color!")

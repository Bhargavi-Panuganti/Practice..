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

import streamlit as st
import google.generativeai as genai
import matplotlib.pyplot as plt
import numpy as np
import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv('GOOGLE_API_KEY')
genai.configure(api_key=api_key)

def analyze_time_complexity(code):
    model = genai.GenerativeModel('gemini-pro')
    prompt = f"Analyze the time complexity of the following code and return only the Big O notation (e.g., O(n), O(n^2), O(log n), etc.):\n\n{code}"
    response = model.generate_content(prompt)
    return response.text.strip()

def plot_time_complexity(complexity):
    plt.figure(figsize=(6, 4))
    plt.style.use('dark_background')

    n = np.linspace(1, 100, 1000)

    if complexity == 'O(1)':
        y = np.ones_like(n)
    elif complexity == 'O(log n)':
        y = np.log(n)
    elif complexity == 'O(n)':
        y = n
    elif complexity == 'O(n log n)':
        y = n * np.log(n)
    elif complexity == 'O(n^2)':
        y = n**2
    elif complexity == 'O(2^n)':
        y = 2**n
    else:
        st.error(f"Unsupported complexity: {complexity}")
        return None

    plt.plot(n, y, color='purple')
    plt.title(f"Time Complexity: {complexity}")
    plt.xlabel('n')
    plt.ylabel('Time')
    plt.ylim(bottom=0)
    plt.grid(True, alpha=0.3)

    return plt

st.title("Code Time Complexity Analyzer")

if 'code' not in st.session_state:
    st.session_state.code = ''
if 'complexity' not in st.session_state:
    st.session_state.complexity = None

st.session_state.code = st.text_area("Enter your code here:", value=st.session_state.code, height=200, key="code_input")

col1, col2, col3 = st.columns([1, 1, 4])

if col1.button("Analyze"):
    if st.session_state.code:
        with st.spinner("Analyzing..."):
            st.session_state.complexity = analyze_time_complexity(st.session_state.code)
    else:
        st.warning("Please enter some code to analyze.")

if col2.button("Clear"):
    st.session_state.code = ''
    st.session_state.complexity = None
    st.experimental_rerun()

if st.session_state.complexity:
    st.write(f"Time Complexity: {st.session_state.complexity}")
    fig = plot_time_complexity(st.session_state.complexity)
    if fig:
        st.pyplot(fig)

st.markdown("---")
st.markdown("This tool uses the Gemini API to analyze code time complexity.")

from footer import *
footer()
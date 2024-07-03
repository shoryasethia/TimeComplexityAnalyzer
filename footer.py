import streamlit as st

def footer():
    footer = """
    <style>
        .footer {
            position: fixed;
            left: 0;
            bottom: 0;
            width: 100%;
            background-color: #0E1117;
            color: #FAFAFA;
            text-align: center;
            padding: 10px;
            font-size: 14px;
        }
    </style>
    <div class="footer">
        <p>Developed by Shorya Sethia | <a href="https://github.com/shoryasethia" target="_blank">GitHub</a> | © 2024</p>
    </div>
    """
    st.markdown(footer, unsafe_allow_html=True)
import streamlit as st
from qa_bot import ask_question

# Page Configuration
st.set_page_config(page_title="HR Policy Chatbot", page_icon="💼", layout="centered")

# Custom Styling
st.markdown("""
    <style>
    body {
        background-color: #f5f7fa;
        font-family: 'Segoe UI', sans-serif;
    }
    .main {
        background-color: #f5f7fa;
    }
    .stTextInput > div > div > input {
        background-color: #ffffff;
        color: #333333;
        font-size: 16px;
        padding: 10px;
        border-radius: 8px;
        border: 1px solid #ddd;
    }
    .answer-box {
        background-color: #e8f0fe;
        padding: 1.2rem;
        border-radius: 10px;
        border-left: 6px solid #1a73e8;
        margin-top: 20px;
        font-size: 16px;
        line-height: 1.6;
        color: #1a1a1a;
    }
    .footer {
        text-align: center;
        font-size: 0.9rem;
        color: #888888;
        margin-top: 40px;
    }
    </style>
""", unsafe_allow_html=True)

# Title and Description
st.markdown("<h1 style='color:#1a73e8;'>🤖 HR Policy Chatbot</h1>", unsafe_allow_html=True)
st.markdown("<p style='font-size:18px;'>Ask me anything about your company's HR policies — from leave rules to appraisal, reimbursement, and more! 📄</p>", unsafe_allow_html=True)

# User Input
query = st.text_input("💬 Type your question below:")

# Generate Answer
if query:
    with st.spinner("🔍 Fetching answer..."):
        answer = ask_question(query)
        st.markdown(f'<div class="answer-box">💡 <strong>Answer:</strong><br>{answer}</div>', unsafe_allow_html=True)

# Footer
st.markdown('<div class="footer">🚀 Created by <strong>Vivek Gaur</strong> for learning purposes</div>', unsafe_allow_html=True)

import streamlit as st

def load_custom_css():
    """Load custom CSS styles"""
    st.markdown("""
    <style>
        .main-header {
            font-size: 2.5rem;
            font-weight: bold;
            color: #1f77b4;
            text-align: center;
            margin-bottom: 2rem;
        }
        .metric-card {
            background-color: #f0f2f6;
            padding: 1rem;
            border-radius: 10px;
            border-left: 5px solid #1f77b4;
        }
        .prediction-box {
            background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
            color: white;
            padding: 1.5rem;
            border-radius: 15px;
            text-align: center;
            margin: 1rem 0;
        }
        .sidebar .sidebar-content {
            background-color: #f8f9fa;
        }
    </style>
    """, unsafe_allow_html=True)
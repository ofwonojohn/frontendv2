import streamlit as st
from config.settings import MARKET_OPTIONS, AI_MODELS, RISK_LEVELS, PREDICTION_HORIZONS
from components.user_dashboard import UserDashboard

def render_sidebar():
    """Render sidebar with trading parameters"""
    
    # User info section
    render_user_info_section()
    
    st.sidebar.markdown("---")
    st.sidebar.header("📊 Trading Parameters")
    
    # Market selection
    market_type = st.sidebar.selectbox("Select Market Type", list(MARKET_OPTIONS.keys()))
    
    # Asset selection
    selected_asset = st.sidebar.selectbox(
        f"Select {market_type} Asset", 
        MARKET_OPTIONS[market_type]
    )
    
    # Trading parameters
    prediction_horizon = st.sidebar.selectbox("Prediction Horizon", PREDICTION_HORIZONS)
    
    investment_amount = st.sidebar.number_input(
        "Investment Amount ($)",
        min_value=100,
        max_value=100000,
        value=1000,
        step=100
    )
    
    risk_level = st.sidebar.select_slider("Risk Tolerance", options=RISK_LEVELS, value="Medium")
    
    model_type = st.sidebar.selectbox("AI Model", AI_MODELS)
    
    # Additional features
    st.sidebar.markdown("---")
    render_additional_features()
    
    return {
        'market_type': market_type,
        'selected_asset': selected_asset,
        'prediction_horizon': prediction_horizon,
        'investment_amount': investment_amount,
        'risk_level': risk_level,
        'model_type': model_type
    }

def render_user_info_section():
    """Render user info in sidebar"""
    username = st.session_state.get('username', 'Unknown')
    is_demo = st.session_state.get('is_demo', False)
    
    st.sidebar.markdown(f"""
    ### 👤 User: {username}
    {"🔧 Demo Mode" if is_demo else "🌟 Premium User"}
    """)
    
    # Quick stats
    if st.sidebar.button("📊 View Dashboard"):
        st.session_state.show_dashboard = True
    
    if st.sidebar.button("📋 Activity Log"):
        st.session_state.show_activity = True

def render_additional_features():
    """Render additional feature buttons"""
    st.sidebar.markdown("### 🛠️ Additional Features")
    
    if st.sidebar.button("📊 Market Overview"):
        st.sidebar.info("Market overview feature coming soon!")
    
    if st.sidebar.button("📈 Backtesting"):
        st.sidebar.info("Backtesting module in development!")
    
    if st.sidebar.button("⚙️ Model Settings"):
        st.sidebar.info("Advanced settings panel coming soon!")
    
    if st.sidebar.button("💾 Save Prediction"):
        if hasattr(st.session_state, 'prediction_data'):
            st.sidebar.success("Prediction saved to your history!")
        else:
            st.sidebar.warning("Generate a prediction first!")
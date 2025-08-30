import streamlit as st
from config.settings import PAGE_CONFIG
from components.auth import AuthManager
from components.sidebar import render_sidebar
from components.charts import render_charts
from components.metrics import render_metrics
from services.ai_predictor import AIPredictor
from styles.css_loader import load_custom_css
from utils.session_manager import SessionManager

def main():
    # Configure page
    st.set_page_config(**PAGE_CONFIG)
    
    # Load custom styles
    load_custom_css()
    
    # Initialize session manager
    session_manager = SessionManager()
    
    # Initialize auth manager
    auth_manager = AuthManager()
    
    # Check if user is logged in
    if not st.session_state.get('logged_in', False):
        auth_manager.render_auth_page()
        return
    
    # Main app header with user info
    render_header_with_user()
    
    # Render sidebar and get user inputs
    user_inputs = render_sidebar()
    
    # Main prediction button
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if st.button("🔮 Generate Prediction", type="primary", use_container_width=True):
            # Log user activity
            session_manager.log_activity("prediction_generated", user_inputs)
            
            # Initialize AI predictor
            predictor = AIPredictor(user_inputs)
            
            # Generate prediction with progress
            prediction_data = predictor.generate_prediction()
            
            # Store in session state
            st.session_state.prediction_data = prediction_data
            st.session_state.user_inputs = user_inputs
    
    # Display results if available
    if hasattr(st.session_state, 'prediction_data'):
        render_metrics(st.session_state.prediction_data, st.session_state.user_inputs)
        render_charts(st.session_state.prediction_data, st.session_state.user_inputs)
    
    # Footer
    st.markdown("---")
    st.markdown("⚠️ **Disclaimer**: Demo AI trading system. Consult financial advisors.")

def render_header_with_user():
    """Render header with user information"""
    col1, col2, col3 = st.columns([2, 3, 1])
    
    with col1:
        st.markdown(f"👋 Welcome, **{st.session_state.username}**")
    
    with col2:
        st.markdown('<h1 class="main-header">🤖 AI Trading Prediction System</h1>', 
                    unsafe_allow_html=True)
    
    with col3:
        if st.button("🚪 Logout"):
            SessionManager.logout()
            st.rerun()

if __name__ == "__main__":
    main()
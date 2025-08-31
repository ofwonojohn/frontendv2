import streamlit as st
from config.settings import PAGE_CONFIG
from components.auth import AuthManager
from components.sidebar import render_sidebar
from components.charts import render_charts
from components.metrics import render_metrics
from services.ai_predictor import AIPredictor
from styles.css_loader import load_custom_css  # Clean import
from utils.session_manager import SessionManager

def main():
    # Configure page
    st.set_page_config(**PAGE_CONFIG)
    
    # Load all styling (one clean import)
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
    
    # Main prediction button with professional styling
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.markdown('<div class="professional-card">', unsafe_allow_html=True)
        if st.button("🔮 Generate AI Prediction", type="primary", use_container_width=True):
            # Log user activity
            session_manager.log_activity("prediction_generated", user_inputs)
            
            # Initialize AI predictor
            predictor = AIPredictor(user_inputs)
            
            # Generate prediction with progress
            prediction_data = predictor.generate_prediction()
            
            # Store in session state
            st.session_state.prediction_data = prediction_data
            st.session_state.user_inputs = user_inputs
        st.markdown('</div>', unsafe_allow_html=True)
    
    # Display results if available
    if hasattr(st.session_state, 'prediction_data'):
        render_metrics(st.session_state.prediction_data, st.session_state.user_inputs)
        render_charts(st.session_state.prediction_data, st.session_state.user_inputs)
    
    # Professional footer
    render_footer()

def render_header_with_user():
    """Render professional header with user information"""
    # User info section with proper Streamlit layout
    col1, col2, col3 = st.columns([3, 4, 1])
    
    with col1:
        st.markdown(f"""
        <div class="professional-card" style="padding: 1rem;">
            <h3 style="margin: 0; color: var(--text-primary);">
                👋 Welcome, <strong>{st.session_state.username}</strong>
            </h3>
            <p style="margin: 0; color: var(--text-secondary); font-size: 0.9rem;">
                {"Demo" if st.session_state.get('is_demo', False) else "Premium"} Account • 
                Last login: {st.session_state.get('login_time', 'N/A')[:19]}
            </p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        # Main header
        st.markdown('<h1 class="main-header">🤖 AI Trading Prediction System</h1>', 
                    unsafe_allow_html=True)
    
    with col3:
        # Working Streamlit logout button
        if st.button("🚪 Logout", type="secondary"):
            # Clear all session state
            for key in list(st.session_state.keys()):
                del st.session_state[key]
            # Force page refresh to show login screen
            st.rerun()

def render_footer():
    """Render professional footer"""
    st.markdown("---")
    st.markdown("""
    <div style="text-align: center; padding: 2rem; color: var(--text-muted);">
        <p>⚠️ <strong>Disclaimer:</strong> This is a demo AI trading system. 
        Always consult with financial advisors before making investment decisions.</p>
        <p style="font-size: 0.8rem; margin-top: 1rem;">
            © 2025 AI Trading System • Built with Streamlit • Version 1.0
        </p>
    </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
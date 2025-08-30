import streamlit as st
from datetime import datetime
from utils.user_database import UserDatabase

class SessionManager:
    def __init__(self):
        self.user_db = UserDatabase()
        self.initialize_session()
    
    def initialize_session(self):
        """Initialize session state variables"""
        if 'logged_in' not in st.session_state:
            st.session_state.logged_in = False
        
        if 'username' not in st.session_state:
            st.session_state.username = None
        
        if 'login_time' not in st.session_state:
            st.session_state.login_time = None
        
        if 'prediction_history' not in st.session_state:
            st.session_state.prediction_history = []
    
    def log_activity(self, activity_type, details=None):
        """Log user activity during session"""
        if st.session_state.get('logged_in', False):
            username = st.session_state.username
            self.user_db.log_user_activity(username, activity_type, details)
    
    @staticmethod
    def logout():
        """Logout user and clear session"""
        if st.session_state.get('logged_in', False):
            # Log logout activity
            user_db = UserDatabase()
            user_db.log_user_activity(st.session_state.username, "logout")
        
        # Clear session state
        for key in list(st.session_state.keys()):
            del st.session_state[key]
    
    def get_session_duration(self):
        """Get current session duration"""
        if st.session_state.get('login_time'):
            login_time = datetime.fromisoformat(st.session_state.login_time)
            return datetime.now() - login_time
        return None
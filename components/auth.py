import streamlit as st
import hashlib
from utils.user_database import UserDatabase
from components.user_dashboard import UserDashboard
from datetime import datetime

st.session_state.login_time = datetime.now().isoformat()



class AuthManager:
    def __init__(self):
        self.user_db = UserDatabase()
        self.dashboard = UserDashboard()
    
    def render_auth_page(self):
        """Main authentication page"""
        st.markdown("""
        <div style="text-align: center; padding: 2rem;">
            <h1>🔐 AI Trading System</h1>
            <p style="font-size: 1.2rem; color: #666;">
                Secure access to advanced trading predictions
            </p>
        </div>
        """, unsafe_allow_html=True)
        
        # Create tabs
        login_tab, register_tab, profile_tab = st.tabs(["🔑 Login", "📝 Register", "👤 Demo Profile"])
        
        with login_tab:
            self.render_login_form()
        
        with register_tab:
            self.render_registration_form()
        
        with profile_tab:
            self.render_demo_login()
    
    def render_login_form(self):
        """Render login form"""
        st.markdown("### 🔑 Login to Your Account")
        
        with st.form("login_form"):
            username = st.text_input("Username", placeholder="Enter your username")
            password = st.text_input("Password", type="password", placeholder="Enter your password")
            
            col1, col2 = st.columns(2)
            with col1:
                remember_me = st.checkbox("Remember me")
            with col2:
                show_demo = st.checkbox("Use demo account")
            
            login_button = st.form_submit_button("🔑 Login", use_container_width=True)
            
            if login_button:
                if show_demo:
                    self.demo_login()
                elif self.authenticate_user(username, password):
                    self.login_user(username, remember_me)
                else:
                    st.error("❌ Invalid credentials. Try the demo account!")
    
    def render_registration_form(self):
        """Render registration form"""
        st.markdown("### 📝 Create New Account")
        
        with st.form("registration_form"):
            col1, col2 = st.columns(2)
            
            with col1:
                username = st.text_input("Username*", placeholder="Choose a username")
                email = st.text_input("Email*", placeholder="your.email@example.com")
                password = st.text_input("Password*", type="password", placeholder="Min 6 characters")
                confirm_password = st.text_input("Confirm Password*", type="password")
            
            with col2:
                full_name = st.text_input("Full Name", placeholder="Your full name")
                phone = st.text_input("Phone", placeholder="Your phone number")
                experience_level = st.selectbox("Trading Experience", 
                                              ["Beginner", "Intermediate", "Advanced", "Expert"])
                preferred_markets = st.multiselect("Preferred Markets", 
                                                 ["Forex", "Stocks", "Crypto", "Commodities"])
            
            terms = st.checkbox("I agree to Terms & Conditions")
            register_button = st.form_submit_button("📝 Create Account", use_container_width=True)
            
            if register_button:
                if self.validate_and_register(username, email, password, confirm_password, 
                                            full_name, phone, experience_level, 
                                            preferred_markets, terms):
                    st.success("✅ Account created! Please login with your credentials.")
    
    def render_demo_login(self):
        """Render demo login option"""
        st.markdown("### 👤 Try Demo Account")
        st.info("Experience the platform without registration")
        
        if st.button("🚀 Enter as Demo User", use_container_width=True):
            self.demo_login()
    
    def demo_login(self):
        """Login with demo account"""
        st.session_state.logged_in = True
        st.session_state.username = "demo_user"
        st.session_state.is_demo = True
        st.session_state.login_time = datetime.now().isoformat()
        
        st.success("✅ Logged in as Demo User!")
        st.rerun()
    
    def authenticate_user(self, username, password):
        """Authenticate user credentials"""
        if not username or not password:
            return False
        return self.user_db.verify_user(username, self.hash_password(password))
    
    def login_user(self, username, remember_me):
        """Login user and set session"""
        st.session_state.logged_in = True
        st.session_state.username = username
        st.session_state.remember_me = remember_me
        st.session_state.is_demo = False
        st.session_state.login_time = datetime.now().isoformat()
        
        # Log login activity
        self.user_db.log_user_activity(username, "login")
        
        st.success("✅ Login successful!")
        st.rerun()
    
    def validate_and_register(self, username, email, password, confirm_password, 
                            full_name, phone, experience_level, preferred_markets, terms):
        """Validate and register new user"""
        
        # Validation
        if not all([username, email, password, terms]):
            st.error("❌ Please fill required fields and accept terms")
            return False
        
        if len(username) < 3:
            st.error("❌ Username must be at least 3 characters")
            return False
        
        if len(password) < 6:
            st.error("❌ Password must be at least 6 characters")
            return False
        
        if password != confirm_password:
            st.error("❌ Passwords do not match")
            return False
        
        if "@" not in email or "." not in email:
            st.error("❌ Please enter a valid email address")
            return False
        
        # Create user
        user_data = {
            'username': username,
            'email': email,
            'password': self.hash_password(password),
            'full_name': full_name,
            'phone': phone,
            'experience_level': experience_level,
            'preferred_markets': preferred_markets,
            'created_at': datetime.now().isoformat(),
            'last_login': None
        }
        
        return self.user_db.create_user(user_data)
    
    @staticmethod
    def hash_password(password):
        """Hash password for security"""
        return hashlib.sha256(password.encode()).hexdigest()
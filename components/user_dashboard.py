import streamlit as st
import pandas as pd
from datetime import datetime, timedelta
from utils.user_database import UserDatabase

class UserDashboard:
    def __init__(self):
        self.user_db = UserDatabase()
    
    def render_user_profile(self):
        """Render user profile section"""
        username = st.session_state.username
        user_info = self.user_db.get_user_info(username)
        
        st.subheader("👤 User Profile")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown(f"""
            **Username:** {username}  
            **Email:** {user_info.get('email', 'N/A')}  
            **Experience:** {user_info.get('experience_level', 'N/A')}  
            **Member Since:** {user_info.get('created_at', 'N/A')[:10]}
            """)
        
        with col2:
            preferred_markets = user_info.get('preferred_markets', [])
            if preferred_markets:
                st.markdown("**Preferred Markets:**")
                for market in preferred_markets:
                    st.markdown(f"• {market}")
    
    def render_activity_log(self):
        """Render user activity log"""
        st.subheader("📋 Recent Activity")
        
        username = st.session_state.username
        activities = self.user_db.get_user_activities(username, limit=20)
        
        if activities:
            # Convert to DataFrame for better display
            df_activities = pd.DataFrame(activities)
            df_activities['timestamp'] = pd.to_datetime(df_activities['timestamp'])
            df_activities = df_activities.sort_values('timestamp', ascending=False)
            
            # Display in a nice format
            for _, activity in df_activities.iterrows():
                timestamp = activity['timestamp'].strftime("%Y-%m-%d %H:%M:%S")
                activity_type = activity['activity_type'].replace('_', ' ').title()
                
                with st.expander(f"{activity_type} - {timestamp}"):
                    if activity.get('details'):
                        st.json(activity['details'])
                    else:
                        st.write("No additional details")
        else:
            st.info("No recent activity found.")
    
    def render_trading_stats(self):
        """Render trading statistics"""
        st.subheader("📊 Trading Statistics")
        
        # Mock statistics (replace with real data)
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            st.metric("Total Predictions", "47", "+3")
        
        with col2:
            st.metric("Accuracy Rate", "73.2%", "+2.1%")
        
        with col3:
            st.metric("Profit/Loss", "$1,247", "+$156")
        
        with col4:
            st.metric("Active Trades", "3", "-1")
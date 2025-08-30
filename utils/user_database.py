import json
import os
from datetime import datetime

class UserDatabase:
    def __init__(self):
        self.users_file = "data/users.json"
        self.activity_file = "data/user_activity.json"
        self.ensure_data_directory()
    
    def ensure_data_directory(self):
        """Create data directory if it doesn't exist"""
        os.makedirs("data", exist_ok=True)
        
        # Initialize files if they don't exist
        if not os.path.exists(self.users_file):
            self.save_json({}, self.users_file)
        
        if not os.path.exists(self.activity_file):
            self.save_json({}, self.activity_file)
    
    def load_json(self, filepath):
        """Load JSON data from file"""
        try:
            with open(filepath, 'r') as f:
                return json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            return {}
    
    def save_json(self, data, filepath):
        """Save JSON data to file"""
        with open(filepath, 'w') as f:
            json.dump(data, f, indent=2)
    
    def create_user(self, user_data):
        """Create new user account"""
        users = self.load_json(self.users_file)
        
        if user_data['username'] in users:
            return False  # User already exists
        
        users[user_data['username']] = user_data
        self.save_json(users, self.users_file)
        
        # Log registration
        self.log_user_activity(user_data['username'], "registration")
        return True
    
    def verify_user(self, username, password_hash):
        """Verify user credentials"""
        users = self.load_json(self.users_file)
        
        if username in users:
            return users[username]['password'] == password_hash
        return False
    
    def get_user_info(self, username):
        """Get user information"""
        users = self.load_json(self.users_file)
        return users.get(username, {})
    
    def log_user_activity(self, username, activity_type, details=None):
        """Log user activity"""
        activities = self.load_json(self.activity_file)
        
        if username not in activities:
            activities[username] = []
        
        activity_entry = {
            'timestamp': datetime.now().isoformat(),
            'activity_type': activity_type,
            'details': details or {}
        }
        
        activities[username].append(activity_entry)
        
        # Keep only last 100 activities per user
        activities[username] = activities[username][-100:]
        
        self.save_json(activities, self.activity_file)
    
    def get_user_activities(self, username, limit=50):
        """Get user activity history"""
        activities = self.load_json(self.activity_file)
        return activities.get(username, [])[-limit:]
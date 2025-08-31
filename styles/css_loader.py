import streamlit as st
import os

class StyleManager:
    def __init__(self):
        self.styles_dir = "styles"
        
    def load_css_file(self, filename):
        """Load CSS from external file"""
        css_path = os.path.join(self.styles_dir, filename)
        try:
            with open(css_path, 'r', encoding='utf-8') as f:
                css_content = f.read()
            return css_content
        except FileNotFoundError:
            # Fallback to inline CSS if file doesn't exist
            return self.get_fallback_css()
    
    def load_professional_theme(self):
        """Load professional theme styling"""
        css_content = self.load_css_file("professional_theme.css")
        st.markdown(f"<style>{css_content}</style>", unsafe_allow_html=True)
    
    def load_dark_theme(self):
        """Load dark theme styling"""
        css_content = self.load_css_file("dark_theme.css")
        st.markdown(f"<style>{css_content}</style>", unsafe_allow_html=True)
    
    def load_custom_components(self):
        """Load custom component styles"""
        css_content = self.load_css_file("components.css")
        st.markdown(f"<style>{css_content}</style>", unsafe_allow_html=True)
    
    def get_fallback_css(self):
        """Fallback CSS if external files aren't found"""
        return """
        .stApp {
            font-family: 'Inter', sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        }
        .main-header {
            font-size: 2.5rem;
            font-weight: bold;
            color: #1f77b4;
            text-align: center;
            margin-bottom: 2rem;
        }
        .prediction-box {
            background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
            color: white;
            padding: 1.5rem;
            border-radius: 15px;
            text-align: center;
            margin: 1rem 0;
        }
        """

def load_custom_css():
    """Main function to load all CSS styling"""
    style_manager = StyleManager()
    style_manager.load_professional_theme()
    style_manager.load_custom_components()
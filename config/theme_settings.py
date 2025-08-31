# Theme configuration
THEMES = {
    "professional": {
        "primary_color": "#2E86AB",
        "background_color": "#FFFFFF", 
        "secondary_background_color": "#F8FAFC",
        "text_color": "#1A202C"
    },
    "dark": {
        "primary_color": "#667eea",
        "background_color": "#1A202C",
        "secondary_background_color": "#2D3748", 
        "text_color": "#F7FAFC"
    },
    "trading": {
        "primary_color": "#06D6A0",
        "background_color": "#0D1421",
        "secondary_background_color": "#1A2332",
        "text_color": "#FFFFFF"
    }
}

# Component styling classes
CSS_CLASSES = {
    "card": "professional-card",
    "prediction": "prediction-box", 
    "metric": "metric-container",
    "button": "professional-button",
    "header": "main-header"
}

def get_theme_config(theme_name="professional"):
    """Get theme configuration"""
    return THEMES.get(theme_name, THEMES["professional"])

def apply_streamlit_theme(theme_name="professional"):
    """Apply theme to Streamlit config"""
    theme = get_theme_config(theme_name)
    
    return {
        "primaryColor": theme["primary_color"],
        "backgroundColor": theme["background_color"],
        "secondaryBackgroundColor": theme["secondary_background_color"],
        "textColor": theme["text_color"]
    }
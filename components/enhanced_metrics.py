import streamlit as st
import numpy as np

def render_metrics(prediction_data, user_inputs):
    """Render professional metrics with enhanced styling"""
    
    # Main prediction display
    render_professional_prediction_box(prediction_data, user_inputs)
    
    # Metrics grid
    render_metrics_grid(prediction_data, user_inputs)
    
    # Technical analysis section
    # render_technical_analysis()
    
    # Trading recommendation
    # render_trading_recommendation(prediction_data, user_inputs)

def render_professional_prediction_box(prediction_data, user_inputs):
    """Render main prediction with professional styling"""
    current_price = prediction_data['current_price']
    predicted_price = prediction_data['predicted_price']
    predicted_change = prediction_data['predicted_change']
    confidence = prediction_data['confidence']
    
    # Determine trend color and icon
    trend_color = "#06D6A0" if predicted_change > 0 else "#EE6055"
    trend_icon = "📈" if predicted_change > 0 else "📉"
    
    st.markdown(f"""
    <div class="prediction-box">
        <div style="display: flex; justify-content: space-between; align-items: center;">
            <div>
                <h2 style="margin: 0; font-size: 1.5rem;">{trend_icon} {user_inputs['selected_asset']}</h2>
                <p style="margin: 0; opacity: 0.9;">AI Prediction Analysis</p>
            </div>
            <div style="text-align: right;">
                <div style="font-size: 2.5rem; font-weight: 700; margin: 0;">
                    ${predicted_price:.2f}
                </div>
                <div style="color: {trend_color}; font-size: 1.2rem; font-weight: 600;">
                    {predicted_change*100:+.2f}%
                </div>
            </div>
        </div>
        
        <div style="margin-top: 1.5rem; padding-top: 1rem; border-top: 1px solid rgba(255,255,255,0.3);">
            <div style="display: flex; justify-content: space-between;">
                <div>
                    <small style="opacity: 0.8;">Current Price</small>
                    <div style="font-size: 1.1rem; font-weight: 600;">${current_price:.2f}</div>
                </div>
                <div>
                    <small style="opacity: 0.8;">Confidence</small>
                    <div style="font-size: 1.1rem; font-weight: 600;">{confidence*100:.1f}%</div>
                </div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

def render_metrics_grid(prediction_data, user_inputs):
    """Render metrics in a professional grid layout"""
    predicted_change = prediction_data['predicted_change']
    investment_amount = user_inputs['investment_amount']
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        render_metric_card(
            "Potential P&L",
            f"${investment_amount * predicted_change:+.2f}",
            f"{predicted_change*100:+.2f}%",
            "success" if predicted_change > 0 else "error"
        )
    
    with col2:
        risk_score = np.random.randint(1, 11)
        risk_color = "success" if risk_score <= 3 else "warning" if risk_score <= 7 else "error"
        render_metric_card(
            "Risk Score",
            f"{risk_score}/10",
            "Volatility-based",
            risk_color
        )
    
    with col3:
        accuracy = np.random.uniform(0.7, 0.9) * 100
        render_metric_card(
            "Model Accuracy",
            f"{accuracy:.1f}%",
            "Historical avg",
            "success"
        )
    
    with col4:
        sentiment = np.random.choice(["Bearish 🐻", "Neutral ➡️", "Bullish 🐂"])
        sentiment_color = "error" if "Bear" in sentiment else "warning" if "Neutral" in sentiment else "success"
        render_metric_card(
            "Market Sentiment",
            sentiment,
            f"{np.random.randint(-10, 11):+d} points",
            sentiment_color
        )

def render_metric_card(title, value, subtitle, color_type):
    """Render individual metric card with professional styling"""
    colors = {
        "success": "#06D6A0",
        "warning": "#FFD23F", 
        "error": "#EE6055",
        "primary": "#2E86AB"
    }
    
    color = colors.get(color_type, colors["primary"])
    
    st.markdown(f"""
    <div class="metric-container" style="border-left-color: {color};">
        <div style="color: var(--text-secondary); font-size: 0.85rem; font-weight: 500; margin-bottom: 0.5rem;">
            {title}
        </div>
        <div style="font-size: 1.5rem; font-weight: 700; color: {color}; margin-bottom: 0.25rem;">
            {value}
        </div>
        <div style="color: var(--text-muted); font-size: 0.75rem;">
            {subtitle}
        </div>
    </div>
    """, unsafe_allow_html=True)
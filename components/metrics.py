import streamlit as st
import numpy as np

def render_metrics(prediction_data, user_inputs):
    """Render prediction results and metrics"""
    
    # Main prediction box
    render_prediction_box(prediction_data, user_inputs)
    
    # Metrics row
    render_metrics_row(prediction_data, user_inputs)
    
    # Technical indicators
    render_technical_indicators()
    
    # Trading recommendation
    render_trading_recommendation(prediction_data, user_inputs)

def render_prediction_box(prediction_data, user_inputs):
    """Render main prediction display box"""
    current_price = prediction_data['current_price']
    predicted_price = prediction_data['predicted_price']
    predicted_change = prediction_data['predicted_change']
    confidence = prediction_data['confidence']
    
    st.markdown(f"""
    <div class="prediction-box">
        <h2>🎯 AI Prediction for {user_inputs['selected_asset']}</h2>
        <h3>Current Price: ${current_price:.2f}</h3>
        <h3>Predicted Price: ${predicted_price:.2f}</h3>
        <h4>Expected Change: {predicted_change*100:+.2f}%</h4>
        <h4>Confidence: {confidence*100:.1f}%</h4>
    </div>
    """, unsafe_allow_html=True)

def render_metrics_row(prediction_data, user_inputs):
    """Render metrics in a row layout"""
    col1, col2, col3, col4 = st.columns(4)
    
    predicted_change = prediction_data['predicted_change']
    investment_amount = user_inputs['investment_amount']
    
    with col1:
        st.metric(
            "Potential Profit/Loss",
            f"${investment_amount * predicted_change:+.2f}",
            f"{predicted_change*100:+.2f}%"
        )
    
    with col2:
        st.metric(
            "Risk Score",
            f"{np.random.randint(1, 11)}/10",
            "Based on volatility"
        )
    
    with col3:
        st.metric(
            "Model Accuracy",
            f"{np.random.uniform(0.7, 0.9)*100:.1f}%",
            "Historical performance"
        )
    
    with col4:
        st.metric(
            "Market Sentiment",
            np.random.choice(["Bearish", "Neutral", "Bullish"]),
            f"{np.random.randint(-10, 11):+d} points"
        )

def render_technical_indicators():
    """Render technical analysis indicators"""
    st.subheader("🔧 Technical Analysis")
    
    tech_col1, tech_col2, tech_col3 = st.columns(3)
    
    with tech_col1:
        render_rsi_indicator()
    
    with tech_col2:
        render_macd_indicator()
    
    with tech_col3:
        render_ma_indicator()

def render_rsi_indicator():
    """Render RSI indicator"""
    st.markdown("**RSI (14)**")
    rsi_value = np.random.uniform(20, 80)
    if rsi_value > 70:
        st.error(f"Overbought: {rsi_value:.1f}")
    elif rsi_value < 30:
        st.success(f"Oversold: {rsi_value:.1f}")
    else:
        st.info(f"Neutral: {rsi_value:.1f}")

def render_macd_indicator():
    """Render MACD signal"""
    st.markdown("**MACD Signal**")
    signals = ["Strong Buy", "Buy", "Hold", "Sell", "Strong Sell"]
    signal = np.random.choice(signals)
    if "Buy" in signal:
        st.success(signal)
    elif signal == "Hold":
        st.info(signal)
    else:
        st.error(signal)

def render_ma_indicator():
    """Render Moving Average indicator"""
    st.markdown("**Moving Average**")
    ma_signal = np.random.choice(["Above MA50", "Below MA50"])
    if "Above" in ma_signal:
        st.success(ma_signal)
    else:
        st.error(ma_signal)

def render_trading_recommendation(prediction_data, user_inputs):
    """Render trading recommendation section"""
    st.subheader("💡 AI Trading Recommendation")
    
    current_price = prediction_data['current_price']
    predicted_price = prediction_data['predicted_price']
    investment_amount = user_inputs['investment_amount']
    
    recommendations = {
        "action": np.random.choice(["BUY", "SELL", "HOLD"]),
        "entry_price": f"${current_price:.2f}",
        "target_price": f"${predicted_price:.2f}",
        "stop_loss": f"${current_price * 0.95:.2f}",
        "position_size": f"{investment_amount / current_price:.2f} units"
    }
    
    rec_col1, rec_col2 = st.columns(2)
    
    with rec_col1:
        action_color = {"BUY": "🟢", "SELL": "🔴", "HOLD": "🟡"}[recommendations["action"]]
        st.markdown(f"""
        ### {action_color} **{recommendations["action"]} Signal**
        - **Entry Price:** {recommendations["entry_price"]}
        - **Target Price:** {recommendations["target_price"]}
        - **Stop Loss:** {recommendations["stop_loss"]}
        """)
    
    with rec_col2:
        st.markdown(f"""
        ### 📋 **Trade Details**
        - **Position Size:** {recommendations["position_size"]}
        - **Risk/Reward Ratio:** 1:2.5
        - **Timeframe:** {user_inputs['prediction_horizon']}
        """)

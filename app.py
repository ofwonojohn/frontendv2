import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import plotly.express as px
from datetime import datetime, timedelta
import time

# Configure page
st.set_page_config(
    page_title="AI Trading Predictor",
    page_icon="📈",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
st.markdown("""
<style>
    .main-header {
        font-size: 2.5rem;
        font-weight: bold;
        color: #1f77b4;
        text-align: center;
        margin-bottom: 2rem;
    }
    .metric-card {
        background-color: #f0f2f6;
        padding: 1rem;
        border-radius: 10px;
        border-left: 5px solid #1f77b4;
    }
    .prediction-box {
        background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
        color: white;
        padding: 1.5rem;
        border-radius: 15px;
        text-align: center;
        margin: 1rem 0;
    }
</style>
""", unsafe_allow_html=True)

# Header
st.markdown('<h1 class="main-header">🤖 AI Trading Prediction System</h1>', unsafe_allow_html=True)

# Sidebar for inputs
st.sidebar.header("📊 Trading Parameters")

# Market selection
market_type = st.sidebar.selectbox(
    "Select Market Type",
    ["Forex", "Stocks", "Crypto", "Commodities", "Indices"]
)

# Asset selection based on market type
asset_options = {
    "Forex": ["EUR/USD", "GBP/USD", "USD/JPY", "AUD/USD", "USD/CHF"],
    "Stocks": ["AAPL", "GOOGL", "MSFT", "AMZN", "TSLA"],
    "Crypto": ["BTC/USD", "ETH/USD", "ADA/USD", "SOL/USD", "DOT/USD"],
    "Commodities": ["Gold", "Silver", "Oil", "Natural Gas", "Wheat"],
    "Indices": ["S&P 500", "NASDAQ", "DOW", "FTSE 100", "DAX"]
}

selected_asset = st.sidebar.selectbox(
    f"Select {market_type} Asset",
    asset_options[market_type]
)

# Time parameters
prediction_horizon = st.sidebar.selectbox(
    "Prediction Horizon",
    ["1 Hour", "4 Hours", "1 Day", "1 Week", "1 Month"]
)

investment_amount = st.sidebar.number_input(
    "Investment Amount ($)",
    min_value=100,
    max_value=100000,
    value=1000,
    step=100
)

# Risk tolerance
risk_level = st.sidebar.select_slider(
    "Risk Tolerance",
    options=["Very Low", "Low", "Medium", "High", "Very High"],
    value="Medium"
)

# AI Model selection
model_type = st.sidebar.selectbox(
    "AI Model",
    ["LSTM Neural Network", "Random Forest", "XGBoost", "Ensemble Model"]
)

# Main content area
col1, col2, col3 = st.columns([1, 2, 1])

with col2:
    if st.button("🔮 Generate Prediction", type="primary", use_container_width=True):
        # Simulate AI processing
        progress_bar = st.progress(0)
        status_text = st.empty()
        
        for i in range(100):
            progress_bar.progress(i + 1)
            if i < 30:
                status_text.text("Collecting market data...")
            elif i < 60:
                status_text.text("Running AI analysis...")
            elif i < 90:
                status_text.text("Calculating predictions...")
            else:
                status_text.text("Finalizing results...")
            time.sleep(0.02)
        
        status_text.empty()
        progress_bar.empty()

# Generate mock prediction data
if 'prediction_generated' not in st.session_state:
    st.session_state.prediction_generated = False

if st.session_state.get('prediction_generated', False) or st.sidebar.button("Show Sample Results"):
    st.session_state.prediction_generated = True
    
    # Mock prediction results
    np.random.seed(42)
    current_price = np.random.uniform(50, 200)
    predicted_change = np.random.uniform(-0.05, 0.05)
    predicted_price = current_price * (1 + predicted_change)
    confidence = np.random.uniform(0.65, 0.95)
    
    # Prediction display
    st.markdown(f"""
    <div class="prediction-box">
        <h2>🎯 AI Prediction for {selected_asset}</h2>
        <h3>Current Price: ${current_price:.2f}</h3>
        <h3>Predicted Price: ${predicted_price:.2f}</h3>
        <h4>Expected Change: {predicted_change*100:+.2f}%</h4>
        <h4>Confidence: {confidence*100:.1f}%</h4>
    </div>
    """, unsafe_allow_html=True)
    
    # Metrics row
    col1, col2, col3, col4 = st.columns(4)
    
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
            ["Bearish", "Neutral", "Bullish"][np.random.randint(0, 3)],
            f"{np.random.randint(-10, 11):+d} points"
        )
    
    # Charts section
    st.subheader("📈 Price Analysis & Predictions")
    
    chart_col1, chart_col2 = st.columns(2)
    
    with chart_col1:
        # Historical price chart with prediction
        dates = pd.date_range(start=datetime.now() - timedelta(days=30), end=datetime.now() + timedelta(days=7), freq='D')
        historical_prices = current_price + np.cumsum(np.random.randn(len(dates)) * 2)
        
        # Add prediction point
        historical_prices[-7:] = np.linspace(historical_prices[-8], predicted_price, 7)
        
        fig = go.Figure()
        
        # Historical data
        fig.add_trace(go.Scatter(
            x=dates[:-7],
            y=historical_prices[:-7],
            mode='lines',
            name='Historical Price',
            line=dict(color='blue', width=2)
        ))
        
        # Prediction
        fig.add_trace(go.Scatter(
            x=dates[-8:],
            y=historical_prices[-8:],
            mode='lines',
            name='AI Prediction',
            line=dict(color='red', width=3, dash='dash')
        ))
        
        fig.update_layout(
            title=f"{selected_asset} Price Trend & Prediction",
            xaxis_title="Date",
            yaxis_title="Price ($)",
            height=400
        )
        
        st.plotly_chart(fig, use_container_width=True)
    
    with chart_col2:
        # Confidence intervals
        confidence_data = {
            'Scenario': ['Best Case', 'Most Likely', 'Worst Case'],
            'Price': [predicted_price * 1.1, predicted_price, predicted_price * 0.9],
            'Probability': [0.2, 0.6, 0.2]
        }
        
        fig2 = px.bar(
            confidence_data,
            x='Scenario',
            y='Price',
            color='Probability',
            title="Price Scenarios & Probabilities",
            color_continuous_scale='RdYlGn'
        )
        
        fig2.update_layout(height=400)
        st.plotly_chart(fig2, use_container_width=True)
    
    # Technical indicators
    st.subheader("🔧 Technical Analysis")
    
    tech_col1, tech_col2, tech_col3 = st.columns(3)
    
    with tech_col1:
        st.markdown("**RSI (14)**")
        rsi_value = np.random.uniform(20, 80)
        if rsi_value > 70:
            st.error(f"Overbought: {rsi_value:.1f}")
        elif rsi_value < 30:
            st.success(f"Oversold: {rsi_value:.1f}")
        else:
            st.info(f"Neutral: {rsi_value:.1f}")
    
    with tech_col2:
        st.markdown("**MACD Signal**")
        signals = ["Strong Buy", "Buy", "Hold", "Sell", "Strong Sell"]
        signal = np.random.choice(signals)
        if "Buy" in signal:
            st.success(signal)
        elif signal == "Hold":
            st.info(signal)
        else:
            st.error(signal)
    
    with tech_col3:
        st.markdown("**Moving Average**")
        ma_signal = np.random.choice(["Above MA50", "Below MA50"])
        if "Above" in ma_signal:
            st.success(ma_signal)
        else:
            st.error(ma_signal)
    
    # Trading recommendation
    st.subheader("💡 AI Trading Recommendation")
    
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
        - **Timeframe:** {prediction_horizon}
        """)

# Footer
st.markdown("---")
st.markdown("⚠️ **Disclaimer**: This is a demo AI trading system. Always consult with financial advisors before making investment decisions.")

# Additional features in sidebar
st.sidebar.markdown("---")
st.sidebar.markdown("### 🛠️ Additional Features")

if st.sidebar.button("📊 Market Overview"):
    st.sidebar.info("Market overview feature coming soon!")

if st.sidebar.button("📈 Backtesting"):
    st.sidebar.info("Backtesting module in development!")

if st.sidebar.button("⚙️ Model Settings"):
    st.sidebar.info("Advanced settings panel coming soon!")
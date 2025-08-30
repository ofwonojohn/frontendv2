import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
import numpy as np
from datetime import datetime, timedelta

def render_charts(prediction_data, user_inputs):
    """Render all charts and visualizations"""
    st.subheader("📈 Price Analysis & Predictions")
    
    chart_col1, chart_col2 = st.columns(2)
    
    with chart_col1:
        render_price_chart(prediction_data, user_inputs)
    
    with chart_col2:
        render_scenario_chart(prediction_data)

def render_price_chart(prediction_data, user_inputs):
    """Render historical price and prediction chart"""
    dates = pd.date_range(
        start=datetime.now() - timedelta(days=30), 
        end=datetime.now() + timedelta(days=7), 
        freq='D'
    )
    
    current_price = prediction_data['current_price']
    predicted_price = prediction_data['predicted_price']
    
    # Generate mock historical data
    historical_prices = current_price + np.cumsum(np.random.randn(len(dates)) * 2)
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
        title=f"{user_inputs['selected_asset']} Price Trend & Prediction",
        xaxis_title="Date",
        yaxis_title="Price ($)",
        height=400
    )
    
    st.plotly_chart(fig, use_container_width=True)

def render_scenario_chart(prediction_data):
    """Render scenario analysis chart"""
    predicted_price = prediction_data['predicted_price']
    
    confidence_data = {
        'Scenario': ['Best Case', 'Most Likely', 'Worst Case'],
        'Price': [predicted_price * 1.1, predicted_price, predicted_price * 0.9],
        'Probability': [0.2, 0.6, 0.2]
    }
    
    fig = px.bar(
        confidence_data,
        x='Scenario',
        y='Price',
        color='Probability',
        title="Price Scenarios & Probabilities",
        color_continuous_scale='RdYlGn'
    )
    
    fig.update_layout(height=400)
    st.plotly_chart(fig, use_container_width=True)
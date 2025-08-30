import pandas as pd
import numpy as np
from datetime import datetime, timedelta

def generate_mock_data(days=30, base_price=100):
    """Generate mock historical price data"""
    dates = pd.date_range(start=datetime.now() - timedelta(days=days), periods=days, freq='D')
    prices = base_price + np.cumsum(np.random.randn(days) * 2)
    return pd.DataFrame({'date': dates, 'price': prices})

def calculate_technical_indicators(prices):
    """Calculate basic technical indicators"""
    df = pd.DataFrame(prices)
    
    # Simple moving average
    df['sma_20'] = df['price'].rolling(window=20).mean()
    df['sma_50'] = df['price'].rolling(window=50).mean()
    
    # RSI calculation (simplified)
    delta = df['price'].diff()
    gain = delta.where(delta > 0, 0)
    loss = -delta.where(delta < 0, 0)
    avg_gain = gain.rolling(window=14).mean()
    avg_loss = loss.rolling(window=14).mean()
    rs = avg_gain / avg_loss
    df['rsi'] = 100 - (100 / (1 + rs))
    
    return df

def format_currency(amount):
    """Format currency with proper symbols"""
    return f"${amount:,.2f}"

def calculate_risk_metrics(predicted_change, investment_amount):
    """Calculate risk-related metrics"""
    potential_loss = abs(min(0, predicted_change * investment_amount))
    potential_gain = max(0, predicted_change * investment_amount)
    
    return {
        'potential_loss': potential_loss,
        'potential_gain': potential_gain,
        'risk_reward_ratio': potential_gain / max(potential_loss, 1)
    }
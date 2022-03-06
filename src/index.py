import numpy as np
import pandas as pd
import yfinance as yf
import plotly.graph_objs as go

user_crypto_currency = input('Enter the currency code of the cryptocurrency: ')
user_currency = input('Enter the ISO code of your currency: ')
user_tickers = user_crypto_currency.upper() + '-' + user_currency.upper()

data = yf.download(tickers='BTC-USD', period='3mo', interval='1d')
print(data)

data['MA5'] = data['Close'].rolling(5).mean()
data['MA20'] = data['Close'].rolling(20).mean()

fig = go.Figure()

fig.add_trace(go.Candlestick(x=data.index, open=data['Open'], high=data['High'], low=data['Low'], close=data['Close'], name = 'Market data'))

fig.add_trace(go.Scatter(x=data.index, y=data['MA20'], line=dict(color='black', width = 1.5), name='Death Line'))
fig.add_trace(go.Scatter(x=data.index, y=data['MA5'], line=dict(color='orange', width=1.5), name='Gold Line'))

fig.show()

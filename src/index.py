import numpy as np
import pandas as pd
import yfinance as yf
import plotly.graph_objs as go

data = yf.download(tickers='BTC-USD', period='3mo', interval='1d')
print(data)

data['MA5'] = data['Close'].rolling(5).mean()
data['MA20'] = data['Close'].rolling(20).mean()

fig = go.Figure()

fig.add_trace(go.Candlestick(x=data.index, open=data['Open'], high=data['High'], low=data['Low'], close=data['Close'], name = 'market data'))

fig.show()

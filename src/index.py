import numpy as np
import pandas as pd
import yfinance as yf
import plotly.graph_objs as go

user_crypto_currency = input('Enter the currency code of the cryptocurrency: ')
user_currency = input('Enter the ISO code of your currency: ')
user_tickers = user_crypto_currency.upper() + '-' + user_currency.upper()

user_period = input('Enter the number for the period of the chart (m/h/d/mo/y): ')

valid_intervals = ['1m', '2m', '5m', '15m', '30m', '60m', '90m', '1h', '1d', '5d', '1wk', '1mo', '3mo']

for i in range(0, len(valid_intervals)):
    print(str(i + 1) + ': ' + str(str({valid_intervals[i]}).removeprefix("{'").removesuffix("'}")))

user_interval = int(input('Enter corresponding number to the wanted interval: '))

data = yf.download(tickers=user_tickers, period=user_period, interval=valid_intervals[user_interval - 1])
print(data)

data['MA5'] = data['Close'].rolling(5).mean()
data['MA20'] = data['Close'].rolling(20).mean()

fig = go.Figure()

fig.add_trace(go.Candlestick(x=data.index, open=data['Open'], high=data['High'], low=data['Low'], close=data['Close'], name = 'Market data'))

fig.add_trace(go.Scatter(x=data.index, y=data['MA20'], line=dict(color='black', width = 1.5), name='Death Line'))
fig.add_trace(go.Scatter(x=data.index, y=data['MA5'], line=dict(color='orange', width=1.5), name='Gold Line'))

fig.show()

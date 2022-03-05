import numpy as np
import pandas as pd
import yfinance as yf
import plotly.graph_objs as go

data = yf.download(tickers='BTC-USD', period='3mo', interval='1d')
print(data)

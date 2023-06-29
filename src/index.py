
# Import of the modules

import yfinance as yf
import plotly.graph_objs as go
import plotly.io as pio
import time
from selenium import webdriver
import os
from random import randint
from asciimatics.screen import Screen
from asciimatics.effects import Cycle, Stars
from asciimatics.renderers import FigletText
from asciimatics.scene import Scene
from asciimatics.screen import Screen

# Startup Animation

def demo(screen):
    effects = [
        Cycle(
            screen,
            FigletText("Gate to", font='small'),
            int(screen.height / 2 - 8)),
        Cycle(
            screen,
            FigletText("HEAVEN", font='big'),
            int(screen.height / 2 + 3)),
        Stars(screen, 200)
    ]
    screen.play([Scene(effects, 500)])
    ev = screen.get_key()
    if ev in (ord('Q'), ord('q')):
         return
    screen.refresh()
Screen.wrapper(demo)

# Main code of the Bot

x = 0

clear = lambda: os.system('cls')
clear()

user_crypto_currency = input('Enter the currency code of the cryptocurrency: ')
user_currency = input('Enter the ISO code of your currency: ')
user_tickers = user_crypto_currency.upper() + '-' + user_currency.upper()

user_period = input('Enter the number for the period of the chart (m/h/d/mo/y): ')

valid_intervals = ['1m', '2m', '5m', '15m', '30m', '60m', '90m', '1h', '1d', '5d', '1wk', '1mo', '3mo']

for i in range(0, len(valid_intervals)):
    print(str(i + 1) + ': ' + str(str({valid_intervals[i]}).removeprefix("{'").removesuffix("'}")))

user_interval = int(input('Enter corresponding number to the wanted interval: '))

data_refresh = int(input('In what time intervall should the bot refresh the data (seconds): '))

# Chromedriver creation

driver = webdriver.Chrome()

# Loop of recreating and refreshing the data

while True:

    # Data download from yahoo

    data = yf.download(tickers=user_tickers, period=user_period, interval=valid_intervals[user_interval - 1])
    print(data)

    # Creating the chart
   
    data['MA5'] = data['Close'].rolling(5).mean()
    data['MA20'] = data['Close'].rolling(20).mean()

    fig = go.Figure()
    fig.add_trace(go.Candlestick(x=data.index, open=data['Open'], high=data['High'], low=data['Low'], close=data['Close'], name='Market Data'))
    fig.add_trace(go.Scatter(x=data.index, y=data['MA20'], line=dict(color='black', width=1.5), name='Death Line'))
    fig.add_trace(go.Scatter(x=data.index, y=data['MA5'], line=dict(color='orange', width=1.5), name='Gold Line'))

    cross_points_green = []
    for i in range(1, len(data)):
        if (data['MA5'][i-1] < data['MA20'][i-1]) and (data['MA5'][i] >= data['MA20'][i]):
                cross_points_green.append(data.index[i])

    cross_points_red = []
    for i in range(1, len(data)):
        if (data['MA5'][i-1] > data['MA20'][i-1]) and (data['MA5'][i] <= data['MA20'][i]):
                cross_points_red.append(data.index[i])
   
    # Ad the markers to the chart
    fig.add_trace(go.Scatter(x=cross_points_green, y=data.loc[cross_points_green, 'Close'], mode='markers', marker=dict(color='green'), name='Buy'))
    fig.add_trace(go.Scatter(x=cross_points_red, y=data.loc[cross_points_red, 'Close'], mode='markers', marker=dict(color='red'), name='Sell'))
   

    # Saving the chart as html

    plot_file = f"plot.html"
    fig.write_html(plot_file)

    # Opening the chart

    if x == 0:
        driver.get(f"file:///C:/Users/valen/Desktop/crypto-prediction-master/{plot_file}")
        x = x +1
    else:
        driver.execute_script(f"window.location.href = 'file:///C:/Users/valen/Desktop/crypto-prediction-master/{plot_file}';")

    time.sleep(data_refresh)

    # Deleting the html file

    os.remove(plot_file)

driver.quit()

# Cryptocurrency Prediction Help

#### A cryptocurrency bot which can help you predict future crypto prices through comparing previous crypto prices with actual prices. The bot used the method of Death Cross vs Golden Cross, a reliable method for solid predictions of prices, to make plot previously predicted data.

---
<img src = "/screenshots/graph.png">

###### *Image: Preview of the graph*

## Features

- Interactive graph

- Allows user to input to customize the following in the chart - currency, cryptocurrency, time period and time interval

-  Various built-in chart functions such as zooming and downloading the plotted graph, thanks to plotly <!--Link to libraries used in same file ^ -->

- Data is viewable for every candlestick in the data chart

- Along with the graph, a table is also rendered to output important data

###### *Head to [project screenshots](/screenshots) to check out the mentioned features!*

## How it works

- The program receives data of the chosen cryptocurrency from Yahoo finance from which it creates a chart based on the original prices of the cryptocurrency. 
- Moving average of 5 days (MA₅) is taken and then plotted in the graph as the 'Gold Line', where 

```
MA₅ = (MA₁ + MA₂ + MA₃ + MA₄ + MA₅) / 5
```
- Another moving average, this time for 20 days (MA₂₀), is plotted in the graph as the 'Death Line', where

```
MA₂₀ = (MA₁ + MA₂ + MA₃ + MA₄ ... MA₂₀) / 5
```

- The graph helps detecting bullish and bearish trends, ie. helps when you should buy or sell. It is explained in the following points.
- The graph tries to catch a global trend, over which a short-term 'Gold Line' and a long-term 'Black Line' is plotted
- The Gold Line will always be more accurate with the prices as it is a short-term moving average compared to the Death Line
- Two situations will always be visible in the graph - Death Line being higher than the Gold Line and vice-versa; both these situations will help us make decisions for either buying or selling
- When the Death line crosses the Gold line and gets higher than the latter in the graph, it indicates a bearish moving average in the future market. This time is the perfect for selling.

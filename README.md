# Cryptocurrency Prediction Help

#### A cryptocurrency bot which can help you predict future crypto prices through comparing previous crypto prices with actual prices. The bot used the method of Death Cross vs Golden Cross, a reliable method for solid predictions of prices, to make plot previously predicted data.

---
<img src = "/screenshots/graph.png">

###### *Image: Preview of the graph*

---

## Features

- Interactive graph

- Allows user to input to customize the following in the chart - currency, cryptocurrency, time period and time interval

-  Various built-in chart functions such as zooming and downloading the plotted graph, thanks to [plotly](https://plotly.com/python/getting-started/#:~:text=The%20plotly%20Python%20library%20is,3%2Ddimensional%20use%2Dcases.)

- Data is viewable for every candlestick in the data chart

- Along with the graph, a table is also rendered to output important data

###### *Head to [project screenshots](/screenshots) to check out the mentioned features!*

---

## How It Works - The Gold Line vs Death Line Algorithm

- The program receives data of the chosen cryptocurrency from Yahoo finance from which it creates a chart based on the original prices of the cryptocurrency. 
- Moving average of 5 days (MA₅) is taken and then plotted in the graph as the 'Gold Line', where 

```
MA₅ = (MA₁ + MA₂ + MA₃ + MA₄ + MA₅) / 5
```
- Another moving average, this time for 20 days (MA₂₀), is plotted in the graph as the 'Death Line', where

```
MA₂₀ = (MA₁ + MA₂ + MA₃ + MA₄ ... MA₂₀) / 20
```

- The graph helps detecting bullish and bearish trends, ie. helps when you should buy or sell. It is explained in the following points.

- The graph tries to catch a global trend, over which a short-term 'Gold Line' and a long-term 'Black Line' is plotted

- The Gold Line will always be more accurate with the prices as it is a short-term moving average compared to the Death Line

- Two situations will always be visible in the graph - Death Line being higher than the Gold Line and vice-versa; both these situations will help us make decisions for either buying or selling

- When the Death line crosses the Gold line and gets higher in the graph, it indicates a bearish moving average in the future market. This situation is known as the Death Cross and it is the perfect time for selling
 
 <img src = /screenshots/charts/selling_point.png>

- When the Gold line crosses the Death line and gets higher in the graph, it indicates a bullish moving average in the future market. This situation is known as the Golden Cross and it is the perfect time for buying

<img src = /screenshots/charts/buying_point.png>

###### *Read more about Death Cross and Golden Cross [here](https://academy.binance.com/en/articles/golden-cross-and-death-cross-explained)*

---

## Resources

#### Here is a list of resources which helped me, both - the libraries I used and the sources which helped me for the understanding of the algorithm

> Libraries used
> - [Yahoo! Finance](https://pypi.org/project/yfinance/)
> - [Plotly](https://plotly.com/python/getting-started/#:~:text=The%20plotly%20Python%20library%20is,3%2Ddimensional%20use%2Dcases.)

> Sources for understanding algorithm
> - [Binance - Golden Cross and Death Cross Explained](https://academy.binance.com/en/articles/golden-cross-and-death-cross-explained)
> - [YouTube - Golden Cross Explained: Why most traders get it wrong (and how it really works)](https://www.youtube.com/watch?v=6mckJdktXkc)
> - [YouTube - 15 min Crypto Trading Strategy Golden Cross Tested 100 times](https://www.youtube.com/watch?v=Iw5sHVlSzaE)

I would like to thank for the availibilty of these resources as the project would not have been in existence without them!

---

## Contributing

Contributions are always welcome!

See <a href = "CONTRIBUTING.md">`CONTRIBUTING.md`</a> for ways to get started.

Please adhere to this project's <a href = "CODE_OF_CONDUCT.md">`CODE OF CONDUCT`</a>.

---

## License

[MIT](LICENSE)  

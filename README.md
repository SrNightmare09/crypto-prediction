# Cryptocurrency Prediction Assistance

#### A cryptocurrency bot which can assist you in predicting future crypto prices through comparing previous crypto prices with actual prices. The bot uses the method of Death Cross vs Golden Cross, a reliable method for solid predictions of prices, to make a plot based on previously predicted data.

---
<img src = "/screenshots/graph.png">

###### *Image: Preview of the graph*

---

<br>

## Table of Contents

- [Features](https://github.com/SrNightmare09/crypto-prediction#features)
- [Installation](https://github.com/SrNightmare09/crypto-prediction#installation)
- [How It Works - The Gold Line vs Death Line Algorithm](https://github.com/SrNightmare09/crypto-prediction#how-it-works---the-gold-line-vs-death-line-algorithm)
- [Resources](https://github.com/SrNightmare09/crypto-prediction#resources)
- [Upcoming Features](https://github.com/SrNightmare09/crypto-prediction#upcoming-features)
- [Contributing](https://github.com/SrNightmare09/crypto-prediction#contributing)
- [MIT License](https://github.com/SrNightmare09/crypto-prediction#license)

---

<br>

## Features

- Interactive graph

- Allows user to input to customize the following in the chart - currency, cryptocurrency, time period and time interval

-  Various built-in chart functions such as zooming and downloading the plotted graph, thanks to [plotly](https://plotly.com/python/getting-started/#:~:text=The%20plotly%20Python%20library%20is,3%2Ddimensional%20use%2Dcases.)

- Data is viewable for every candlestick in the data chart

- Along with the graph, a table is also rendered to output important data

###### *Head to [project screenshots](/screenshots) to check out the mentioned features!*

---

<br>

## Installation

- Clone the repository by running the following command

```
git clone https://github.com/SrNightmare09/crypto-prediction.git
```

- Run the following commands to install the required libraries for the code - 

```
pip install yfinance
```

```
pip install plotly
```

- Run `index.py` from the `src` folder. On doing this, A few questions will be asked in your terminal related to the plotting, please give valid input for proper functioning of the graph.

- When all input values have been received, your terminal will print a table with statistics, along with a plotted graph also being rendered.
 
- And, we're done! But that's not it, feel free to edit the code as you wish, add features and feel free to send a pull request. Read about contributing [here](CONTRIBUTING.md)

###### *Note: Currently the project can only be run through raw cloning of the code and running it*

---

<br>

<details>
 <summary>How It Works</summary>

## How It Works - The Gold Line vs Death Line Algorithm

- The program receives data of the chosen cryptocurrency from Yahoo! finance, from which it creates a chart based on the original prices of the cryptocurrency. 

- The moving average of 5 days (MA₅) is taken and then plotted in the graph as the 'Gold Line', where 

```
MA₅ = (MA₁ + MA₂ + MA₃ + MA₄ + MA₅) / 5
```

- Another moving average, this time for 20 days (MA₂₀), is plotted in the graph as the 'Death Line', where

```
MA₂₀ = (MA₁ + MA₂ + MA₃ + MA₄ ... MA₂₀) / 20
```

- The graph helps detecting bullish and bearish trends, i.e., helps determine when you should buy or sell. It is explained in the following points.

- The graph tries to catch a global trend, over which a short-term 'Gold Line' and a long-term 'Black Line' is plotted

- The Gold Line will always be more accurate with the prices as it is a short-term moving average compared to the Death Line, which is a long-term moving average

- Two situations will always be visible in the graph - Death Line being higher than the Gold Line and vice-versa; both these situations will help us make decisions for either buying or selling

- When the Death line crosses the Gold line and gets higher in the graph, it indicates a bearish moving average in the future market. This situation is known as the Death Cross and it is the perfect time for selling
 
 <img src = /screenshots/charts/selling_point.png>

- When the Gold line crosses the Death line and gets higher in the graph, it indicates a bullish moving average in the future market. This situation is known as the Golden Cross and it is the perfect time for buying

<img src = /screenshots/charts/buying_point.png>

###### *Read more about Death Cross and Golden Cross [here](https://academy.binance.com/en/articles/golden-cross-and-death-cross-explained)*

---

</details>

<br>

<details>
    <summary>Resources</summary>

## Resources

#### Here is a list of resources which helped me, both - the libraries I used and the sources which helped me for the understanding of the algorithm

> Libraries used
> - [Yahoo! Finance](https://pypi.org/project/yfinance/)
> - [Plotly](https://plotly.com/python/getting-started/#:~:text=The%20plotly%20Python%20library%20is,3%2Ddimensional%20use%2Dcases.)

> Sources for understanding the algorithm
> - [Binance - Golden Cross and Death Cross Explained](https://academy.binance.com/en/articles/golden-cross-and-death-cross-explained)
> - [YouTube - Golden Cross Explained: Why most traders get it wrong (and how it really works)](https://www.youtube.com/watch?v=6mckJdktXkc)
> - [YouTube - 15 min Crypto Trading Strategy Golden Cross Tested 100 times](https://www.youtube.com/watch?v=Iw5sHVlSzaE)

I would like to thank for the availibility of these resources as the project would not have been in existence without them!

</details>

---

<br>

## Upcoming Features

#### A list of a few features which I will add in the later versions of the project - 

- [ ] Error handling for user input
- [ ] Viewing table alongside graph instead of in the terminal
- [ ] Future price predictions
- [ ] Response of code for predicting price by taking real-life events into consideration as well
- [ ] Implement code into a downloadable and useable application
- [ ] Add more graph tools (like drawing tools)
- [ ] Implement shortcuts for graph tools
- [ ] Add dark mode/light mode toggle

---

<br>

## Contributing

Contributions are always welcome! Feel free to fork this project, report issues/bugs, etc.

See <a href = "CONTRIBUTING.md">`CONTRIBUTING.md`</a> for ways to get started.

Please adhere to this project's <a href = "CODE_OF_CONDUCT.md">`CODE OF CONDUCT`</a>.

---

<br>

## License

[MIT](LICENSE)  

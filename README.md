# Stock Market Forecast

#### Heroku App - https://evening-dusk-74419.herokuapp.com/

#### -- Project Status: Active

## Project Intro/Objective

The purpose of this project is to gain familiarty with the application of deep learning in a finance domain, specifically in stock market forecasting. The reason for utilizing neural networks is so that we can the capture complex and non-linear trends that traditional ARIMA models fail to. 

### Methods Used
* Single Layer LSTM
* Stacked LSTM
* Bidirectional LSTM
* Data Visualization 

### Technologies
* Python
* Pandas
* Numpy
* Plotly
* Dash
* Postgres
* Heroku

## Project Description

In this project, we use S&P 500 historical data collected from Yahoo Finance. The models are trained on opening prices from December 27th 1950 to December 24th 2020 and then used to make two predictions: a next day prediction and a 5-day prediction (opening price of index 5 days later). Finally, a simple app is created where the user can see how well the model captures the stock prices and the prediction for the selected timeframe. 

## Findings

A Single Layer LSTM was able to, in 100 epochs, predict the next day stock price with a score of 0.995. For 5 days, it scored 0.947. I turns out that a stacked LSTM severely overfits the data. A simpler architecture is able to fit the data much better. 



## R2 Scores
* Single Layer LSTM: 0.995
* Stacked LSTM: -3.91
* Bidirectional LSTM: 0.994



## Next Steps

* Expand the prediction timeframe
* Explore convolutional neural networks (CNNs)


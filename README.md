# Stock Market Forecast

#### -- Project Status: Active

## Project Intro/Objective

The purpose of this project is to use deep learning to develop a stock market forecast. The reason for using deep learning is so that we can capture non linear trends in the data. 

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

In this project, we use S&P500 historical data collected from Yahoo Finance. The models are trained opening prices from December 27th 1950 to December 24th 2020. The model is then used to make two predictions: next day prediction and 5 day prediction. Finally, an app is created where the user can see how well the model captures the stock prices and the prediction for the selected timeframe. 

## Findings

The Single Layer LSTM was able to, in 100 epochs, predict the next day stock prices with a score of 0.995. For 5 days, it scored 0.947. I turned out that a stacked LSTM severely overfit the data. A simpler architecture was able to fit the data much better. 



## R2 Scores
* Single Layer LSTM: 0.995
* Stacked LSTM: -3.91
* Bidirectional LSTM: 0.994



## Next Steps

* Expand the prediction timeframe
* Explore convolutional neural networks (CNNs)


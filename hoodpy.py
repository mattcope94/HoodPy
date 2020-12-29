import pandas as pd 
from pandas_datareader import data as pdr
import numpy as np
import datetime as dt
import yfinance as yf

#Initial user input
stock=input("Enter stock ticker:")
print(stock)

#Setting timeframe 
startdate = [1,1,2020]
start = dt.datetime(startdate[2],startdate[1],startdate[0])
now= dt.datetime.now()

df=pdr.get_data_yahoo(stock,start,now)
print(df)

import pandas as pd 
from pandas_datareader import data as pdr
import numpy as np
import datetime as dt
import yfinance as yf

#Initial user input
stock=input("Enter stock ticker:")
print(stock)

#Setting timeframe 
startdate=[1,1,2020]
start=dt.datetime(startdate[2],startdate[1],startdate[0])
now=dt.datetime.now()

df=pdr.get_data_yahoo(stock,start,now)
print(df)

#We are using these simple moving averages according to my strategy
df["SMA_20"]=round(df.iloc[:,3].rolling(window=20).mean(),2)
df["SMA_200"]=round(df.iloc[:,3].rolling(window=200).mean(),2)

print(df)

#To help keep track of trades and enter/exit status
enter=False
numHigh=0
numLow=0

#Loop through keeping track of closing price relative to those moving averages ^
for i in df.index:

    #Do this if the stock closed higher than the 20 day simple moving averagekk
    if (df["Adj Close"][i]>df["SMA_20"][i]):
        print("Close is higher")
        numHigh+=1
    else:
        print("Close is lower")
        numLow+=1
print("Close is higher "+str(numHigh)+" times.")
print("Close is lower "+str(numLow)+" times.")
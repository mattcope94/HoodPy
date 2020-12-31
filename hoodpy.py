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

#We are using these simple moving averages according to 20 day sma for now
df["SMA_20"]=round(df.iloc[:,3].rolling(window=20).mean(),2)
df["SMA_200"]=round(df.iloc[:,3].rolling(window=200).mean(),2)

print(df)

#To help keep track of trades and enter/exit status
entered=False
numHigh=0
numLow=0
#specifically positions and their prices
positions=0
buyPrice=0
sellPrice=0

#Loop through keeping track of closing price relative to those moving averages ^
for i in df.index:

    sma20=df["SMA_20"][i]
    #200 day simple moving average is used here as a point of reference/additional confluence
    sma200=df["SMA_200"][i]
    price=df["Adj Close"][i]

    #Do this if the stock closed higher than the 20 day simple moving average
    if (df["Adj Close"][i]>df["SMA_20"][i]):
        print("Close is higher than 20 day SMA")
        numHigh+=1
        if(entered==False):
            print("Entering at $"+str(round(price,2)))
            entered=True
            positions+=1
            buyPrice+=price

    else:
        print("Close is lower  than 20 day SMA")
        numLow+=1
        if(entered==True):
            print("Selling at $"+str(round(price,2)))
            entered=False
            sellPrice+=price

#Messy analytics variables
profit=sellPrice-buyPrice  
closeOut=price+profit

print("Entered "+str(positions)+" positions netting $"+str(round(profit,2))+" profit.")

if entered==True:
    print("Still holding "+stock+". Sell for $"+str(round(closeOut,2))+" profit.")
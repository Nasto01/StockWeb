import streamlit as st
import pandas as pd
import numpy as np
import requests as requests
import tweepy

from alphavantage import *

#specify today
from datetime import date
today = date.today()
date = today.strftime("%Y-%m-%d")



#sidebar selector
option = st.sidebar.selectbox('Which Dashboard',('Twitter', 'StockTwits','ARK'))
st.header (option)


if option == 'Stock Price':
    st.subheader('Stock Dashboard')

if option == 'Twitter':
    st.subheader('Twitter Dashboard')

#stocktwits channel
if option == 'StockTwits':
    symbol = st.sidebar.text_input('Symbol',value='NVDA',max_chars=5)
    st.subheader(f'Stocktwits Dashboard for {symbol}')
    r = requests.get(f'https://api.stocktwits.com/api/2/streams/symbol/{symbol}.json')
    st.write(f'https://finviz.com/quote.ashx?t={symbol}')
    st.image(f'https://finviz.com/chart.ashx?t={symbol}')
    data=r.json()
    for message in data['messages']:
        st.image(message['user']['avatar_url'])
        st.write(message['user']['username'])
        st.write(message['created_at'])
        st.write(message['body'])

#ark ownership and changes
if option == 'ARK':
    st.subheader('Stock Ownership and changes in ARK')
    symbol = st.sidebar.text_input('Symbol',value='NVDA',max_chars=5)
   #Get ownership
    ownership = requests.get(f'https://arkfunds.io/api/v1/stock/fund-ownership?symbol={symbol}').json()
    #Get buys/sells for the ticker
    trades= requests.get(f'https://arkfunds.io/api/v1/stock/trades?symbol={symbol}&date_from=2021-01-01&date_to={date}').json()
    #stock profile
    profile=requests.get(f'https://arkfunds.io/api/v1/stock/profile?symbol={symbol}').json()
    
    #prepare trades dataframe
    trades=pd.DataFrame(trades['trades'])
    trades=trades[['date', 'fund', 'direction', 'shares',
       'etf_percent']].sort_index()
    
    owned_shares=ownership['totals']['shares']
    st.write(f'ARK currently owns {owned_shares} shares.\n')
    
    st.write(f'Last ARK trades for {symbol}')
    st.dataframe(trades)
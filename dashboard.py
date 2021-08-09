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
option = st.sidebar.selectbox('Which Dashboard',('Overview', 'StockTwits','ARK'))
st.header (option)

#Overview
if option == 'Overview':
    st.subheader('Overview Dashboard')
    symbol = st.sidebar.text_input('Symbol',value='NVDA',max_chars=4)
    st.write(f'https://finviz.com/quote.ashx?t={symbol}')
    st.image(f'https://finviz.com/chart.ashx?t={symbol}')
    
    st.subheader('Stock Ownership and changes in ARK')
   #Get ownership
    ownership = requests.get(f'https://arkfunds.io/api/v1/stock/fund-ownership?symbol={symbol}').json()
    #Get buys/sells for the ticker
    trades= requests.get(f'https://arkfunds.io/api/v1/stock/trades?symbol={symbol}&date_from=2021-01-01&date_to={date}').json()
    profile=requests.get(f'https://arkfunds.io/api/v1/stock/profile?symbol={symbol}').json()
    owned_shares=ownership['totals']['shares']
    st.write(f'ARK currently owns {owned_shares} shares.\n')
    if 'detail' in trades:
        st.write(f'There are no ARK trades for {symbol}')
    else:
        trades=pd.DataFrame(trades['trades'])
        trades=trades[['date', 'fund', 'direction', 'shares',
       'etf_percent']].sort_index()
        st.write(f'Last ARK trades for {symbol}')
        st.dataframe(trades)
        
    st.subheader('Analyst recommendations')
    url= base_url = f"https://finnhub.io/api/v1/stock/recommendation?symbol={symbol}&token=bv94chf48v6p9584nq2g"
    s = requests.get(url)
    if len(s.json()) > 0 :
        analyst=pd.DataFrame(s.json())
        st.dataframe(analyst[['period','strongBuy','buy', 'hold',  'sell',  'strongSell']])
    else:
        st.write(f'{symbol} is not covered by any analyst.')
        
    st.subheader('Insider activity')
    url= f"https://finnhub.io/api/v1/stock/insider-transactions?symbol={symbol}&limit=20&token=bv94chf48v6p9584nq2g"
    s = requests.get(url)
    if len(s.json()['data']) > 0:
        insiders=pd.DataFrame(s.json()['data'])
        st.dataframe(insiders[['name', 'share', 'change', 'transactionDate','transactionPrice']])
    else:
        st.write(f'{symbol} does not have any insider activity.')
        
    st.subheader('News')
    s=requests.get(f'https://finnhub.io/api/v1/company-news?symbol={symbol}&from=2021-03-01&to=2021-03-09&token=bv94chf48v6p9584nq2g')
    if len(s.json()) > 0:
        news=pd.DataFrame(s.json())
        news=news[['headline', 'summary', 'url','source',]]
        st.dataframe(news)
    else:
        st.write(f'There are no news for {symbol}.')

    
    
    

#stocktwits channel
if option == 'StockTwits':
    symbol = st.sidebar.text_input('Symbol',value='NVDA',max_chars=4)
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
    profile=requests.get(f'https://arkfunds.io/api/v1/stock/profile?symbol={symbol}').json()
    owned_shares=ownership['totals']['shares']
    st.write(f'ARK currently owns {owned_shares} shares.\n')
    if 'detail' in trades:
        st.write(f'There are no ARK trades for {symbol}')
    else:
        trades=pd.DataFrame(trades['trades'])
        trades=trades[['date', 'fund', 'direction', 'shares',
       'etf_percent']].sort_index()
        st.write(f'Last ARK trades for {symbol}')
        st.dataframe(trades)
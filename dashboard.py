import streamlit as st
import pandas as pd
import numpy as np
import requests as requests
import tweepy




option = st.sidebar.selectbox('Which Dashboard',('Stock Price', 'Twitter', 'StockTwits'))

st.header (option)

if option == 'Stock Price':
    st.subheader('Stock Dashboard')

if option == 'Twitter':
    st.subheader('Twitter Dashboard')
    
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
        
        
        
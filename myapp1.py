#!/usr/bin/env python
# coding: utf-8

# In[12]:


import streamlit as st
import pandas as pd
import requests


# In[6]:


st.write('''
#Simple stock price app

Shown are stock closing price and volume for Google!


''')


# In[13]:




#definition of page & functions
page=('https://www.alphavantage.co/query?')
api=('&apikey=DB0W6OHNAAX59Z9V')
daily=('function=TIME_SERIES_DAILY_ADJUSTED')
symbol=('&symbol=')
full=('&outputsize=full')

#get data and convert to json
def getPage(page,function,symbol,name,api,full=''):
    url=page+function+symbol+name+full+api
    resp=requests.get(url)
    if resp.status_code == 200:
        return resp.json()
    else:
        print('Error:',status_code)
        return -1
    return url

#prepare dataframe function
def prepareDataFrame(name,page,function,symbol,api,full=''):
    #create data dictionary
    data=getPage(page,function,symbol,name,api,full)
    #filter daily list
    data_daily=data['Time Series (Daily)']
    #create dataframe, twist X and Y axis
    data_daily=pd.DataFrame(data_daily).T
    #remove numbers from column_names
    data_daily.columns=['open', 'high', 'low', 'close', 'adjusted_close',
       'volume', 'dividend_amount', 'split_coefficient']
    #change index dtype to datetime
    data_daily.index=pd.to_datetime(data_daily.index)
    #sort according to date - oldest first
    data_daily=data_daily.sort_index(ascending=True)
    #change values tu numeric
    data_daily[['open','high','low','close','adjusted_close','volume','dividend_amount','split_coefficient']]=data_daily[['open','high','low','close','adjusted_close','volume','dividend_amount','split_coefficient']].apply(pd.to_numeric)
    return data_daily


# In[14]:


nvidia=prepareDataFrame('NVDA',page,daily,symbol,api,full)


# In[15]:


nvidia.tail()


# In[18]:


st.line_chart(nvidia.close)


# In[ ]:





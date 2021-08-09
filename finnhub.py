import pandas as pd
import finnhub
import requests

#Analyst recommendations update from finnhub
def Analyst (symbol='NVDA'):
    url= base_url = f"https://finnhub.io/api/v1/stock/recommendation?symbol={symbol}&token=bv94chf48v6p9584nq2g"
    s = requests.get(url)
    analyst=pd.DataFrame(s.json())
    return analyst[['period','strongBuy','buy', 'hold',  'sell',  'strongSell']]


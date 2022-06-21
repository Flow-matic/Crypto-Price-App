import streamlit as st 
import pandas as pd

st.markdown('''# **Binance Price App**
A cryptocurrency price app pulling price data from *Binance API*.
''')

st.header('**Selected Price**')

# Load market data from Binance API 

df = pd.read_json('https://api.binance.com/api/v3/ticker/24hr')

# Custom function for rouinding values

def round_value(input_value):
    if input_value.values > 1:
        a = float(round(input_value, 2))
    else:
        a = float(round(input_value, 8))
    return a

cryptolist = {
    'Price 1': 'BTCBUSD',
    'Price 2': 'ETHBUSD',
    'Price 3': 'BNBBUSD',
    'Price 4': 'XRPBUSD',
    'Price 5': 'ADABUSD',
    'Price 6': 'DOGEBUSD',
    'Price 7': 'SHIBBUSD',
    'Price 8': 'DOTBUSD',
    'Price 9': 'MATICBUSD'
}
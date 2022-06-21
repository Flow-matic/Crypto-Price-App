import streamlit as st 
import pandas as pd 

st.markdown('''# **Binance Price App**
A cryptocurrency price app pulling price data from *Binance API*.
''')

st.header('**Selected Prices')

# Load market data from Binance API

df = pd.read_json('https://api.binance.com/api/v3/ticker/24hr')

# Custom function for rounding values
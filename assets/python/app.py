import streamlit as st 
import pandas as pd 

st.markdown('''# **Binance Price App**
A cryptocurrency price app pulling price data from *Binance API*.
''')

st.header('**Selected Prices')

# Load market data from Binance API

df = pd.read_json('https://api.binance.com/api/v3/ticker/24hr')

# Custom function for rounding values

def round_value(input_value):
    if input_value.values > 1:
        a = float(round(input_value, 2))
    else:
        a = float(round(input_value, 8))
    return a

    
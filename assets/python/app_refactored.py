import streamlit as st 
import pandas as pd

st.markdown('''# **Binance Price App**
A cryptocurrency price app pulling price data from *Binance API*.
''')

st.header('**Selected Price**')

# Load market data from Binance API 

df = pd.read_json('https://api.binance.com/api/v3/ticker/24hr')

# Custom function for rounding values

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

col1, col2, col3 = st.columns(3)

for i in range(len(cryptoList.keys())):
    selected_crypto_label = list(cryptoList.keys())[i]
    selected_crypto_index = list(df.symbol).index(cryptoList[selected_crypto_label])
    selected_crypto = st.sidebar.selectbox(selected_crypto_label, df.symbol, selected_crypto_index, key = str(1))
    col_df = df[df.symbol == selected_crypto]
    col_price = round_value(col_df.weightedAvgPrice)
    col_percent = f'{float(col_df.priceChangePercent)}%'
    if i < 3:
        with col1:
            st.metric(selected_crypto, col_price, col_percent)
    if 2 < i < 6:
        with col2:
            st.metric(selected_crypto, col_price, col_percent)
    if i > 5:
        with col3:
            st.metric(selected_crypto, col_price, col_percent)



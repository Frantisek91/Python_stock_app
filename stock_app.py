 # Import knihoven
import yfinance as yf
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.write("""
# Portfolio
""")

stock_symbols = st.text_input('Vlozit symboly akcii')
#start_date = st.date_input('Start date')
#end_date = st.date_input('End date')
period = st.text_input('Obdobi', '1y')
""" Moznosti: 1d,5d,1mo,3mo,6mo,1y,2y,5y,10y,ytd,max """
interval = st.text_input('Interval', '1h')
""" 1m,2m,5m,15m,30m,60m,90m\n,1h,1d,5d,1wk,1mo,3mo """

# Rozdeleni na jednotlive akcie
stocks = stock_symbols.split()

for stock in stocks: 
    data = yf.Ticker(stock)
    df = data.history(period = period, interval = interval)
    df['Date'] = df.index
    #st.write(df.head(10))
    plt.plot(df.Date, df.Close, color='skyblue', alpha=0.8)
    plt.fill_between(df.Date, df.Close, color = 'skyblue', alpha=0.2)
    plt.xticks(rotation=45)
    #plt.xlabel('Datum', fontweight='bold')
    plt.ylabel('Cena v $', fontweight='bold')
    plt.title(stock, fontweight='bold')
    
    #st.pyplot()

    st.line_chart(df.Close)

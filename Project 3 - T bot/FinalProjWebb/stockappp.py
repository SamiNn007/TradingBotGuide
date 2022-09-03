from distutils import extension
import streamlit as st
import pandas as pd
from PIL import Image
import os
import matplotlib.pyplot as plt
import plotly.tools
import plotly.graph_objects as go
#import plot_plotly

#title
st.write("""
MY GBPUSD PLATFORM
""")

image = Image.open(r"C:\Users\Acer\OneDrive\Desktop\Streamlit\logo 1.png")
st.image(image, use_column_width=True)

## sidebar header
st.sidebar.header('GBPUSD INFORMATION')

option = st.sidebar.selectbox("Select your preferred view", ('line chart', 'pattern'))

st.subheader(option)

if option == 'chart':
    st.subheader('this is the chart dashboard')

## create function
def get_input():
    start_date = st.sidebar.text_input('Start Date', '2003-12-01')
    end_date = st.sidebar.text_input('End Date', '2022-06-01')
    stock_symbol = st.sidebar.text_input('Currency Symbol', 'GBPUSD')
    return start_date, end_date, stock_symbol

# get company name 
def curr_name(symbol):
    if symbol == 'GBPUSD':
        return 'GBPUSD'

# load the data
def get_data(symbol, start, end):
    if symbol.upper() == 'GBPUSD':
        df = pd.read_csv('C:/Users/Acer/OneDrive/Desktop/Streamlit/new_GBPUSD=X.csv')
    else:
        df = pd.DataFrame(columns = ['Date', 'Close', 'Open', 'Adj Close', 'High' 'Low'])
    

    start = pd.to_datetime(start)
    end = pd.to_datetime(end)

    start_row = 0
    end_row = 0

    for i in range(0, len(df)):
        if start <= pd.to_datetime(df['Date'][i]):
            start_row = i
            break

    for j in range(0, len(df)):
        if end >= pd.to_datetime(df['Date'][(len(df)-1)-j]):
            end_row = (len(df) -1) - j
            break

    df = df.set_index(pd.DatetimeIndex(df['Date'].values))

    return df.iloc[start_row:end_row +1, :]

start, end , symbol = get_input()
df = get_data(symbol, start, end)
currency_name = curr_name(symbol.upper())

st.header(currency_name+" Close Price\n")
st.line_chart(df["Open"])

st.header('Data Statistics')
st.write(df.describe())

#st.header('NEW')
#pl = st.empty()
#pl.plotly_chart(df['Open'])

#_, extension = os.path.splitext('stokappp.py')
#extension[1:]
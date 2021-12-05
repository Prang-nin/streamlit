import datetime
import yfinance as yf
import streamlit as st
import pandas as pd
from datetime import date
from plotly import graph_objs as go


def app():
    st.write("""
    ## Commodity Stock Price UP TO DATE
    📉📊💸💰
    """)
    comName = ('GC=F', 'SI=F','CL=F')
    selectedCom = st.selectbox('Select commodity type',comName)
    st.caption('GC=F : Gold , SI=F : Silver , CL=F : Crude oil')

    fromDate = st.date_input("From Date")
    st.write('Display from date :', fromDate,'untill recent time')
    @st.cache
    #Dowload data from yahoo
    def load_data(ticker):
        startDate = str(fromDate)
        nowDate = date.today().strftime("%Y-%m-%d")
        tickerData = yf.download(ticker, startDate, nowDate)
        tickerData.reset_index(inplace=True)
        return tickerData
       
    with st.spinner("Please wait..."):
        rawData = load_data(selectedCom)
    st.subheader('Selcted commodity data')
    st.write(rawData)

    # plot history of raw data
    def plot_raw_data():
        fig = go.Figure()
        fig.add_trace(go.Scatter(x=rawData['Date'], y=rawData['Open'], name="stock_open" ))
        fig.add_trace(go.Scatter(x=rawData['Date'], y=rawData['Close'], name="stock_close"))
        fig.layout.update(title_text='Time Series data with Rangeslider', xaxis_rangeslider_visible=True)
        st.plotly_chart(fig)

    #Select to show plot
    if st.button('Show plot'):
        plot_raw_data()


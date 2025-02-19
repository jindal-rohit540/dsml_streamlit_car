import streamlit as st
import yfinance as yf
import datetime

st.title(" This is my stock data application")
st.image("stocks.jpg", caption="Sunrise by the mountains")

ticker_symbol = st.text_input("Enter the stock data you want", "AAPL")


col1, col2 = st.columns(2)

with col1:
    start_date = st.date_input("Enter start date", datetime.date(2019, 7, 6))

with col2:
    end_date = st.date_input("Enter End Date", datetime.date(2020, 7, 6))


ticker_data = yf.Ticker(ticker_symbol)

ticker_df = ticker_data.history(period = "1d", start = start_date , end = end_date)



st.dataframe(ticker_df, use_container_width=True)

st.write(f"This is the line chart of {ticker_symbol}")

st.line_chart(ticker_df.Close)
st.write(f"This is the Volume chart of {ticker_symbol}")

st.line_chart(ticker_df.Volume)


# app.py

import streamlit as st
import pandas as pd
import seaborn as sb
import matplotlib.pyplot as plt

# Page config
st.set_page_config(page_title="Nifty Stocks Viewer", layout="wide")

# Load the dataset
@st.cache_data
def load_data():
    df = pd.read_csv("Nifty_Stocks.csv")
    df['Date'] = pd.to_datetime(df['Date'])
    return df

df = load_data()

st.title("📈 Nifty Stocks Time Series Viewer")

# Select Category
categories = df['Category'].unique()
selected_category = st.selectbox("Select a Category", sorted(categories))

# Filter by Category
filtered_df = df[df['Category'] == selected_category]

# Select Symbol
symbols = filtered_df['Symbol'].unique()
selected_symbol = st.selectbox("Select a Symbol", sorted(symbols))

# Filter by Symbol
stock_data = filtered_df[filtered_df['Symbol'] == selected_symbol]

# Plotting
st.subheader(f"Closing Price of {selected_symbol} over Time")

fig, ax = plt.subplots(figsize=(12, 6))
sb.lineplot(data=stock_data, x='Date', y='Close', ax=ax)
ax.set_title(f"{selected_symbol} Closing Prices")
ax.set_xlabel("Date")
ax.set_ylabel("Close Price")
plt.xticks(rotation=45)
st.pyplot(fig)

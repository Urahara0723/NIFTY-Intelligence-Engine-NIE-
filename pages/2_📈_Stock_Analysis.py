import streamlit as st
import pandas as pd
import plotly.express as px

st.title("📈 Stock Analysis")

df = pd.read_csv("data/master_df.csv")

df["Date"] = pd.to_datetime(df["Date"])

stock = st.selectbox(
    "Select Stock",
    sorted(df["Stock"].unique())
)

stock_df = df[
    df["Stock"] == stock
].copy()

# Price Chart
fig = px.line(
    stock_df,
    x="Date",
    y="Close",
    title=f"{stock} Closing Price"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

# Volume Chart
fig2 = px.line(
    stock_df,
    x="Date",
    y="Volume",
    title=f"{stock} Trading Volume"
)

st.plotly_chart(
    fig2,
    use_container_width=True
)

fig = px.line(
    stock_df,
    x="Date",
    y=[
        "Close",
        "SMA20",
        "SMA50",
        "SMA200"
    ],
    title=f"{stock} Price & Moving Averages"
)

st.plotly_chart(
    fig,
    use_container_width=True
)
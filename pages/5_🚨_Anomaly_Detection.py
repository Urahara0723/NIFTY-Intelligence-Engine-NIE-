import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="Anomaly Detection",
    page_icon="🚨",
    layout="wide"
)

st.title("🚨 Market Anomaly Detection")

st.markdown("""
Identify unusual market behavior using Isolation Forest.

Detected using:

- Daily Returns
- Trading Volume
- Rolling Volatility
""")

# ----------------------------------
# LOAD DATA
# ----------------------------------

df = pd.read_csv("data/anomaly_df.csv")

if "Date" in df.columns:
    df["Date"] = pd.to_datetime(df["Date"])

# ----------------------------------
# ANOMALIES ONLY
# ----------------------------------

anomalies = df[df["Anomaly"] == -1]

# ----------------------------------
# KPI SECTION
# ----------------------------------

col1, col2 = st.columns(2)

col1.metric(
    "Total Records",
    len(df)
)

col2.metric(
    "Detected Anomalies",
    len(anomalies)
)

st.divider()

# ----------------------------------
# TOP ANOMALY STOCKS
# ----------------------------------

st.subheader("Stocks with Highest Number of Anomalies")

anomaly_counts = (
    anomalies["Stock"]
    .value_counts()
    .head(15)
    .reset_index()
)

anomaly_counts.columns = [
    "Stock",
    "Count"
]

fig = px.bar(
    anomaly_counts,
    x="Stock",
    y="Count",
    title="Top Anomalous Stocks"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

# ----------------------------------
# STOCK SELECTOR
# ----------------------------------

st.subheader("Stock-wise Anomaly Analysis")

stock = st.selectbox(
    "Select Stock",
    sorted(df["Stock"].unique())
)

stock_df = df[
    df["Stock"] == stock
]

stock_anomalies = stock_df[
    stock_df["Anomaly"] == -1
]

# ----------------------------------
# PRICE CHART
# ----------------------------------

fig2 = px.line(
    stock_df,
    x="Date",
    y="Close",
    title=f"{stock} Price History"
)

fig2.add_scatter(
    x=stock_anomalies["Date"],
    y=stock_anomalies["Close"],
    mode="markers",
    name="Anomaly"
)

st.plotly_chart(
    fig2,
    use_container_width=True
)

# ----------------------------------
# ANOMALY TABLE
# ----------------------------------

st.subheader("Detected Anomaly Events")

st.dataframe(
    stock_anomalies[
        [
            "Date",
            "Close",
            "Daily_Return",
            "Volume"
        ]
    ].sort_values(
        "Date",
        ascending=False
    ),
    use_container_width=True
)

# ----------------------------------
# INSIGHTS
# ----------------------------------

st.subheader("Key Findings")

st.success("""
Isolation Forest successfully identified:

• COVID-19 crash period (2020)

• Global Financial Crisis events (2008)

• Extreme volatility spikes

• Unusual trading activity

These anomalies can help investors
identify market stress periods and
improve risk-aware decision making.
""")
import streamlit as st
import pandas as pd
import plotly.express as px

st.title("📊 Market Overview")

df = pd.read_csv("data/master_df.csv")

# KPIs
col1, col2, col3 = st.columns(3)

col1.metric(
    "Total Stocks",
    df["Stock"].nunique()
)

col2.metric(
    "Industries",
    df["Industry"].nunique()
)

col3.metric(
    "Records",
    len(df)
)

st.divider()

# Industry Distribution
industry_counts = (
    df["Industry"]
    .value_counts()
    .reset_index()
)

industry_counts.columns = [
    "Industry",
    "Count"
]

fig = px.bar(
    industry_counts,
    x="Industry",
    y="Count",
    title="Industry Distribution"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

# Date Range
st.subheader("Dataset Coverage")

st.write(
    f"From **{df['Date'].min()}** to **{df['Date'].max()}**"
)
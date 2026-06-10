import streamlit as st
import pandas as pd
import plotly.express as px

# ---------------------------------------
# PAGE CONFIG
# ---------------------------------------

st.set_page_config(
    page_title="Risk Analyzer",
    page_icon="⚠️",
    layout="wide"
)

st.title("⚠️ Risk Analyzer")

st.markdown("""
Analyze the historical risk characteristics of NIFTY-50 stocks using:

- Volatility
- Sharpe Ratio
- Sortino Ratio
- Maximum Drawdown
- Total Return
""")

# ---------------------------------------
# LOAD DATA
# ---------------------------------------

risk_df = pd.read_csv("data/risk_df.csv")

# ---------------------------------------
# STOCK SELECTOR
# ---------------------------------------

stock = st.selectbox(
    "Select Stock",
    sorted(risk_df["Stock"].unique())
)

stock_data = risk_df[
    risk_df["Stock"] == stock
].iloc[0]

# ---------------------------------------
# METRICS
# ---------------------------------------

st.subheader(f"Risk Metrics : {stock}")

col1, col2, col3 = st.columns(3)

col1.metric(
    "Total Return (%)",
    f"{stock_data['Total_Return_%']:.2f}"
)

col2.metric(
    "Volatility",
    f"{stock_data['Volatility']:.4f}"
)

col3.metric(
    "Sharpe Ratio",
    f"{stock_data['Sharpe']:.4f}"
)

col4, col5 = st.columns(2)

col4.metric(
    "Sortino Ratio",
    f"{stock_data['Sortino']:.4f}"
)

col5.metric(
    "Max Drawdown",
    f"{stock_data['Max_Drawdown']:.2%}"
)

st.divider()

# ---------------------------------------
# RISK INTERPRETATION
# ---------------------------------------

st.subheader("Investment Interpretation")

sharpe = stock_data["Sharpe"]
volatility = stock_data["Volatility"]

if sharpe > 0.5:
    st.success(
        "Strong risk-adjusted performance."
    )
elif sharpe > 0.2:
    st.warning(
        "Moderate risk-adjusted performance."
    )
else:
    st.error(
        "Weak risk-adjusted performance."
    )

if volatility > 0.45:
    st.warning(
        "High volatility stock."
    )
elif volatility > 0.30:
    st.info(
        "Moderate volatility stock."
    )
else:
    st.success(
        "Relatively stable stock."
    )

st.divider()

# ---------------------------------------
# TOP 10 SHARPE
# ---------------------------------------

st.subheader("🏆 Top 10 Stocks by Sharpe Ratio")

top_sharpe = (
    risk_df
    .sort_values(
        "Sharpe",
        ascending=False
    )
    .head(10)
)

fig = px.bar(
    top_sharpe,
    x="Stock",
    y="Sharpe",
    title="Top 10 Risk-Adjusted Performers"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

# ---------------------------------------
# TOP 10 VOLATILITY
# ---------------------------------------

st.subheader("📈 Most Volatile Stocks")

top_volatility = (
    risk_df
    .sort_values(
        "Volatility",
        ascending=False
    )
    .head(10)
)

fig2 = px.bar(
    top_volatility,
    x="Stock",
    y="Volatility",
    title="Top 10 Most Volatile Stocks"
)

st.plotly_chart(
    fig2,
    use_container_width=True
)

# ---------------------------------------
# TOP 10 DRAWDOWNS
# ---------------------------------------

st.subheader("📉 Largest Historical Drawdowns")

drawdown_df = (
    risk_df
    .sort_values(
        "Max_Drawdown"
    )
    .head(10)
)

fig3 = px.bar(
    drawdown_df,
    x="Stock",
    y="Max_Drawdown",
    title="Worst Historical Drawdowns"
)

st.plotly_chart(
    fig3,
    use_container_width=True
)

# ---------------------------------------
# FULL TABLE
# ---------------------------------------

st.subheader("Complete Risk Table")

st.dataframe(
    risk_df.sort_values(
        "Sharpe",
        ascending=False
    ),
    use_container_width=True
)
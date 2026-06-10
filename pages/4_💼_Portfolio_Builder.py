import streamlit as st
import pandas as pd
import json
import plotly.express as px

st.set_page_config(
    page_title="Portfolio Builder",
    page_icon="💼",
    layout="wide"
)

st.title("💼 Portfolio Builder")

st.markdown("""
Generate investment portfolios tailored to different investor profiles:

- Conservative
- Balanced
- Aggressive
""")

# --------------------------------
# LOAD PORTFOLIOS
# --------------------------------

with open("portfolios/conservative_portfolio.json") as f:
    conservative = json.load(f)

with open("portfolios/balanced_portfolio.json") as f:
    balanced = json.load(f)

with open("portfolios/aggressive_portfolio.json") as f:
    aggressive = json.load(f)

# --------------------------------
# SELECT PROFILE
# --------------------------------

profile = st.selectbox(
    "Select Investor Profile",
    [
        "Conservative",
        "Balanced",
        "Aggressive"
    ]
)

if profile == "Conservative":
    portfolio = conservative
    description = """
    Low risk portfolio focused on capital preservation,
    stability, and lower volatility.
    """

elif profile == "Balanced":
    portfolio = balanced
    description = """
    Moderate risk portfolio balancing growth
    and stability.
    """

else:
    portfolio = aggressive
    description = """
    High risk portfolio focused on maximizing
    long-term returns.
    """

st.info(description)

# --------------------------------
# CLEAN DATA
# --------------------------------

portfolio_df = pd.DataFrame(
    portfolio.items(),
    columns=["Stock", "Weight"]
)

portfolio_df = portfolio_df[
    portfolio_df["Weight"] > 0
]

portfolio_df["Weight (%)"] = (
    portfolio_df["Weight"] * 100
)

portfolio_df = portfolio_df.sort_values(
    "Weight",
    ascending=False
)

# --------------------------------
# TABLE
# --------------------------------

st.subheader("Portfolio Allocation")

st.dataframe(
    portfolio_df[
        ["Stock", "Weight (%)"]
    ],
    use_container_width=True
)

# --------------------------------
# PIE CHART
# --------------------------------

fig = px.pie(
    portfolio_df,
    names="Stock",
    values="Weight (%)",
    title=f"{profile} Portfolio Allocation"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

# --------------------------------
# TOP HOLDINGS
# --------------------------------

st.subheader("Top Holdings")

top_holdings = portfolio_df.head(5)

fig2 = px.bar(
    top_holdings,
    x="Stock",
    y="Weight (%)",
    title="Top Portfolio Holdings"
)

st.plotly_chart(
    fig2,
    use_container_width=True
)
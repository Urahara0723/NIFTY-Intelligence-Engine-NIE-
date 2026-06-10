import streamlit as st

st.set_page_config(
    page_title="NIFTY Investment Intelligence",
    page_icon="📈",
    layout="wide"
)

# ==================================================
# CSS
# ==================================================

st.markdown("""
<style>

.hero {
    background: linear-gradient(135deg,#0f172a,#1e293b);
    padding: 2rem;
    border-radius: 20px;
    color: white;
    margin-bottom: 2rem;
}

.card {
    background: #111827;
    border: 1px solid #334155;
    border-radius: 18px;
    padding: 20px;
    min-height: 220px;
    margin-bottom: 10px;
}

.card-title {
    font-size: 26px;
    font-weight: bold;
    margin-bottom: 10px;
}

.card-desc {
    color: #cbd5e1;
    font-size: 15px;
}

div.stButton > button {
    width: 100%;
    border-radius: 10px;
    height: 45px;
    font-weight: bold;
}

</style>
""", unsafe_allow_html=True)

# ==================================================
# HERO SECTION
# ==================================================

st.markdown("""
<div class="hero">
    <h1>📈 NIFTY Investment Intelligence Platform</h1>
    <h3>AI-Powered Investment Decision Support System</h3>
    <p>
    Transform historical NIFTY-50 market data into actionable investment intelligence
    using Machine Learning, Portfolio Optimization, Risk Analytics,
    Market Anomaly Detection and Explainable AI.
    </p>
</div>
""", unsafe_allow_html=True)
# ==================================================
# KPI SECTION
# ==================================================

c1, c2, c3, c4 = st.columns(4)

c1.metric("Stocks", "49")
c2.metric("Industries", "13")
c3.metric("Records", "235K+")
c4.metric("Years", "21")

st.divider()

st.subheader("🚀 Platform Modules")

# ==================================================
# ROW 1
# ==================================================

col1, col2, col3 = st.columns(3)

with col1:

    st.markdown("""
    <div class="card">
        <div class="card-title">📊 Market Overview</div>
        <div class="card-desc">
        Industry distribution, sector insights and
        market-wide statistics.
        </div>
    </div>
    """, unsafe_allow_html=True)

    if st.button(
        "Open Module",
        key="market"
    ):
        st.switch_page(
            "pages/1_📊_Market_Overview.py"
        )

with col2:

    st.markdown("""
    <div class="card">
        <div class="card-title">📈 Stock Analysis</div>
        <div class="card-desc">
        Analyze stock prices, volume,
        moving averages, RSI and MACD.
        </div>
    </div>
    """, unsafe_allow_html=True)

    if st.button(
        "Open Module",
        key="stock"
    ):
        st.switch_page(
            "pages/2_📈_Stock_Analysis.py"
        )

with col3:

    st.markdown("""
    <div class="card">
        <div class="card-title">⚠️ Risk Analyzer</div>
        <div class="card-desc">
        Sharpe Ratio, Sortino Ratio,
        Volatility and Drawdown Analysis.
        </div>
    </div>
    """, unsafe_allow_html=True)

    if st.button(
        "Open Module",
        key="risk"
    ):
        st.switch_page(
            "pages/3_⚠️_Risk_Analyzer.py"
        )

# ==================================================
# ROW 2
# ==================================================

col4, col5, col6 = st.columns(3)

with col4:

    st.markdown("""
    <div class="card">
        <div class="card-title">💼 Portfolio Builder</div>
        <div class="card-desc">
        Conservative, Balanced and
        Aggressive investment portfolios.
        </div>
    </div>
    """, unsafe_allow_html=True)

    if st.button(
        "Open Module",
        key="portfolio"
    ):
        st.switch_page(
            "pages/4_💼_Portfolio_Builder.py"
        )

with col5:

    st.markdown("""
    <div class="card">
        <div class="card-title">🚨 Anomaly Detection</div>
        <div class="card-desc">
        Detect unusual market events,
        crashes and volatility spikes.
        </div>
    </div>
    """, unsafe_allow_html=True)

    if st.button(
        "Open Module",
        key="anomaly"
    ):
        st.switch_page(
            "pages/5_🚨_Anomaly_Detection.py"
        )

with col6:

    st.markdown("""
    <div class="card">
        <div class="card-title">🤖 Prediction Engine</div>
        <div class="card-desc">
        Future stock direction and
        return forecasting.
        </div>
    </div>
    """, unsafe_allow_html=True)

    if st.button(
        "Open Module",
        key="prediction"
    ):
        st.switch_page(
            "pages/6_🤖_Prediction_Engine.py"
        )

# ==================================================
# ROW 3
# ==================================================

col7, col8 = st.columns(2)

with col7:

    st.markdown("""
    <div class="card">
        <div class="card-title">🔍 AI Insights</div>
        <div class="card-desc">
        SHAP explainability and
        feature importance analysis.
        </div>
    </div>
    """, unsafe_allow_html=True)

    if st.button(
        "Open Module",
        key="ai"
    ):
        st.switch_page(
            "pages/7_🔍_AI_Insights.py"
        )

with col8:

    st.markdown("""
    <div class="card">
        <div class="card-title">🎯 Project Objective</div>
        <div class="card-desc">
        Develop an AI-powered investment intelligence platform that transforms historical NIFTY-50 market data into actionable insights. The system assists investors in analyzing stock performance, assessing risk, optimizing portfolios, detecting market anomalies, and making data-driven investment decisions through explainable machine learning and financial analytics.
        </div>
    </div>
    """, unsafe_allow_html=True)

st.divider()

st.caption(
    "Built by Mohit Trivedi, IIT Roorkee - using NIFTY-50 Historical Market Data • "
    "XGBoost • SHAP • Streamlit • PyPortfolioOpt"
)
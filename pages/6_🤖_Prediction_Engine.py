import streamlit as st
import pandas as pd
import joblib
import numpy as np

st.set_page_config(
    page_title="Prediction Engine",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 Stock Prediction Engine")

st.markdown("""
Predict future stock behavior using the trained XGBoost models.
""")

# ---------------------------------
# LOAD DATA
# ---------------------------------

df = pd.read_csv("data/master_df.csv")

# ---------------------------------
# LOAD MODELS
# ---------------------------------

direction_model = joblib.load(
    "models/direction_model.pkl"
)

return_model = joblib.load(
    "models/return_model.pkl"
)

# ---------------------------------
# FEATURES
# ---------------------------------

features = [
    "Open",
    "High",
    "Low",
    "Close",
    "VWAP",
    "Volume",
    "Turnover",
    "SMA20",
    "SMA50",
    "SMA200",
    "EMA20",
    "EMA50",
    "RSI",
    "MACD",
    "BB_High",
    "BB_Low",
    "Return_5D",
    "Return_20D",
    "Volatility20"
]

# ---------------------------------
# STOCK SELECTOR
# ---------------------------------

stock = st.selectbox(
    "Select Stock",
    sorted(df["Stock"].unique())
)

stock_df = (
    df[df["Stock"] == stock]
    .sort_values("Date")
)

latest = stock_df.iloc[-1]

X = pd.DataFrame(
    [latest[features]]
)

# ---------------------------------
# PREDICTIONS
# ---------------------------------

direction = direction_model.predict(X)[0]

expected_return = return_model.predict(X)[0]

# ---------------------------------
# DISPLAY
# ---------------------------------

st.subheader(f"Prediction Results : {stock}")

col1, col2 = st.columns(2)

if direction == 1:
    col1.success("📈 Predicted Direction: UP")
else:
    col1.error("📉 Predicted Direction: DOWN")

col2.metric(
    "Expected Return",
    f"{expected_return:.2%}"
)

st.divider()

# ---------------------------------
# CONFIDENCE
# ---------------------------------

try:
    probs = direction_model.predict_proba(X)

    up_prob = probs[0][1]
    down_prob = probs[0][0]

    st.subheader("Prediction Confidence")

    st.write(
        f"UP Probability: {up_prob:.2%}"
    )

    st.write(
        f"DOWN Probability: {down_prob:.2%}"
    )

except:
    pass

# ---------------------------------
# TECHNICAL SNAPSHOT
# ---------------------------------

st.subheader("Latest Technical Indicators")

tech = pd.DataFrame({
    "Indicator": [
        "RSI",
        "MACD",
        "SMA20",
        "SMA50",
        "EMA20",
        "EMA50"
    ],
    "Value": [
        latest["RSI"],
        latest["MACD"],
        latest["SMA20"],
        latest["SMA50"],
        latest["EMA20"],
        latest["EMA50"]
    ]
})

st.dataframe(
    tech,
    use_container_width=True
)

# ---------------------------------
# DISCLAIMER
# ---------------------------------

st.warning("""
Predictions are based solely on historical market data
and technical indicators. They should not be interpreted
as financial advice. 
""")
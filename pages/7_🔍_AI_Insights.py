import streamlit as st
from PIL import Image

st.title("🔍 AI Insights")

st.markdown("""
This page explains the factors that influence
the machine learning predictions.
""")

img = Image.open(
    "assets/shap_summary.png"
)

st.image(
    img,
    use_container_width=True
)

st.subheader("Top Influential Features")

st.markdown("""
1. RSI
2. MACD
3. Return_20D
4. Volatility20
5. SMA50

These features were identified as the most influential
drivers of stock direction predictions.
""")
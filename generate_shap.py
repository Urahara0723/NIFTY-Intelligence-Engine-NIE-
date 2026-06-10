import shap
import matplotlib.pyplot as plt
import joblib
import pandas as pd
import os

os.makedirs("assets", exist_ok=True)

model = joblib.load("models/direction_model.pkl")

df = pd.read_csv("data/master_df.csv")

features = [
    "Open","High","Low","Close","VWAP","Volume",
    "Turnover","SMA20","SMA50","SMA200",
    "EMA20","EMA50","RSI","MACD",
    "BB_High","BB_Low",
    "Return_5D","Return_20D","Volatility20"
]

X = df[features].copy()
X = X.dropna()

sample = X.sample(1000, random_state=42)

explainer = shap.TreeExplainer(model)
shap_values = explainer.shap_values(sample)

plt.figure(figsize=(10, 6))

shap.summary_plot(
    shap_values,
    sample,
    show=False
)

plt.tight_layout()

plt.savefig(
    "assets/shap_summary.png",
    bbox_inches="tight"
)

plt.close()

print("Saved: assets/shap_summary.png")
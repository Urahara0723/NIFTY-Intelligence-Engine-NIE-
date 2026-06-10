# 📈 NIFTY Investment Intelligence Platform

<div align="center">

### 🚀 AI-Powered Investment Decision Support System

Transforming Historical NIFTY-50 Market Data into Actionable Investment Intelligence using Machine Learning, Portfolio Optimization, Risk Analytics, Anomaly Detection, and Explainable AI.

![Python](https://img.shields.io/badge/Python-3.12-blue)
![Machine Learning](https://img.shields.io/badge/Machine%20Learning-XGBoost-orange)
![FinTech](https://img.shields.io/badge/Domain-FinTech-green)
![Streamlit](https://img.shields.io/badge/Deployment-Streamlit-red)
![License](https://img.shields.io/badge/License-MIT-yellow)

</div>

---

# 🌟 Overview

Financial markets generate enormous amounts of data every day, making it challenging for investors to identify meaningful trends and make informed investment decisions.

The **NIFTY Investment Intelligence Platform** is an end-to-end AI-powered investment analytics system built using historical NIFTY-50 stock market data. The platform combines machine learning, quantitative finance, risk analytics, portfolio optimization, anomaly detection, and explainable AI to provide practical decision-support tools for investors.

Unlike traditional stock prediction systems, this project focuses on **investment intelligence**, helping users understand market behavior, evaluate risk, optimize portfolios, and make data-driven investment decisions.

---
## 🌐 Live Demo

🚀 Try the application here:

**https://nifty-intelligence-engine.streamlit.app/**

---
# 🌐 Domain

### Artificial Intelligence • Machine Learning • FinTech • Investment Analytics • Data Science

This project lies at the intersection of:

* 🤖 Artificial Intelligence
* 📊 Machine Learning 
* 💰 Financial Technology (FinTech)
* 📈 Quantitative Finance
* 📉 Investment Analytics

---

# 🎯 Project Objectives

The platform aims to:

✅ Analyze historical stock performance

✅ Generate actionable investment insights

✅ Assess investment risk using financial metrics

✅ Construct optimized portfolios for different investor profiles

✅ Detect unusual market behavior and anomalies

✅ Forecast future stock behavior using machine learning

✅ Improve transparency through Explainable AI

✅ Support evidence-based investment decision making

---

# 📂 Dataset

## NIFTY-50 Historical Stock Market Dataset 

https://www.kaggle.com/datasets/rohanrao/nifty50-stock-market-data/data 

### Dataset Characteristics

| Attribute   | Value                                |
| ----------- | ------------------------------------ |
| Time Period | January 2000 – April 2021            |
| Stocks      | 49                                   |
| Industries  | 13                                   |
| Records     | 235,192                              |
| Market      | National Stock Exchange (NSE), India |

### Available Features

#### Market Data

* Open Price
* High Price
* Low Price
* Close Price
* VWAP
* Volume
* Turnover

#### Company Metadata

* Company Name
* Stock Symbol
* Industry Classification

---

# ⚙️ Feature Engineering

The following technical indicators were generated:

## Trend Indicators

* Simple Moving Average (SMA20)
* Simple Moving Average (SMA50)
* Simple Moving Average (SMA200)
* Exponential Moving Average (EMA20)
* Exponential Moving Average (EMA50)

## Momentum Indicators

* Relative Strength Index (RSI)
* MACD

## Volatility Indicators

* Bollinger Bands
* Rolling Volatility

## Return Features

* 5-Day Returns
* 20-Day Returns
* Future Returns

---

# 🤖 Stock Predictor Engine

The platform includes two machine learning models.

## 1️⃣ Direction Prediction Model

Predicts whether a stock is likely to move:

* 📈 Upward
* 📉 Downward

### Algorithm

* XGBoost Classifier

### Evaluation Metrics

* Accuracy
* Precision
* Recall
* F1 Score

---

## 2️⃣ Return Forecasting Model

Predicts future stock returns.

### Algorithm

* XGBoost Regressor

### Evaluation Metrics

* MAE
* RMSE
* R² Score

---

# ⚠️ Risk Assessment Module

The Risk Assessment Engine evaluates the historical risk characteristics of stocks using:

## Metrics

* Volatility
* Sharpe Ratio
* Sortino Ratio
* Maximum Drawdown
* Risk-Adjusted Return

### Benefits

* Compare stocks beyond returns
* Evaluate downside risk
* Assess portfolio stability
* Improve investment decisions

---

# 💼 Portfolio Construction Module

Portfolio optimization was performed using Modern Portfolio Theory (MPT).

## Investor Profiles

### 🟢 Conservative Portfolio

Focus:

* Capital Preservation
* Stable Returns
* Low Volatility

---

### 🟡 Balanced Portfolio

Focus:

* Diversification
* Risk-Adjusted Growth

---

### 🔴 Aggressive Portfolio

Focus:

* Maximum Return Potential
* Higher Risk Tolerance

### Optimization Technique

* Efficient Frontier
* Mean-Variance Optimization
* Risk-Return Tradeoff Analysis

---

# 🚨 Market Anomaly Detection

An Isolation Forest model was developed to identify unusual market behavior.

## Detection Inputs

* Daily Returns
* Trading Volume
* Volatility

## Capabilities

* Detect abnormal price movements
* Identify volatility spikes
* Detect unusual trading activity
* Highlight market stress periods

### Examples Detected

* COVID-19 Market Crash (2020)
* Global Financial Crisis Effects
* Extreme Volatility Events

---

# 🔍 Explainable AI

To improve model transparency, SHAP (SHapley Additive Explanations) was used.

## Explainability Features

* Global Feature Importance
* Model Interpretability
* Decision Transparency

### Most Influential Features

1. RSI
2. MACD
3. Return_20D
4. Volatility20
5. SMA50

---

# 🖥️ Interactive Dashboard

The entire solution is deployed using Streamlit.

## Dashboard Modules

### 📊 Market Overview

* Industry Distribution
* Dataset Statistics
* Market Insights

### 📈 Stock Analysis

* Price Trends
* Volume Analysis
* Technical Indicators

### 🤖 Prediction Engine

* Stock Direction Forecasting
* Return Estimation

### ⚠️ Risk Analyzer

* Sharpe Ratio
* Sortino Ratio
* Volatility
* Drawdown

### 💼 Portfolio Builder

* Conservative Portfolio
* Balanced Portfolio
* Aggressive Portfolio

### 🚨 Anomaly Detection

* Market Anomalies
* Volatility Spikes
* Unusual Trading Activity

### 🔍 AI Insights

* SHAP Explanations
* Feature Importance Analysis

---

# 🛠️ Technology Stack

## Programming Language

* Python

## Data Analysis

* Pandas
* NumPy

## Machine Learning

* XGBoost
* Scikit-Learn

## Financial Analytics

* PyPortfolioOpt

## Explainable AI

* SHAP

## Data Visualization

* Plotly
* Matplotlib

## Dashboard Development

* Streamlit

## Model Persistence

* Joblib

## Development Tools

* Google Colab
* Visual Studio Code

## Version Control

* Git
* GitHub

---

# 📁 Project Structure

```text
NIFTY_INVESTMENT_INTELLIGENCE

│
├── app.py
│
├── data/
│   ├── master_df.csv
│   ├── risk_df.csv
│   └── anomaly_df.csv
│
├── models/
│   ├── direction_model.pkl
│   └── return_model.pkl
│
├── portfolios/
│   ├── conservative_portfolio.json
│   ├── balanced_portfolio.json
│   └── aggressive_portfolio.json
│
├── assets/
│   └── shap_summary.png
│
├── pages/
│
├── requirements.txt
│
└── README.md
```

---

# 🚀 Installation

Clone the repository:

```bash
git clone <repository-url>
cd NIFTY_INVESTMENT_INTELLIGENCE
```

Create virtual environment:

```bash
python -m venv venv
```

Activate environment:

### Windows

```bash
venv\Scripts\activate
```

### Linux / Mac

```bash
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

# ▶️ Run the Application

```bash
streamlit run app.py
```

The dashboard will launch at:

```text
http://localhost:8501
```

---

# 📈 Key Outcomes

* End-to-end investment intelligence platform
* Multi-factor stock analysis framework
* AI-powered prediction engine
* Risk-aware portfolio optimization
* Market anomaly detection system
* Explainable machine learning framework
* Interactive financial analytics dashboard

---

# 🔮 Future Scope

* Real-time market integration
* Deep Learning forecasting models, imoproving the prediction accuracy metrics
* Reinforcement Learning portfolios
* Personalized investment recommendations
* Cloud deployment

---

# 👨‍💻 Author

**Mohit Trivedi**
IIT Roorkee

Developed as part of an AI-driven Investment Intelligence challenge by Cult council of IITR focused on transforming historical stock market data into actionable financial insights.

---

<div align="center">

</div>


import streamlit as st
import pandas as pd
import joblib
import os

script_dir = os.path.dirname(os.path.abspath(__file__))
model_path = os.path.join(script_dir, "aapl_model_fixed.pkl")

model = joblib.load(model_path)

st.title("📈 AAPL Stock Price Predictor (Next 7-Day Average)")

fed_rate = st.number_input("联邦基金利率 FEDFUNDS", 0.0, 10.0, 5.0, 0.1)
sentiment = st.radio("经济新闻情绪是否乐观？", ["Yes", "No"])
sentiment_val = 1 if sentiment == "Yes" else 0
volatility = st.slider("市场波动性 (1-10)", 1, 10, 5)
volume_flag = st.radio("AAPL 最近交易量是否高？", ["Yes", "No"])
volume_val = 1 if volume_flag == "Yes" else 0
sp500_trend = st.radio("标普500 走势", ["Rising", "Falling"])
sp500_val = 1 if sp500_trend == "Rising" else 0

input_df = pd.DataFrame({
    "FEDFUNDS": [fed_rate],
    "sentiment": [sentiment_val],
    "AAPL_21d_Volatility": [volatility / 10],
    "AAPL_HighVolume": [volume_val],
    "SP500_Return": [sp500_val]
})

if st.button("预测未来7天平均价格"):
    prediction = model.predict(input_df)[0]
    st.success(f"📊 预测未来7天平均股价为：${prediction:.2f}")

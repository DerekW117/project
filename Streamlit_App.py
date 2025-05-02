
import streamlit as st
import pandas as pd
import joblib

model = joblib.load("aapl_model_fixed.pkl")

st.title("📈 AAPL Stock Price Predictor")

fed_rate = st.slider("联邦基金利率", 0.0, 10.0, 5.0)
sentiment = st.radio("情绪是否乐观", ["Yes", "No"])
volatility = st.slider("市场波动性", 1, 10, 5)
volume_flag = st.radio("交易量高吗", ["Yes", "No"])
sp500_trend = st.radio("标普走势", ["Rising", "Falling"])

input_df = pd.DataFrame({
    "FEDFUNDS": [fed_rate],
    "sentiment": [1 if sentiment == "Yes" else 0],
    "AAPL_21d_Volatility": [volatility / 10],
    "AAPL_HighVolume": [1 if volume_flag == "Yes" else 0],
    "SP500_Return": [1 if sp500_trend == "Rising" else 0]
})

if st.button("预测"):
    prediction = model.predict(input_df)[0]
    st.success(f"预测结果：${prediction:.2f}")

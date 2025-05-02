
import streamlit as st
import pandas as pd

st.title("AAPL Stock Price Predictor (Fixed Output)")

fed_rate = st.slider("Federal Funds Rate (%)", 0.0, 10.0, 5.0, 0.25)
sentiment = st.radio("Is the economic sentiment positive?", ["Yes", "No"])
volatility = st.slider("Market Volatility (1-10)", 1, 10, 5)
volume_flag = st.radio("Is AAPL's recent trading volume high?", ["Yes", "No"])
sp500_trend = st.radio("S&P 500 Trend", ["Rising", "Falling"])

input_df = pd.DataFrame({
    "FEDFUNDS": [fed_rate],
    "sentiment": [1 if sentiment == "Yes" else 0],
    "AAPL_21d_Volatility": [volatility / 10],
    "AAPL_HighVolume": [1 if volume_flag == "Yes" else 0],
    "SP500_Return": [1 if sp500_trend == "Rising" else 0]
})

st.subheader("Model Input Preview")
st.write(input_df)

if st.button("Predict"):
    prediction = 165.00
    st.success(f"Predicted AAPL average price for the next 7 days: ${prediction:.2f}")

import streamlit as st
import numpy as np
import pandas as pd
from tensorflow.keras.models import load_model
from sklearn.preprocessing import MinMaxScaler
from datetime import datetime, timedelta

# Load the data and model
data = pd.read_csv('./dataset/Oil_Historical_Data.csv')

data['Date']=pd.to_datetime(data['Date'])
data.isnull().sum()
date=data.Date.tolist()
data["Date"] = pd.to_datetime(data.Date,format="%b-%y")
len_of_date=len(data.Date)
start=data.Date[0]
end=data.Date[len_of_date-1]
new_dates = pd.date_range(start=end,end=start,freq='D')
data = data.set_index('Date')

model = load_model("./models/trained_lstm_model.h5")
# Define sequence length
sequence_length = 10

# Prepare data
scaler = MinMaxScaler()
scaled_data = scaler.fit_transform(data[['Price']])

# Streamlit UI
st.title("Oil Price Prediction")
input_date = st.date_input("Select a date:", datetime.now())
if st.button("Predict"):
    input_date = pd.Timestamp(input_date)  # Convert input_date to pandas.Timestamp
    input_index = (input_date - data.index[0]).days - sequence_length

    if input_index >= 0:
        input_sequence = scaled_data[input_index: input_index + sequence_length, 0]
        input_sequence = np.reshape(input_sequence, (1, sequence_length, 1))

        # Predict
        predicted_price = model.predict(input_sequence)
        predicted_price = scaler.inverse_transform(predicted_price)

        st.write("Predicted Price: $", predicted_price[0][0])
    else:
        st.write("Input date is too early for prediction.")

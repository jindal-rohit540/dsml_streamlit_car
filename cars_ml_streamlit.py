import pandas as pd
import streamlit as st
import datetime
import pickle

cars_df = pd.read_excel("./cars24.xlsx")

st.dataframe(cars_df)

## Encoding Categorical features

encode_dict = {
    "fuel_type": {'Diesel': 1, 'Petrol': 2, 'CNG': 3, 'LPG': 4, 'Electric': 5},
    "seller_type": {'Dealer': 1, 'Individual': 2, 'Trustmark Dealer': 3},
    "transmission_type": {'Manual': 1, 'Automatic': 2}
}


def model_pred(fuel_type, transmission_type, engine, seats):

    ## Load the model 
    with open("car_pred", 'rb') as file:
        reg_model = pickle.load(file)

        input_features = [[2019.0, 1, 1000, fuel_type, transmission_type, 19.70, engine, 86.30, seats]]

        return reg_model.predict(input_features)

col1, col2 = st.columns(2)

fuel_type = col1.selectbox("Select the fuel Type", ["Diesel", "Petrol", "CNG","Electric" ])

engine = col1.slider("Setthe engine power", 500, 5000, step = 100)

transmission_type = col2.selectbox("Select the transmission type", ["Manual", "Automatic"])

seats = col2.selectbox("Select the number of seats", [4,5,7,8,9,11])


if (st.button("Predict Price")):
    fuel_type_encoded = encode_dict['fuel_type'][fuel_type]

    transmission_type_encoded = encode_dict['transmission_type'][transmission_type]

    price = model_pred(fuel_type_encoded, transmission_type_encoded, engine, seats)
    st.text(price)
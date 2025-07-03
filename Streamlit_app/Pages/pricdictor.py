import pandas as pd
import streamlit as st
import numpy as np
import pickle
from sklearn.pipeline import Pipeline


st.set_page_config(page_title="Plotting Demo", page_icon="$")
st.title("Price prediction")

with open('dataframe(2).pkl', 'rb') as file:
    df = pickle.load(file)

with open('pipeline(2).pkl', 'rb') as file:
    pipeline = pickle.load(file)

st.dataframe(df)

st.header('Give specifications')

property_type = st.selectbox('property_type', ['house', 'flat'])

sector = st.selectbox('sector', list(set(df['sector'])))

super_built_up_area_sq_feet = st.number_input('super_built_up_area')

bedrooms = st.selectbox('bedRoom', list(set(df['bedRoom'].astype('int32'))))

bathrooms = st.selectbox('bathroom', list(set(df['bathroom'].astype('int32'))))

balcony = st.selectbox('balcony', list(set(df['balcony'].astype('int32'))))

Servant_room = st.selectbox('Servant Room', [0,1])

additional_room = st.selectbox('additional_room', [0,1, 2, 3, 4])

agePossession = st.selectbox('agePossession', (list(set(df['agePossession']))))

st.text("0 : unfurnished, 1 : semi-furnished, 2 : furnished")
furnish_type = st.selectbox('furnish_type', (list(set(df['furnish_type']))))

luxury_type = st.selectbox('luxury_type', (list(set(df['luxury_type']))))

floortype = st.selectbox('floortype', (list(set(df['floortype']))))

if st.button('Predict'):

    data = [[property_type, sector, bedrooms, bathrooms, balcony,
             agePossession, Servant_room, furnish_type, super_built_up_area_sq_feet, additional_room, floortype, luxury_type]]
    columns = ['F/H' , 'sector', 'bedRoom', 'bathroom', 'balcony',
               'agePossession', 'Servant Room', 'furnish_type', 'super_built_up_area', 'additional_room', 'floortype', 'luxury_type']

    new_df = pd.DataFrame(data, columns=columns)

    base_price = np.expm1(pipeline.predict(new_df))[0]
    low = base_price - 0.2
    high = base_price + 0.2

    st.text("The price of the flat is between {} Cr and {} Cr.".format(round(low,2), round(high,2)))
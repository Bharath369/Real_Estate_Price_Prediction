import streamlit as st

st.set_page_config(
    page_title="House Price Prediction",
    page_icon="🏠"
)

st.write("# welcome to Mumbai House Price prediction")

#st.sidebar.success("select")


import streamlit as st
import pickle
import numpy as np
import pandas as pd
#import sklearn
import plotly.express as px

#property_type	sector	bedRoom	bathroom	balcony	agePossession	built_up_area	servant room	store room	furnishing_type	luxury_category	floor_category

with open('df_1.pkl', 'rb') as file:
    df = pickle.load(file)

with open('pipeline_1.pkl', 'rb') as file:
    pipeline = pickle.load(file)

#st.dataframe(df)

st.header('Enter your inputs')

#Property_type

property_type = st.selectbox('Property Type', ['flat', 'house'])

#sector
Housing_Society = st.selectbox('Housing Society', sorted(df['sector'].unique().tolist()))

bedrooms = float(st.selectbox('Number of Bedroom', sorted(df['bedRoom'].unique().tolist())))

bathroom = float(st.selectbox('Number of Bathrooms', sorted(df['bathroom'].unique().tolist())))

balcony = st.selectbox('Balconies', sorted(df['balcony'].unique().tolist()))

property_age = st.selectbox('Property Age', sorted(df['agePossession'].unique().tolist()))

built_up_area = float(st.number_input('Built Up Area (sq ft)'))

Maid_Room = float(st.selectbox('Maid Room', [0.0, 1.0]))
storeroom = float(st.selectbox('Store Room', [0.0, 1.0]))

furnishing_type = st.selectbox('Furnishing Type', sorted(df['furnishing_type'].unique().tolist()))
luxury_category = st.selectbox('Luxury Category', sorted(df['luxury_category'].unique().tolist()))
floor_category = st.selectbox('Floor Category', sorted(df['floor_category'].unique().tolist()))

if st.button('Predict'):
    data = [
        [property_type, Housing_Society, bedrooms, bathroom, balcony, property_age, built_up_area, Maid_Room, storeroom,
         furnishing_type, luxury_category, floor_category]]
    columns = ['property_type', 'sector', 'bedRoom', 'bathroom', 'balcony',
               'agePossession', 'built_up_area', 'servant room', 'store room',
               'furnishing_type', 'luxury_category', 'floor_category']

    # Convert to DataFrame
    one_df = pd.DataFrame(data, columns=columns)

    #erleast.dataframe(one_df)

    Price = round(np.expm1(pipeline.predict(one_df))[0], 2)
    st.text("INR {} Cr".format(Price))

lat_long = pd.read_csv("properties lat price sqft.csv")

lat_long_group = lat_long.groupby('Sector').mean()[['Avg_price_per_sqft', 'Longitude', 'Latitude']]

fig = px.scatter_mapbox(lat_long_group, lat="Latitude", lon="Longitude", color="Avg_price_per_sqft",
                        color_continuous_scale=px.colors.cyclical.IceFire, size_max=15, zoom=10,
                        mapbox_style="carto-positron", width=1500, height=500)
st.plotly_chart(fig, use_container_width=True)

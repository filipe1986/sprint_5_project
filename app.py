import streamlit as st
import pandas as pd
import plotly.express as px

st.header('vehicles analysis')

df = pd.read_csv("vehicles.csv")

hist_checkbox = st.checkbox('Create histogram')

if hist_checkbox: # with button click
    st.write('Creating an histogram to the odometer column')

    fig = px.histogram(df, x="odometer")

    st.plotly_chart(fig, use_container_width = True)

plotly_express = st.checkbox('Create a scatter chart price vs odometer')

if plotly_express: # if clicked
    st.write('Creating a scatter chart')

    fig_01 = px.scatter(df, x='odometer', y='price')

    st.plotly_chart(fig_01)


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


numeric_columns = df.select_dtypes(include=['number']).columns.tolist()

st.subheader('Chose the columns to view')

# creating a dictionary to stock the checkboxes
selected_columns = {}

# Criating a checkbox for each numeric column
for column in numeric_columns:
    selected_columns[column] = st.checkbox(f'Show {column}')

# Check the selected columns
chosen_columns = [col for col, selected in selected_columns.items() if selected]

if len(chosen_columns) >= 2:
    #If at least 2 columns was chose, cheate scatter plot
    x_col = chosen_columns[0]
    y_col = chosen_columns[1]

    fig = px.scatter(df, x=x_col, y=y_col)
    st.plotly_chart(fig, use_container_width=True)
elif len(chosen_columns) == 1:
    # If only one column was chose, create an histogram again
    fig = px.histogram(df, x=chosen_columns[0])
    st.plotly_chart(fig, use_container_width=True)

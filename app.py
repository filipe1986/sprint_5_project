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

st.title('Car data viewer')

# Extracting columns for comparison (excluding price itself)
compare_columns = [col for col in df.columns if col != "price"]

# User selection
selected_features = st.multiselect("Select columns to compare against Price:",
                                   options=compare_columns,
                                   default = ["model_year", "odometer"],)

# Generagin dynamic charts
if selected_features:
    for feature in selected_features:
        st.subheader(f"Price vs {feature.replace('_', ' ').title()}")

        # Check if the column is numeric or categorical to choose the best chart
        if df[feature].dtype in ["int64", "float64"] and len(df[feature].unique() > 10:
            # Use scatter chart for continuous numbers
            st.scatter_chart(df, x=feature, y="price")
        else:
            # Use bar chart for categories or discrete numbers
            st.bar_chart(df, x=feature, y="price")
else:
    st.warning("Please, select at least one column")
        )

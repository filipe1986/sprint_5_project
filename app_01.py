import numpy as np
import pandas as pd
import streamlit as st

# 1. Create a dummy DataFrame based on your columns
np.random.seed(42)
n_rows = 100
data = {
    "price": np.random.randint(5000, 50000, n_rows),
    "model_year": np.random.randint(2000, 2024, n_rows),
    "model": np.random.choice(["Camry", "Civic", "F-150"], n_rows),
    "condition": np.random.choice(
        ["new", "excellent", "good", "fair"], n_rows
    ),
    "cylinders": np.random.choice([4, 6, 8], n_rows),
    "fuel": np.random.choice(["gas", "diesel", "hybrid"], n_rows),
    "odometer": np.random.randint(1000, 200000, n_rows),
    "transmission": np.random.choice(["automatic", "manual"], n_rows),
    "type": np.random.choice(["sedan", "SUV", "truck"], n_rows),
    "paint_color": np.random.choice(["white", "black", "silver"], n_rows),
    "is_4wd": np.random.choice([0, 1], n_rows),
    "date_posted": pd.date_range("2025-01-01", periods=n_rows),
    "days_listed": np.random.randint(1, 60, n_rows),
}
df = pd.DataFrame(data)

st.title("🚗 Car Price Analysis Dashboard")

# 2. Extract columns for comparison (excluding price itself)
compare_columns = [col for col in df.columns if col != "price"]

# 3. User selection
selected_features = st.multiselect(
    "Select columns to compare against Price (Y-axis):",
    options=compare_columns,
    default=["model_year", "odometer"],  # Default starting visuals
)

# 4. Generate dynamic charts
if selected_features:
    for feature in selected_features:
        st.subheader(f"Price vs {feature.replace('_', ' ').title()}")

        # Check if the column is numeric or categorical to choose the best chart
        if df[feature].dtype in ["int64", "float64"] and len(
            df[feature].unique()
        ) > 10:
            # Use scatter chart for continuous numbers (e.g., odometer)
            st.scatter_chart(df, x=feature, y="price")
        else:
            # Use bar chart for categories or discrete numbers (e.g., condition, cylinders)
            st.bar_chart(df, x=feature, y="price")

else:
    st.warning("Please select at least one column from the dropdown above.")

import streamlit as st
import pandas as pd
import plotly.express as px
from pathlib import Path

st.set_page_config(page_title="Vehicles Analysis", layout="wide")

@st.cache_data
def load_data(csv_path: str | Path) -> pd.DataFrame:
    df = pd.read_csv(csv_path)
    # Caso existam colunas com datas ou numéricas como strings,
    # faça o parsing aqui.
    df['date_posted'] = pd.to_datetime(df['date_posted'])
    return df

DATA_PATH = "vehicles.csv"
df = load_data(DATA_PATH)

# side bar
st.sidebar.header("Visualization")

show_hist   = st.sidebar.checkbox("Histogram (odometer)")
show_scatter = st.sidebar.checkbox("Scatter: price × odmeter")

if show_hist:
    # bins number choice
    bins = st.sidebar.slider("bins number",
                             min_value=10, max_value=100, value=50, step=5)

if show_scatter:
    # to color by option
    default_color = "condition" if "condition" in df.columns else None
    color_col = st.sidebar.selectbox("to color scatter by:",
                                     options=[None] + list(df.columns),
                                     index=0 if default_color is None else
                                     list(df.columns).index(default_color)+1)

st.title("🚗 Vehicles Analysis")

# generatin the charts
def plot_histogram(data: pd.DataFrame, nbins: int):
    fig = px.histogram(data, x="odometer", nbins=nbins,
                       title=f"odometer distribution (bins={nbins})")
    fig.update_layout(margin=dict(l=20, r=20, t=60, b=40))
    st.plotly_chart(fig, use_container_width=True)

def plot_scatter(data: pd.DataFrame, color: str | None):
    fig = px.scatter(data, x="odometer", y="price",
                     color=color,
                     title="price × odometer"
                           + (f" (cor = {color})" if color else ""))
    fig.update_layout(margin=dict(l=20, r=20, t=60, b=40))
    st.plotly_chart(fig, use_container_width=True)

# Dispatcher
if show_hist:
    st.subheader("odometer histogram")
    plot_histogram(df, bins)

if show_scatter:
    st.subheader("Scatter: preço × odômetro")
    plot_scatter(df, color_col)

if not (show_hist or show_scatter):
    st.info("☝️ Use the side bar to choice the charts.")

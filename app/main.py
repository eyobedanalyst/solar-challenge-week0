# app/main.py
import sys
import os

# Ensure root folder is in Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))





import streamlit as st
from app.utils import load_data, boxplot_metric
import pandas as pd



st.set_page_config(page_title="Solar Data Dashboard", layout="wide")

st.title("☀️ Solar Radiation Dashboard")
st.markdown("Visualize solar radiation data interactively across different countries.")

# Sidebar controls
country = st.sidebar.selectbox("Select Country", ["Benin", "Togo", "SierraLeone"])
metric = st.sidebar.selectbox("Select Metric", ["GHI", "DNI", "DHI"])

# Load data
df = load_data(country)

# Display summary
st.subheader(f"Summary Statistics for {country}")
st.dataframe(df.describe()[[metric]])

# Boxplot visualization
fig = boxplot_metric(df, metric, country)
st.plotly_chart(fig, use_container_width=True)

# Top regions table (if 'region' column exists)
if "region" in df.columns:
    st.subheader("Top Regions by Average GHI")
    region_summary = (
        df.groupby("region")[metric].mean().sort_values(ascending=False).reset_index()
    )
    st.dataframe(region_summary.head(5))
else:
    st.info("No region data available for this dataset.")

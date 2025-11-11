# app/utils.py
import pandas as pd
import plotly.express as px

def load_data(country):
    """Load cleaned data for the given country."""
    try:
        df = pd.read_csv(f"data/{country.lower()}_clean.csv")
    except FileNotFoundError:
        df = pd.read_csv(f"sample_data/{country.lower()}_sample.csv")
    return df

def boxplot_metric(df, metric, country):
    """Create a boxplot for a selected metric."""
    fig = px.box(df, y=metric, title=f"{metric} Distribution - {country}")
    fig.update_layout(template="plotly_white")
    return fig

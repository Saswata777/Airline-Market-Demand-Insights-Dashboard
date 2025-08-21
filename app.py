import streamlit as st
from datetime import datetime
from dateutil.relativedelta import relativedelta
import pandas as pd

# Local imports
from utils.constants import CITIES, ROUTES
from utils.data_loader import load_trends
from utils.summarizer import summarize_with_ai
from utils.charts import plot_route_trends

# ---------------- Streamlit Config ----------------
st.set_page_config(page_title="Airline Demand Insights", page_icon="✈️", layout="wide")

st.title("✈️ Airline Booking Market Demand – Insights Dashboard")
st.caption("MVP using free data sources: Google Trends (demand proxy) and optional OpenSky (traffic proxy)")

# ---------------- Sidebar ----------------
with st.sidebar:
    st.header("Filters")
    au_cities = list(CITIES.keys())
    city_multiselect = st.multiselect("Cities of interest", au_cities, default=au_cities)

    default_start = (datetime.utcnow() - relativedelta(months=6)).date()
    default_end = datetime.utcnow().date()
    date_range = st.date_input("Date range", (default_start, default_end))

    geo = st.selectbox("Geo (Google Trends)", ["AU", "US", "GB", "NZ", "Worldwide"], index=0)
    if geo == "Worldwide":
        geo = ""

    st.markdown("---")
    use_ai = st.button("✨ Summarize with AI")

# ---------------- Keywords ----------------
keywords = [f"{a} to {b} flights" for (a, b) in ROUTES if a in city_multiselect and b in city_multiselect]
if not keywords:
    st.warning("Select at least two cities to evaluate routes.")
    st.stop()

# ---------------- Fetch Google Trends ----------------
start_date, end_date = date_range
timeframe = f"{start_date} {end_date}"
with st.spinner("Fetching Google Trends data..."):
    df_trends = load_trends(keywords, geo, timeframe)

if df_trends.empty:
    st.error("No data returned by Google Trends for these filters. Try changing date range or geo.")
    st.stop()

# ---------------- Aggregate ----------------
route_daily = df_trends.groupby(['route', 'date'], as_index=False)['interest'].mean()

# ---------------- KPIs ----------------
kpi = route_daily.groupby('route')['interest'].mean().sort_values(ascending=False).head(5)
col1, col2, col3 = st.columns(3)
col1.metric("Routes tracked", f"{route_daily['route'].nunique()}")
col2.metric("Date span", f"{route_daily['date'].min().date()} → {route_daily['date'].max().date()}")
col3.metric("Top route (avg)", f"{kpi.index[0]} ({kpi.iloc[0]:.1f})")

# ---------------- Chart ----------------
select_routes = st.multiselect(
    "Select routes to visualize",
    options=sorted(route_daily['route'].unique()),
    default=list(kpi.index)[:3]
)
fig = plot_route_trends(route_daily, select_routes)
st.plotly_chart(fig, use_container_width=True)

# ---------------- Latest snapshot ----------------
latest_date = route_daily['date'].max()
latest = route_daily[route_daily['date'] == latest_date].sort_values('interest', ascending=False)
st.write(f"#### Latest snapshot — {latest_date.date()}")
st.dataframe(latest.reset_index(drop=True))

# ---------------- Insights ----------------
st.write("### Insights")
if use_ai:
    summary = summarize_with_ai(route_daily)
    st.text_area("AI-generated summary", value=summary, height=220)

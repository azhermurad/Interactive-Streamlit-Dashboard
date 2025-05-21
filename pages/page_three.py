import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import altair as alt
import plotly.express as px

# Load dataset
df = pd.read_csv("dataset/palmerpenguins_extended.csv")
df.dropna(inplace=True)  # Remove missing values

# Sidebar manual inputs
sex = st.sidebar.text_input("Enter Sex (e.g., male, female or 'all')", "female").strip().lower()
island = st.sidebar.text_input("Enter Island (e.g., Biscoe, Dream, Torgersen or 'all')", "Dream").strip().lower()
species_input = st.sidebar.text_input("Enter Species (e.g., Adelie, Chinstrap, Gentoo)", "Chinstrap").strip().lower()

# Apply global filters
filtered_df_global = df.copy()
if sex and sex != 'all':
    filtered_df_global = filtered_df_global[filtered_df_global['sex'].str.lower() == sex]
if island and island != 'all':
    filtered_df_global = filtered_df_global[filtered_df_global['island'].str.lower() == island]

# === Line Chart ===
st.subheader("Line Chart of Bill Length & Bill Depth")

selected_year = st.slider("Select a year to filter (or view all years)", min_value=2021, max_value=2025, step=1)

# Further filter for year and species
filtered_df = filtered_df_global[filtered_df_global['year'] == selected_year]
if species_input:
    filtered_df = filtered_df[filtered_df['species'].str.lower() == species_input]

if not filtered_df.empty:
    st.line_chart(filtered_df[['bill_length_mm', 'bill_depth_mm']])
else:
    st.warning("No data available for the selected filters.")

# === Two Columns: Diet Distribution and Life Stage Area Chart ===
col1, col2 = st.columns(2)

with col1:
    st.subheader("Diet Distribution by Species")
    diet_species = filtered_df_global.groupby(['species', 'diet']).size().reset_index(name='count')

    fig_stacked = px.bar(
        diet_species,
        x='species',
        y='count',
        color='diet',
        title="Diet Types per Species",
        barmode='stack',
        template="plotly_white"
    )
    st.plotly_chart(fig_stacked, use_container_width=True)

    st.markdown(
        "<p style='font-family: Arial, sans-serif; font-size: 14px; color: gray; margin-top: 10px;'>"
        "This bar graph illustrates how diet types are distributed among different penguin species "
        "based on your filters."
        "</p>",
        unsafe_allow_html=True
    )

with col2:
    st.subheader("Avg Measurements by Life Stage")
    life_stage_avg = df.groupby('life_stage')[['bill_length_mm', 'bill_depth_mm', 'flipper_length_mm']].mean()
    st.area_chart(life_stage_avg)

    st.markdown(
        "<p style='font-family: Arial, sans-serif; font-size: 14px; color: gray; margin-top: 10px;'>"
        "This area chart shows average values for key measurements across penguin life stages."
        "</p>",
        unsafe_allow_html=True
    )

# === Scatter Plot Based on Diet and Species ===
st.subheader("Diet Comparison")

diet_avg = filtered_df_global.groupby(['diet', 'species']).agg({
    'bill_length_mm': 'mean',
    'bill_depth_mm': 'mean',
    'flipper_length_mm': 'mean',
    'body_mass_g': 'mean'
}).reset_index()

fig_scatter = px.scatter(
    diet_avg,
    x='bill_length_mm',
    y='bill_depth_mm',
    color='diet',
    symbol='species',
    size='body_mass_g',
    hover_data=['species', 'flipper_length_mm', 'body_mass_g'],
    title='Diet Comparison: Bill Length vs Bill Depth by Species',
    template='plotly_white'
)

st.plotly_chart(fig_scatter, use_container_width=True)

st.markdown(
    "<p style='font-family: Arial, sans-serif; font-size: 14px; color: gray;'>"
    "Scatter plot showing comparison of bill length and bill depth for different diets and species. "
    "Size of points indicates average body mass. Data is filtered by selected sex and island."
    "</p>",
    unsafe_allow_html=True
)

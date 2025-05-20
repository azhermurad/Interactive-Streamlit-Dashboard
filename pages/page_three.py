import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import altair as alt
import plotly.express as px



df = pd.read_csv("dataset/palmerpenguins_extended.csv")
df.dropna(inplace=True) # drop null value 




st.subheader("Line Chart of Bill Length & Bill Depth")

  # Step 3: Optional year filter using slider
selected_year = st.slider("Select a year to filter (or view all years)", min_value=2021, max_value=2025, step=1)
sex = st.sidebar.text_input("Enter Sex (e.g., male, female)", "female").strip().lower()
species = st.sidebar.text_input("Enter Species (e.g., Adelie, Chinstrap, Gentoo)", "Chinstrap").strip().lower()
   # Filter data by selected year
filtered_df = df[df['year'] == selected_year]

if sex:
    filtered_df = filtered_df[filtered_df['sex'].str.lower() == sex]
if species:
    filtered_df = filtered_df[filtered_df['species'].str.lower() == species]

# Line chart
if not filtered_df.empty:
    st.line_chart(filtered_df[['bill_length_mm', 'bill_depth_mm']])
else:
        st.warning("No data available for the selected filters.")


# Add Column 
col1, col2, = st.columns(2)
with col1:
    st.subheader("Diet Distribution by Species ")
    diet_species = df.groupby(['species', 'diet']).size().reset_index(name='count')
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
        "This bar graph illustrates how diet types are distributed among different penguin species."
        "</p>",
        unsafe_allow_html=True
    )

    
with col2:
    life_stage_avg = df.groupby('life_stage')[['bill_length_mm', 'bill_depth_mm', 'flipper_length_mm']].mean()

    st.subheader("Avg Measurements by Life Stage")
    st.area_chart(life_stage_avg)
    
    st.markdown(
    "<p style='font-family: Arial, sans-serif; font-size: 14px; color: gray; margin-top: 10px;'>"
    "This area chart shows average values for key measurements across penguin life stages."
    "</p>",
    unsafe_allow_html=True
)



 
        
    








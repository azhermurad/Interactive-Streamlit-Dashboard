import streamlit as st
import pandas as pd
import plotly.express as px

# Load and clean dataset
df = pd.read_csv("dataset/palmerpenguins_extended.csv")
df.dropna(inplace=True)

st.title("Life Stage & Health Trends of Penguins")

# SECTION 1: Life Stage Analysis
st.subheader("Life Stage Distribution")

# User filters for species and island
col_filter1, col_filter2 = st.columns(2)
with col_filter1:
    selected_species_ls = st.selectbox("Select Species", sorted(df["species"].unique()))
with col_filter2:
    selected_island_ls = st.selectbox("Select Island", sorted(df["island"].unique()))

filtered_ls_df = df[(df["species"] == selected_species_ls) & (df["island"] == selected_island_ls)]

# Plot 1 and 2 side by side
col1, col2 = st.columns(2)

# Plot 1: Donut chart
with col1:
    if not filtered_ls_df.empty:
        stage_counts = filtered_ls_df["life_stage"].value_counts().reset_index()
        stage_counts.columns = ["life_stage", "count"]
        fig1 = px.pie(
            stage_counts,
            names="life_stage",
            values="count",
            title=f"Life Stage of {selected_species_ls} on {selected_island_ls}",
            hole=0.4,
            template="plotly_white"
        )
        st.plotly_chart(fig1, use_container_width=True)
        st.caption("This donut chart shows the distribution of life stages for the selected species on the chosen island.")
    else:
        st.warning(f"No data for {selected_species_ls} on {selected_island_ls}.")

# Plot 2: Area chart
with col2:
    island_df = df[df["island"] == selected_island_ls]
    if not island_df.empty:
        species_stage_counts = island_df.groupby(["species", "life_stage"]).size().reset_index(name="count")
        fig2 = px.area(
            species_stage_counts,
            x="life_stage",
            y="count",
            color="species",
            title=f"Life Stages of All Species on {selected_island_ls}",
            template="plotly_white"
        )
        st.plotly_chart(fig2, use_container_width=True)
        st.caption("This area chart compares life stages of all species on the selected island.")
    else:
        st.warning(f"No data for island {selected_island_ls}.")

# SECTION 2: Health Metric Trends
st.subheader("Health Metric Trends Over Time")

# Plot 3 and 4 filters
health_years = sorted(df["year"].unique())
selected_year = st.select_slider("Select a Year", options=health_years)
selected_species_health = st.selectbox("Select Species for Health Trend", sorted(df["species"].unique()))

filtered_year_species_df = df[df["species"] == selected_species_health]

col3, col4 = st.columns(2)

# Plot 3: Line graph showing health trend over time
with col3:
    if not filtered_year_species_df.empty:
        health_over_time = (
            filtered_year_species_df.groupby(["year", "health_metrics"])
            .size()
            .reset_index(name="count")
        )
        fig3 = px.line(
            health_over_time,
            x="year",
            y="count",
            color="health_metrics",
            markers=True,
            title=f"Health Trends of {selected_species_health} Over the Years",
            template="plotly_white"
        )
        st.plotly_chart(fig3, use_container_width=True)
        st.caption("This line chart shows how health status of the selected species has changed over the years.")
    else:
        st.warning("No health data available for the selected species.")

# Plot 4: Health by gender for that species in selected year
with col4:
    filtered_year_df = filtered_year_species_df[filtered_year_species_df["year"] == selected_year]
    if not filtered_year_df.empty:
        gender_health = filtered_year_df.groupby(["sex", "health_metrics"]).size().reset_index(name="count")
        fig4 = px.bar(
            gender_health,
            x="sex",
            y="count",
            color="health_metrics",
            barmode="group",
            title=f"Health of Male vs Female {selected_species_health} in {selected_year}",
            template="plotly_white"
        )
        st.plotly_chart(fig4, use_container_width=True)
        st.caption("This bar chart compares the health of male and female penguins for the selected species in the selected year.")
    else:
        st.warning("Not enough gender-specific health data for this species in the selected year.")

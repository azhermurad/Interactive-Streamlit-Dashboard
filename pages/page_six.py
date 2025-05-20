import streamlit as st
import pandas as pd
import plotly.express as px

# Load and clean dataset
df = pd.read_csv("dataset/palmerpenguins_extended.csv")
df.dropna(inplace=True)

st.title("Life Stage & Health Trends of Penguins")

# Section 1: Life Stage Analysis
st.subheader("Life Stage Distribution")

# Filter selection
col_filter1, col_filter2 = st.columns([1, 1])
with col_filter1:
    selected_species_ls = st.selectbox("Select Species", sorted(df["species"].unique()))
with col_filter2:
    selected_island_ls = st.selectbox("Select Island", sorted(df["island"].unique()))

# Filtered dataframe for Plot 1
filtered_ls_df = df[(df["species"] == selected_species_ls) & (df["island"] == selected_island_ls)]

# Create two plots side by side
col1, col2 = st.columns(2)

with col1:
    if not filtered_ls_df.empty:
        stage_counts = filtered_ls_df["life_stage"].value_counts().reset_index()
        stage_counts.columns = ["life_stage", "count"]  # Rename for clarity

        fig1 = px.pie(
            stage_counts,
            names="life_stage",
            values="count",
            title=f"Life Stage Distribution of {selected_species_ls} on {selected_island_ls}",
            template="plotly_white",
            color_discrete_sequence=px.colors.qualitative.Set3,
            hole=0.4  # Makes it a donut chart
        )
        st.plotly_chart(fig1, use_container_width=True)
        st.caption("This donut chart shows the proportion of life stages for the selected species on the chosen island.")
    else:
        st.warning(f"No data for {selected_species_ls} on {selected_island_ls}.")



with col2:
    island_df = df[df["island"] == selected_island_ls]
    if not island_df.empty:
        stage_species_counts = island_df.groupby(["life_stage", "species"]).size().reset_index(name="count")

        fig2 = px.area(
            stage_species_counts,
            x="life_stage",
            y="count",
            color="species",
            line_group="species",
            title=f"Life Stages of All Species on {selected_island_ls}",
            template="plotly_white"
        )
        st.plotly_chart(fig2, use_container_width=True)
        st.caption("This area chart compares life stage distributions across species on the selected island.")
    else:
        st.warning(f"No data for island {selected_island_ls}.")


# Section 2: Health Metric Trends
st.subheader("Health Metric Trends Over Years")

# Species selection for health analysis
selected_species_health = st.selectbox("Select Species for Health Trend", sorted(df["species"].unique()))

# Filter dataframe
health_df = df[df["species"] == selected_species_health]

col3, col4 = st.columns(2)

# Plot 3: Health trend over years
with col3:
    if not health_df.empty:
        health_by_year = health_df.groupby(["year", "health_metrics"]).size().reset_index(name="count")
        fig3 = px.bar(
            health_by_year,
            x="year",
            y="count",
            color="health_metrics",
            barmode="group",
            title=f"Health Metrics of {selected_species_health} Over the Years",
            template="plotly_white"
        )
        st.plotly_chart(fig3, use_container_width=True)
        st.caption("Shows how health metrics of the selected species change over the years.")
    else:
        st.warning(f"No health data available for {selected_species_health}.")

# Plot 4: Health by gender over years
with col4:
    gender_health_df = health_df.copy()
    if not gender_health_df.empty:
        health_gender_year = gender_health_df.groupby(["year", "sex", "health_metrics"]).size().reset_index(name="count")
        fig4 = px.bar(
            health_gender_year,
            x="year",
            y="count",
            color="health_metrics",
            facet_col="sex",
            barmode="group",
            title=f"Health of Male vs Female {selected_species_health} Over Years",
            template="plotly_white"
        )
        st.plotly_chart(fig4, use_container_width=True)
        st.caption("Compares the health status of male and female penguins for the selected species over time.")
    else:
        st.warning("Not enough gender-specific health data for this species.")

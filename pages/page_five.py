import streamlit as st
import pandas as pd
import plotly.express as px

# Load and clean dataset
df = pd.read_csv("dataset/palmerpenguins_extended.csv")
df.dropna(inplace=True)

st.title(" Island-based Analysis of Penguins")

col1, col2 = st.columns(2)

with col1:
    # Filters side by side on one row inside col1
    filter1, filter2 = st.columns([1,1])
    with filter1:
        selected_island = st.radio("Select Island", sorted(df["island"].unique()), key="island_radio")
    with filter2:
        selected_species = st.radio("Select Species", sorted(df["species"].unique()), key="species_radio")

    # Show plot 1 below filters
    filtered_df1 = df[(df["island"] == selected_island) & (df["species"] == selected_species)]

    if filtered_df1.empty:
        st.warning(f"No data for species '{selected_species}' on island '{selected_island}'.")
    else:
        fig1 = px.box(
            filtered_df1,
            x="sex",
            y="body_mass_g",
            color="sex",
            title=f"Body Mass by Gender - {selected_species} on {selected_island}",
            template="plotly_white",
            color_discrete_sequence=["#1f77b4", "#ff7f0e"]
        )
        st.plotly_chart(fig1, use_container_width=True)

with col2:
    # Plot 2 filter and plot stacked vertically
    selected_islands = st.multiselect(
        "Compare Body Mass Across Islands (All Species)",
        options=sorted(df["island"].unique()),
        default=sorted(df["island"].unique())[:2]
    )
    filtered_df2 = df[df["island"].isin(selected_islands)]

    if filtered_df2.empty:
        st.warning("No data available for selected islands.")
    else:
        fig2 = px.box(
            filtered_df2,
            x="island",
            y="body_mass_g",
            color="island",
            title="Body Mass Comparison Across Islands",
            template="plotly_white",
            color_discrete_sequence=px.colors.qualitative.Set2
        )
        st.plotly_chart(fig2, use_container_width=True)



# Section 2: Health Metric Trends
st.subheader("Health Metric Trends (Filtered by Year and Species)")

# Filters
selected_year = st.slider("Select Year", min_value=int(df["year"].min()), max_value=int(df["year"].max()), step=1)
selected_species = st.text_input("Enter Species (e.g., Adelie, Chinstrap, Gentoo)", "Adelie").strip().lower()

# Filter data
filtered_df = df[df["year"] == selected_year]
filtered_df = filtered_df[filtered_df["species"].str.lower() == selected_species]

col3, col4 = st.columns(2)

# Plot 3: Health metrics distribution in selected year for selected species
with col3:
    if not filtered_df.empty:
        health_counts = filtered_df["health_metrics"].value_counts().reset_index()
        health_counts.columns = ["health_metrics", "count"]

        fig3 = px.pie(
            health_counts,
            names="health_metrics",
            values="count",
            hole=0.5,  # Donut chart
            title=f"Health Metrics for {selected_species.capitalize()} in {selected_year}",
            template="plotly_white"
        )
        st.plotly_chart(fig3, use_container_width=True)
        st.caption("Donut chart showing distribution of health metrics for the selected species in the chosen year.")
    else:
        st.warning("No data available for the selected species and year.")

# Plot 4: Health by gender for selected species and year
with col4:
    if not filtered_df.empty:
        gender_health = filtered_df.groupby(["sex", "health_metrics"]).size().reset_index(name="count")

        fig4 = px.bar(
            gender_health,
            x="sex",
            y="count",
            color="health_metrics",
            barmode="group",
            title=f"Health Comparison by Gender - {selected_species.capitalize()} ({selected_year})",
            template="plotly_white"
        )
        st.plotly_chart(fig4, use_container_width=True)
        st.caption("Grouped bar chart comparing health status of male and female penguins.")
    else:
        st.warning("No gender-specific data available for the selected filters.")

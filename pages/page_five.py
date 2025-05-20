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



# 3 & 4. Body mass and diet trends over time
st.subheader("Trends Over the Years")

filter_col, _ = st.columns([1, 5])  # 1:5 ratio to make the filter column smaller
with filter_col:
    selected_species_for_trend = st.selectbox(
        "Select Species to View Trends", 
        sorted(df["species"].unique())
    )

col3, col4 = st.columns(2)

with col3:
    trend_df = df[df["species"] == selected_species_for_trend]
    avg_mass_per_year = trend_df.groupby(["year", "sex"])["body_mass_g"].mean().reset_index()

    fig3 = px.line(
        avg_mass_per_year,
        x="year",
        y="body_mass_g",
        color="sex",
        markers=True,
        title=f"Average Body Mass Over Years - {selected_species_for_trend}",
        template="plotly_white"
    )
    st.plotly_chart(fig3, use_container_width=True)

with col4:
    diet_df = df[df["species"] == selected_species_for_trend]
    diet_per_year = diet_df.groupby(["year", "diet"]).size().reset_index(name="count")

    fig4 = px.bar(
        diet_per_year,
        x="year",
        y="count",
        color="diet",
        title=f"Diet Distribution Over Years - {selected_species_for_trend}",
        barmode="stack",
        template="plotly_white"
    )
    st.plotly_chart(fig4, use_container_width=True)

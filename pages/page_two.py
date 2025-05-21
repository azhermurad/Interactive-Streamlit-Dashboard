import streamlit as st
import pandas as pd
import altair as alt
import plotly.express as px

st.markdown("""
    <h1 style='text-align: center; color: white; font-family: Arial; font-weight: bold;'>
        Palmer Penguins - Detailed Analysis
    </h1>
""", unsafe_allow_html=True)

# Load dataset
df = pd.read_csv("dataset/palmerpenguins_extended.csv")
df.dropna(inplace=True) # drop null value 

# Filters
f1, f2, f3, f4 = st.columns(4)

with f1:
    species_filter = st.selectbox("🐧 Species", options=["All"] + sorted(df["species"].unique()))

with f2:
    island_filter = st.selectbox("🏝️ Island", options=["All"] + sorted(df["island"].unique()))

with f3:
    year_filter = st.selectbox("📅 Year", options=["All"] + sorted(df["year"].unique()))

with f4:
    sex_filter = st.selectbox("🚻 Gender", options=["All"] + sorted(df["sex"].dropna().unique()))

# Apply filters
filtered_df = df.copy()
if species_filter != "All":
    filtered_df = filtered_df[filtered_df["species"] == species_filter]
if island_filter != "All":
    filtered_df = filtered_df[filtered_df["island"] == island_filter]
if year_filter != "All":
    filtered_df = filtered_df[filtered_df["year"] == year_filter]
if sex_filter != "All":
    filtered_df = filtered_df[filtered_df["sex"] == sex_filter]

# Summary statistics
with st.expander("📊 Summary Statistics of Numerical Columns"):
    st.dataframe(filtered_df.describe(), use_container_width=True)

if filtered_df.empty:
    st.warning("⚠️ No data available for the selected filters. Please adjust your selections.")
else:
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Relationship With Body Mass")
        bil_value = st.selectbox(
            "Select feature to compare vs Body Mass",
            ("bill_length_mm", "bill_depth_mm", "flipper_length_mm"),
        )
        c = (
            alt.Chart(filtered_df)
            .mark_circle()
            .encode(
                x=bil_value,
                y="body_mass_g",
                color="species",
                tooltip=[bil_value, "body_mass_g"]
            )
            .properties(height=500)
            .configure_axis(labelFontSize=14, titleFontSize=16)
        )
        st.altair_chart(c)
        st.markdown(
            "<p style='font-family: Arial, sans-serif; font-size: 14px; color: gray; margin-top: 10px;'>"
            "This scatter plot explores how selected penguin features relate to their body mass across species."
            "</p>",
            unsafe_allow_html=True
        )

    with col2:
        st.subheader("Correlation Between Features")
        corr_matrix = filtered_df.corr(numeric_only=True)
        fig = px.imshow(
            corr_matrix,
            text_auto=True,
            color_continuous_scale='RdBu_r',
        )
        fig.update_layout(
            title={
                'text': "Correlation Between Features",
                'x': 0.5,
                'xanchor': 'center',
                'font': {'size': 24, 'family': 'Arial', 'color': 'white'}
            },
            width=600,
            height=600
        )
        st.plotly_chart(fig, use_container_width=True)
        st.markdown(
            "<p style='font-family: Arial, sans-serif; font-size: 14px; color: gray; margin-top: 10px;'>"
            "This heatmap visualizes the correlation strength between various numerical features in the dataset."
            "</p>",
            unsafe_allow_html=True
        )

    st.subheader("Penguins Body Mass by Species")
    fig_box = px.box(
    filtered_df,
    x='species',
    y='body_mass_g',
    color='species',
    template="plotly_white"
)
    st.plotly_chart(fig_box, use_container_width=True)
    st.markdown(
        "<p style='font-family: Arial, sans-serif; font-size: 14px; color: gray; margin-top: 10px;'>"
        "This is a comparison of body mass distribution across different penguin species using box plots."
        "</p>",
        unsafe_allow_html=True
    )

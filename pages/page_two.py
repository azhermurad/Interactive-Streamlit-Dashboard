import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import altair as alt
import plotly.express as px


st.markdown("""
    <h1 style='text-align: center; color: white; font-family: Arial; font-weight: bold;'>
        Palmer Penguins Dataset
    </h1>
""", unsafe_allow_html=True)


df = pd.read_csv("dataset/palmerpenguins_extended.csv")
df.dropna(inplace=True) # drop null value 
st.write(df.head())
print(df.corr(numeric_only=True))


st.markdown("<br>", unsafe_allow_html=True)
st.markdown("<br>", unsafe_allow_html=True)
st.markdown("<br>", unsafe_allow_html=True)



# Add Column 
col1, col2, = st.columns(2)
with col1:
    bil_value = st.selectbox(
    "Check relationship between Bill Length/ Bill Depth/flipper_lenght_mm   vs  Body Mass",
    ("bill_length_mm", "bill_depth_mm","flipper_length_mm"),
)
    st.write('')
    c = (
   alt.Chart(df)
   .mark_circle()
   .encode(
       x=bil_value, y="body_mass_g", color="species", tooltip=[bil_value, "body_mass_g"])
).properties(
        height=500,
    ).configure_axis(
        labelFontSize=14,
        titleFontSize=16
    )

    st.altair_chart(c)
   




    
with col2:
#    we have to add seaborn histogram for bodymass or bill length to check the distribution of it
    corr_matrix = df.corr(numeric_only=True)
# Plotly heatmap
    fig = px.imshow(
        corr_matrix,
        text_auto=True,  # shows values inside cells
        color_continuous_scale='RdBu_r',
)

    # Center the title
    fig.update_layout(
        title={
        'text': "Correlation Between Features",
        'x': 0.5,
        'xanchor': 'center',
        'font': {
            'size': 24,  # Increase this value for bigger title
            'family': 'Arial',
            'color': 'white'
        }
    },
        width=600,
        height=600
    )

    # Show in Streamlit
    st.plotly_chart(fig, use_container_width=True)


 
        
    



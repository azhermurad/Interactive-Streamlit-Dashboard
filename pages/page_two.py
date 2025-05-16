import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import altair as alt


df = pd.read_csv("dataset/palmerpenguins_extended.csv")
df.dropna(inplace=True) # drop null value 


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
        height=600,
        title=alt.TitleParams(
            text=f'Relationship between {bil_value} vs body_mass_g',
            align='center',
            fontSize=20,
            font='Arial',
            anchor='middle',
            # color="orange"
        )
    ).configure_axis(
        labelFontSize=14,
        titleFontSize=16
    )

    st.altair_chart(c)
   




    
with col2:
#    we have to add seaborn histogram for bodymass or bill length to check the distribution of it
    pass


 
        
    



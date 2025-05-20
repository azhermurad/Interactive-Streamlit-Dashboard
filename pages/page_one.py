import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import altair as alt

st.markdown("""
    <h1 style='text-align: center; color: white; font-family: Arial; font-weight: bold; font-weight: bold;'>
        Palmer Penguins Dataset
    </h1>
""", unsafe_allow_html=True)


# Custom image with height
st.markdown(
    """
    <div style='text-align: center;'>
        <img src='https://i.imgur.com/5rtbtpN.png' style='height:190px;border-radius: 1rem;' />
    </div>
    """,
    unsafe_allow_html=True
)

st.write("") # spacing 

# read csv
df = pd.read_csv("dataset/palmerpenguins_extended.csv")
df.dropna(inplace=True) # drop null value 


# Dataset info in an expandable section
with st.expander("📘 About the Dataset"):
    st.markdown(
        """
        ### 🐧 Palmer's Penguins Dataset Overview
        
        Palmer's Penguins dataset, providing a more comprehensive view of penguin characteristics and their environment. It includes new features such as diet, year of observation, life stage, and health metrics, in addition to the original attributes. The dataset spans from 2021 to 2025.

        ---
        ### 📋 Columns Description

        | Column | Description |
        |--------|-------------|
        | **Species** | Species of the penguin (*Adelie, Chinstrap, Gentoo*) |
        | **Island** | Island where the penguin was found (*Biscoe, Dream, Torgensen*) |
        | **Sex** | Gender of the penguin (*Male, Female*) |
        | **Diet** | Primary diet of the penguin (*Fish, Krill, Squid*) |
        | **Year** | Year the data was collected (*2021–2025*) |
        | **Life Stage** | Life stage of the penguin (*Chick, Juvenile, Adult*) |
        | **Body Mass (g)** | Body mass in grams |
        | **Bill Length (mm)** | Bill length in millimeters |
        | **Bill Depth (mm)** | Bill depth in millimeters |
        | **Flipper Length (mm)** | Flipper length in millimeters |
        | **Health Metrics** | Health status (*Healthy, Overweight, Underweight*) |

        ---
        """,
        unsafe_allow_html=True
    )
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
    


# statistical summary
with st.expander("📊 Statistical Summary of Numerical Columns"):
    st.dataframe(df.describe().style.format(precision=2))


st.write("")

# Add two colummns 
col1, col2, = st.columns(2)

with col1:
    st.markdown("###  Gender Distribution")
    st.write('')
    sex_counts = df['sex'].value_counts().reset_index()
    sex_counts.columns = ['sex', 'count']
    # Create Altair bar chart
    chart = alt.Chart(sex_counts).mark_bar().encode(
        x=alt.X('sex:N', title=None),
        y=alt.Y('count:Q', title=None),
        color='sex:N'
    ).properties(
        height=500,
        title=alt.TitleParams(
            text='Number Of Male & Female Penguins',
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

    # Display in Streamlit
    st.altair_chart(chart, use_container_width=True,)
    st.markdown("<p style='font-family: Arial, sans-serif; font-size: 14px; color: gray; margin-top: 10px;'>"
                "This bar chart shows the count of male and female penguins in the filtered dataset.</p>", unsafe_allow_html=True)
   
    
    
with col2:
    st.write('')
    st.markdown("### Health Metrics Overview", unsafe_allow_html=True)
    explode = (0, 0.1, 0)

    fig, ax = plt.subplots( figsize=(5, 5),facecolor='none')
    a = df['health_metrics'].value_counts().reset_index()
    a.columns = ['health_metrics', 'count']
    print(a)
    wedges, texts, autotexts=ax.pie(a["count"], explode=explode, labels=a["health_metrics"], autopct='%1.1f%%',
        shadow=True, startangle=90,radius=0.5, textprops={'color': 'white'} )
    # Add legend
    ax.legend(
        wedges,
        a["health_metrics"],
        title="Health Metrics",
        loc="center left",
        bbox_to_anchor=(1, 0.5),
        labelcolor='black',
        prop={'size': 10}
    )
    
    st.pyplot(fig)
   #description
    st.markdown(
    "<p style='font-family: Arial, sans-serif; font-size: 14px; color: gray; margin-top: 10px;'>"
    "This pie chart displays the proportion of penguins categorized as Healthy, Overweight, or Underweight."
    "</p>",
    unsafe_allow_html=True
)
    
    
    
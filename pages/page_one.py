import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import altair as alt



# st.title("Streamlit Dashboard (EDA) Project")
st.markdown("""
    <h1 style='text-align: center; color: white; font-family: Arial; font-weight: bold;'>
        Palmer Penguins Dataset (EDA) 
    </h1>
""", unsafe_allow_html=True)

# st.image("https://i.imgur.com/5rtbtpN.png")

# Custom image with height
st.markdown(
    """
    <div style='text-align: center;'>
        <img src='https://i.imgur.com/5rtbtpN.png' style='height:190px;border-radius: 1rem;' />
    </div>
    """,
    unsafe_allow_html=True
)

st.write("")
# read csv
df = pd.read_csv("dataset/palmerpenguins_extended.csv")
df.dropna(inplace=True) # drop null value 


st.write(df.head())




# Add a slider to the sidebar:
add_slider = st.sidebar.slider(
    'Select a range of values',
    0, 100
) | 5




    # st.header("A cat")




col1, col2, = st.columns(2)

with col1:
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



    with st.sidebar:
        add_radio = st.radio(
            "Choose a shipping method",
            ("Standard (5-15 days)", "Express (2-5 days)")
        )

    # Display in Streamlit
    st.altair_chart(chart, use_container_width=True,)
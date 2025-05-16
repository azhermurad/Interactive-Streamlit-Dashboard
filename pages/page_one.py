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





with st.expander("📊 Statistical Summary of Numerical Columns"):
    st.dataframe(df.describe().style.format(precision=2))
 
        

st.write("")

# Add two colummns 
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

    # Display in Streamlit
    st.altair_chart(chart, use_container_width=True,)
    
    
    
    
with col2:
    st.write('')
    explode = (0, 0.1, 0)

    fig, ax = plt.subplots( figsize=(5, 5),facecolor='none')
    a = df['health_metrics'].value_counts().reset_index()
    a.columns = ['health_metrics', 'count']
    print(a)
    wedges, texts, autotexts=ax.pie(a["count"], explode=explode, labels=a["health_metrics"], autopct='%1.1f%%',
        shadow=True, startangle=90,radius=0.5, textprops={'color': 'white'} )
    # Add legend
    # ax.legend(wedges, a["health_metrics"], title="Health Metrics", loc="center left", bbox_to_anchor=(1, 0.5),)
    st.pyplot(fig)

    
    
    
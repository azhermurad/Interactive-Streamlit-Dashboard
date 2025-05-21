import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import altair as alt


st.set_page_config(page_title="Streamlit Dashboard (EDA) Project", layout="wide")



pages = [
        
        # defalt icon of materail library
        
        # st.Page("pages/page_one.py", title="Home", icon=":material/home:"),
        # st.Page("pages/page_two.py", title="Correlation between Features", icon=":material/insights:"),
        # st.Page("pages/page_three.py", title="Analysis based on Bill Length & Bill Depth", icon=":material/insights:"),
        # st.Page("pages/page_four.py", title="Map-Based Visualization", icon=":material/public:"),
        # st.Page("pages/page_five.py", title="Life Stage & Health Trends", icon=":material/health_and_safety:"),
        # st.Page("pages/page_six.py", title="Island-based Body Mass Analysis", icon=":material/fitness_center:"),
        
        # Color Icons 
        st.Page("pages/page_one.py", title="Home", icon="🏠"),
        st.Page("pages/page_two.py", title="Correlation between Features", icon="📊"),
        st.Page("pages/page_three.py", title="Bill Length & Depth", icon="📈"),
        st.Page("pages/page_four.py", title="Map-Based Visualization", icon="🗺️"),
        st.Page("pages/page_five.py", title="Health Trends", icon="❤️"),
        st.Page("pages/page_six.py", title="Body Mass Analysis", icon="🏋️"),

        
        
        
        ]


pg = st.navigation(pages)
pg.run()



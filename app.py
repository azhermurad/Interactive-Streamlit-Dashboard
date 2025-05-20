import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import altair as alt


st.set_page_config(page_title="Streamlit Dashboard (EDA) Project", layout="wide")



pages = [
        st.Page("pages/page_one.py", title="Home",icon=":material/home:"),
        st.Page("pages/page_two.py", title="Correlation between Features",icon=":material/responsive_layout:"),
        st.Page("pages/page_three.py", title="Analysis based on Bill Length & Bill Depth",icon=":material/monitoring:"),
        st.Page("pages/page_four.py", title="Map-Based Visualization",icon=":material/map:"),
        st.Page("pages/page_five.py", title="Life Stage & Health Trends",icon=":material/map:"),
        st.Page("pages/page_six.py", title="Island-based Body Mass Analysis",icon=":material/map:")]


pg = st.navigation(pages)
pg.run()



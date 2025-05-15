import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import altair as alt


st.set_page_config(page_title="Streamlit Dashboard (EDA) Project", layout="wide")



pages = [
        st.Page("pages/page_one.py", title="Home",icon=":material/home:"),
        st.Page("pages/page_two.py", title="Page_2",icon=":material/responsive_layout:"),
        st.Page("pages/page_three.py", title="Page_3",icon=":material/monitoring:")]


pg = st.navigation(pages)
pg.run()



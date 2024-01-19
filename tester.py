import streamlit as st
from streamlit_lottie import st_lottie
st.set_page_config(page_title="All about me!", page_icon="🐼", layout="wide")
st.header("All about me")
st.caption("This is my first website posted on streamlit!")
l, m, r = st.columns(3)
lottie_robots = st.json("https://lottie.host/b80df535-7d0b-4eeb-81fa-1b5362f0b651/OMFm2v3X3V.json")
st_lottie(lottie_robots,height="300", key="robots")

import streamlit as st
from streamlit_extras.let_it_rain import rain
from streamlit_extras.badges import badge
st.set_page_config(page_title="All about me!", page_icon="🐼", layout="wide")
rain(
  emoji="⭐",
  font_size=40,
  falling_speed=7,
  animation_length="infinite",
)
st.header("All about me")
st.caption("This is my first website posted on streamlit cloud!")
st.write("---")
l, m, r = st.tabs(["Home", "Me", "Website"])
with l:
  st.header("Home page", anchor="Home")
with m:
  st.header("All about me", anchor="Me")
  st.write("I'm a kid named Isaac Rhee doing coding stuff normally in python. I can make simple websites using streamlit (it's really easy to use). \nP.S: I might make more websites")
with r:
  st.header("My channel", anchor="Website")
  st.link_button("The channel", url="https://www.youtube.com/channel/UCU2ciboF3zbv9sV4Bir18NQ")
  st.header("My other streamlit websites (will be finished by Jan 10, 2025)")
  badge(type="streamlit", url="https://python-programs.streamlit.app")
  badge(type="streamlit", url="https://pygame-programs.streamlit.app")

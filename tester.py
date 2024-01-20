import streamlit as st
import requests
from streamlit_lottie import st_lottie
from streamlit_extras.let_it_rain import rain
from streamlit_extras.badges import badge
st.set_page_config(page_title="All about me!", page_icon="🐼", layout="wide")
rain(
  emoji="⭐",
  font_size=40,
  falling_speed=7,
  animation_length="infinite",
)
def load_lottieurl(url):
  r = requests.get(url)
  if r.status_code != 200:
    return None
  return r.json()
kid_that_code = load_lottieurl("https://lottie.host/43e9df2a-0675-46c5-a3c8-116f9664e1dd/hnl9rDKKmX.json")
website = load_lottieurl("https://lottie.host/3b39e3b5-2092-4364-ae5b-7353610dfe4a/Ml44OIJSvO.json")
st.header("All about me")
st.caption("This is my first website posted on streamlit cloud!")
l, m, r = st.tabs(["Home", "Me", "Website"])
with l:
  st.header("Home page", anchor="Home")
with m:
  st.header("All about me", anchor="Me")
  st.subheader("I'm a kid doing coding stuff normally in python.")
  st.subheader("I've been coding for about 10 months")
  st_lottie(kid_that_code, height=250, key="Coding")
  st.subheader("I can make simple websites using streamlit and I try to learn more features for it everyday.")
  st_lottie(website, height=250, key="Website")
  "P.S: I might make more websites"
with r:
  st.header("My channel", anchor="Website")
  st.link_button("The channel", url="https://www.youtube.com/channel/UCU2ciboF3zbv9sV4Bir18NQ")
  st.header("My other streamlit websites (will be finished by March 1, 2024)")
  st.write("Python programs")
  badge(type="streamlit", url="https://python-programs.streamlit.app")
  st.write("Pygame programs")
  badge(type="streamlit", url="https://pygame-programs.streamlit.app")

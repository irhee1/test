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
l, m, r = st.columns(3)
l_ex = l.expander("Stuff about me!")
m_ex = m.expander("What I like doing!")
r_ex = r.expander("More")
with l_ex:
  pass
with m_ex:
  m_ex.subheader("Coding!")
  m_ex.subheader("Building robots")
  m_ex.subheader("Math")
with r_ex:
  r_ex.header("My channel")
  badge(type="Youtube", url="https://www.youtube.com/channel/UCU2ciboF3zbv9sV4Bir18NQ")
  r_ex.header("My other streamlit websites (will be finished by Jan 10, 2025)")
  badge(type="Streamlit", url="https://python-programs.streamlit.app")
  badge(type="Streamlit, url="https://pygame-programs.streamlit.app")

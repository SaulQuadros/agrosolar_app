from __future__ import annotations

import streamlit as st
from src.ui.pages_home import render as render_home

st.set_page_config(page_title="AgroSolar (Demo)", page_icon="☀️", layout="wide")

render_home()

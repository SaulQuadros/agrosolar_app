from __future__ import annotations

import streamlit as st
from src.ui.pages_about import render

st.set_page_config(page_title="Sobre — AgroSolar", page_icon="ℹ️", layout="wide")
render()

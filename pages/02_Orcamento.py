from __future__ import annotations

import streamlit as st
from src.ui.pages_quote import render

st.set_page_config(page_title="Orçamento — AgroSolar", page_icon="📝", layout="wide")
render()

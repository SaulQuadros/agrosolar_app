from __future__ import annotations

import streamlit as st
from src.ui.theme import inject_css


def render() -> None:
    inject_css()
    st.title("Leads")
    st.markdown(
        """
<div class="ag-panel">
  <div class="ag-small-title">Em breve</div>
  <h3 style="margin:6px 0 4px 0;">Página em construção</h3>
  <p style="margin:0;">
    Esta área será reformulada para uma experiência mais amigável de gestão de leads.
  </p>
</div>
        """,
        unsafe_allow_html=True,
    )

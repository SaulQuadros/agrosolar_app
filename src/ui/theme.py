from __future__ import annotations
import streamlit as st

def inject_css() -> None:
    st.markdown(
        """
<style>
/* Layout */
.block-container { padding-top: 2rem; padding-bottom: 3rem; max-width: 1100px; }

/* Cards */
.ag-card {
  border: 1px solid rgba(0,0,0,0.08);
  border-radius: 14px;
  padding: 16px 18px;
  background: rgba(255,255,255,0.70);
}
.ag-hero {
  padding: 22px 22px;
  border-radius: 18px;
  border: 1px solid rgba(0,0,0,0.08);
  background: linear-gradient(135deg, rgba(240,248,255,0.9), rgba(255,255,255,0.7));
}
.small-muted { opacity: 0.75; font-size: 0.92rem; }
</style>
        """,
        unsafe_allow_html=True,
    )

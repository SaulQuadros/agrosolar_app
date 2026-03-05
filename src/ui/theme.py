from __future__ import annotations
import streamlit as st

def inject_css() -> None:
    st.markdown(
        """
<style>
@import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@500;700;800&family=Source+Sans+3:wght@400;600;700&display=swap');

:root {
  --ag-navy: #0d3a66;
  --ag-navy-strong: #082a49;
  --ag-orange: #de7a24;
  --ag-orange-soft: #f0a35e;
  --ag-ink: #1a2530;
  --ag-muted: #5f6d7b;
  --ag-paper: #f5f7fa;
  --ag-white: #ffffff;
  --ag-line: rgba(13,58,102,0.18);
}

html, body, [class*="css"] {
  font-family: "Source Sans 3", sans-serif;
  color: var(--ag-ink);
}

.stApp {
  background:
    linear-gradient(180deg, rgba(13,58,102,0.06), rgba(13,58,102,0.0) 320px),
    linear-gradient(90deg, rgba(13,58,102,0.05) 1px, transparent 1px),
    linear-gradient(rgba(13,58,102,0.05) 1px, transparent 1px),
    var(--ag-paper);
  background-size: auto, 24px 24px, 24px 24px, auto;
}

.block-container {
  padding-top: 1.6rem;
  padding-bottom: 3rem;
  max-width: 1180px;
}

h1, h2, h3, .ag-title {
  font-family: "Montserrat", sans-serif;
  color: var(--ag-navy-strong);
  letter-spacing: -0.02em;
}

p, li, .small-muted {
  color: var(--ag-muted);
}

.ag-panel {
  border: 1px solid var(--ag-line);
  border-radius: 18px;
  padding: 18px 20px;
  background: rgba(255,255,255,0.92);
  box-shadow: 0 8px 28px rgba(9,30,66,0.06);
}

.ag-card {
  border: 1px solid var(--ag-line);
  border-radius: 16px;
  padding: 16px 18px;
  background:
    linear-gradient(160deg, rgba(255,255,255,0.95), rgba(244,248,252,0.95));
  box-shadow: 0 8px 22px rgba(9,30,66,0.06);
}

.ag-blueprint {
  position: relative;
  border: 1px solid rgba(13,58,102,0.22);
  border-radius: 18px;
  padding: 18px;
  background: linear-gradient(155deg, #0d3a66, #0a2f53);
  color: #f1f6fb;
  overflow: hidden;
}

.ag-blueprint::after {
  content: "";
  position: absolute;
  inset: 0;
  background-image:
    linear-gradient(rgba(255,255,255,0.08) 1px, transparent 1px),
    linear-gradient(90deg, rgba(255,255,255,0.08) 1px, transparent 1px);
  background-size: 22px 22px;
  pointer-events: none;
}

.ag-hero {
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  border: 1px solid var(--ag-line);
  border-radius: 22px;
  padding: 20px;
  background: linear-gradient(145deg, rgba(255,255,255,0.98), rgba(237,244,250,0.96));
  box-shadow: 0 12px 30px rgba(8,42,73,0.08);
  animation: agFadeUp 450ms ease;
  min-height: 360px;
}

.ag-hero-content { margin-bottom: 14px; }

.ag-cta-row {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 10px;
}

.ag-cta-btn {
  display: flex;
  align-items: center;
  justify-content: center;
  min-height: 46px;
  padding: 10px 14px;
  border-radius: 12px;
  border: 1px solid rgba(13,58,102,0.20);
  background: linear-gradient(120deg, var(--ag-navy), #14518d);
  color: #fff !important;
  font-weight: 700;
  text-decoration: none !important;
  text-align: center;
}

.ag-cta-btn:hover {
  filter: brightness(1.04);
}

.ag-chip {
  display: inline-block;
  margin: 0 8px 8px 0;
  padding: 6px 12px;
  border-radius: 999px;
  border: 1px solid rgba(222,122,36,0.35);
  background: rgba(222,122,36,0.08);
  color: var(--ag-navy-strong);
  font-size: 0.86rem;
  font-weight: 600;
}

.ag-small-title {
  font-family: "Montserrat", sans-serif;
  text-transform: uppercase;
  font-size: 0.78rem;
  letter-spacing: 0.08em;
  color: var(--ag-orange);
}

.stMetric {
  border: 1px solid var(--ag-line);
  border-radius: 14px;
  padding: 10px 12px;
  background: #fff;
}

.stButton > button, .stDownloadButton > button {
  border: 0;
  border-radius: 12px;
  background: linear-gradient(120deg, var(--ag-navy), #14518d);
  color: white;
  font-weight: 700;
}

.stLinkButton > a {
  border-radius: 12px !important;
  border: 1px solid rgba(13,58,102,0.2) !important;
}

@keyframes agFadeUp {
  from { opacity: 0; transform: translateY(8px); }
  to { opacity: 1; transform: translateY(0); }
}

@media (max-width: 900px) {
  .block-container { padding-top: 1rem; }
  .ag-hero { padding: 16px; }
  .ag-hero { min-height: auto; }
  .ag-hero-content { margin-bottom: 10px; }
  .ag-cta-row { grid-template-columns: 1fr; }
}
</style>
        """,
        unsafe_allow_html=True,
    )

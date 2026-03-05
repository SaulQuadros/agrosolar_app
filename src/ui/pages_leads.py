from __future__ import annotations

import streamlit as st
import pandas as pd

from src.ui.theme import inject_css
from src.core.leads import PIPELINE_STATUSES
from src.tools.formatting import brl

def _guess_columns(df: pd.DataFrame) -> dict:
    """Tenta mapear colunas comuns exportadas do Forms."""
    cols = {c.lower(): c for c in df.columns}
    def pick(*options):
        for o in options:
            if o in cols:
                return cols[o]
        return None

    return {
        "name": pick("nome", "name"),
        "city": pick("cidade", "city", "cidade/uf"),
        "phone": pick("whatsapp", "telefone", "phone", "celular"),
        "status": pick("status"),
        "value": pick("valor", "valor (r$)", "ticket", "value"),
    }

def render() -> None:
    inject_css()
    st.title("Leads (opcional)")
    st.caption("Faça upload de um CSV exportado do Google Sheets/Forms para acompanhar o funil.")

    up = st.file_uploader("CSV de leads", type=["csv"])
    if not up:
        st.info("Dica: no Google Sheets, vá em Arquivo → Fazer download → Valores separados por vírgulas (.csv).")
        return

    df = pd.read_csv(up)
    st.write("Prévia dos dados:")
    st.dataframe(df, use_container_width=True)

    st.divider()
    st.subheader("Funil (simples)")
    mapping = _guess_columns(df)

    status_col = mapping["status"]
    if status_col is None:
        st.warning("Não encontrei uma coluna 'Status'. Você pode criar uma coluna Status no CSV com valores do funil.")
        st.markdown("Valores sugeridos: " + ", ".join([f"`{s}`" for s in PIPELINE_STATUSES]))
        return

    # Normalizar status
    df2 = df.copy()
    df2[status_col] = df2[status_col].astype(str).str.strip()
    counts = df2[status_col].value_counts(dropna=False)

    c1, c2, c3, c4, c5 = st.columns(5)
    cols = [c1, c2, c3, c4, c5]
    for i, s in enumerate(PIPELINE_STATUSES):
        with cols[i]:
            st.metric(s, int(counts.get(s, 0)))

    value_col = mapping["value"]
    if value_col and value_col in df2.columns:
        # tenta converter
        v = pd.to_numeric(df2[value_col], errors="coerce")
        total = float(v.fillna(0).sum())
        st.metric("Soma de valores (se houver)", brl(total))

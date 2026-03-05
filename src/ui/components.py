from __future__ import annotations

import streamlit as st
from typing import List
from src.tools.formatting import brl

def hero(title: str, subtitle: str, bullets: List[str]) -> None:
    st.markdown(f"""<div class="ag-hero">
<h2 style="margin:0 0 8px 0;">{title}</h2>
<p class="small-muted" style="margin:0 0 12px 0;">{subtitle}</p>
</div>""", unsafe_allow_html=True)

    cols = st.columns(3)
    for i, b in enumerate(bullets[:3]):
        with cols[i]:
            st.markdown(f"""<div class="ag-card"><b>{b}</b></div>""", unsafe_allow_html=True)

def cta_row(canva_url: str, form_url: str, whatsapp_url: str) -> None:
    c1, c2, c3 = st.columns(3)
    with c1:
        st.link_button("Ver vitrine (Canva Website)", canva_url, use_container_width=True)
    with c2:
        st.link_button("Solicitar orçamento (Forms)", form_url, use_container_width=True)
    with c3:
        st.link_button("Falar no WhatsApp", whatsapp_url, use_container_width=True)

def pricing_cards(packages) -> None:
    st.subheader("Pacotes (faixas de preço)")
    cols = st.columns(3)
    for i, p in enumerate(packages):
        with cols[i]:
            low, high = p.price_range_brl
            st.markdown('<div class="ag-card">', unsafe_allow_html=True)
            st.markdown(f"### {p.name}")
            st.caption(p.ideal_for)
            st.markdown(f"**A partir de:** {brl(low)}\n**Até:** {brl(high)}")
            st.markdown("**Inclui:**")
            for item in p.includes:
                st.markdown(f"- {item}")
            st.markdown("</div>", unsafe_allow_html=True)

def faq() -> None:
    st.subheader("FAQ (objeções comuns)")
    with st.expander("“É caro?”"):
        st.write(
            "O investimento inicial varia conforme vazão, altura manométrica, distância e horas de operação. "
            "Por isso trabalhamos com pacotes e dimensionamento. Em muitos casos, a economia e a autonomia no campo "
            "compensam no médio prazo."
        )
    with st.expander("“A instalação é difícil?”"):
        st.write(
            "A instalação segue checklist e comissionamento. Também oferecemos treinamento e um guia de operação/manutenção "
            "para reduzir dúvidas e riscos."
        )
    with st.expander("“E manutenção/peças?”"):
        st.write(
            "Oferecemos manutenção preventiva/corretiva e reposição de peças (quando aplicável), além de planos opcionais "
            "para atendimento prioritário."
        )

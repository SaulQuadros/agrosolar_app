from __future__ import annotations

import streamlit as st
from typing import List
from src.tools.formatting import brl

def hero(title: str, subtitle: str, bullets: List[str], image_path: str | None = None) -> None:
    subtitle_html = f'<p class="small-muted" style="margin:0 0 14px 0;">{subtitle}</p>' if subtitle else ""
    left, right = st.columns([1.25, 1], gap="large")
    with left:
        st.markdown(
            f"""
<div class="ag-hero">
  <div class="ag-small-title">Solução Agrosola</div>
  <h2 style="margin:0 0 8px 0;">{title}</h2>
  {subtitle_html}
  {"".join([f'<span class="ag-chip">{b}</span>' for b in bullets[:4]])}
</div>
            """,
            unsafe_allow_html=True,
        )
    with right:
        if image_path:
            st.image(image_path, use_container_width=True, caption="Bomba-Solar")
        else:
            st.markdown(
                """
<div class="ag-blueprint">
  <h4 style="margin:0 0 8px 0; color:#f8fbff;">Diagnóstico técnico + execução em campo</h4>
  <p style="margin:0; color:#d8e6f4;">
    Projeto, kit, instalação e manutenção em uma solução de engenharia.
  </p>
</div>
                """,
                unsafe_allow_html=True,
            )

def cta_row(form_url: str, whatsapp_url: str) -> None:
    c1, c2 = st.columns(2)
    with c1:
        st.link_button("Solicitar orçamento", form_url, use_container_width=True)
    with c2:
        st.link_button("Contato no WhatsApp", whatsapp_url, use_container_width=True)

def pricing_cards(packages) -> None:
    st.subheader("Pacotes (faixas de preço)")
    cols = st.columns(3)
    for i, p in enumerate(packages):
        with cols[i]:
            low, high = p.price_range_brl
            st.markdown('<div class="ag-card">', unsafe_allow_html=True)
            st.markdown(f'<div class="ag-small-title">Plano</div><h3 style="margin:4px 0 8px 0;">{p.name}</h3>', unsafe_allow_html=True)
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

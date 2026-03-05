from __future__ import annotations

import streamlit as st
from src.ui.theme import inject_css
from src.tools.config_loader import load_config

def render() -> None:
    cfg = load_config()
    inject_css()

    st.title("Sobre o APP (didático)")
    st.write(
        "Este APP é um **complemento** para a vitrine principal (Canva Website) e para a captação de orçamento (Google Forms). "
        "Ele ajuda a reforçar a proposta de valor, apresentar pacotes e oferecer um simulador simples."
    )

    st.subheader("Como usar com Canva + Forms")
    st.markdown(
        """- Use o **Canva Website** como landing page principal.  
- Insira botões: **Orçamento (Forms)**, **WhatsApp** e **Simulador (este app)**.  
- Use o Forms para captar leads e organizar as respostas em uma planilha.  
- Se quiser, exporte CSV para acompanhar o funil na página **Leads**."""
    )

    st.subheader("Links")
    st.link_button("Vitrine (Canva Website)", cfg.canva_website_url, use_container_width=True)
    st.link_button("Orçamento (Google Forms)", cfg.google_form_url, use_container_width=True)
    st.link_button("WhatsApp", cfg.whatsapp_url, use_container_width=True)

    st.caption("Template educacional — ajuste textos, pacotes e hipóteses conforme a aula.")

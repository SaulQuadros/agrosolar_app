from __future__ import annotations

import streamlit as st
from src.ui.theme import inject_css
from src.ui.components import hero, cta_row, pricing_cards, faq
from src.core.catalog import get_default_packages
from src.tools.config_loader import load_config

def render() -> None:
    cfg = load_config()
    inject_css()

    st.title(cfg.company_name)
    st.caption(cfg.tagline)

    hero(
        title="Bombeamento solar para agricultura sustentável",
        subtitle="Venda • Instalação • Manutenção • Peças — solução completa para irrigação e abastecimento.",
        bullets=[
            "Reduza custos de energia",
            "Autonomia no campo",
            "Suporte técnico e manutenção",
        ],
    )

    st.write("")
    cta_row(cfg.canva_website_url, cfg.google_form_url, cfg.whatsapp_url)

    st.divider()
    st.header("A solução (o produto é o serviço de engenharia)")
    st.write(
        "Nós cuidamos do sistema completo: dimensionamento (vazão/altura/perdas), fornecimento do kit (bomba + FV), "
        "instalação e comissionamento, manutenção preventiva/corretiva e reposição de peças."
    )

    st.divider()
    packages = get_default_packages()
    pricing_cards(packages)

    st.divider()
    st.header("Como funciona")
    st.markdown(
        """1. Você envia os dados no formulário  
2. Nós dimensionamos o sistema  
3. Enviamos proposta com 3 opções  
4. Instalamos e entregamos em operação  
5. Manutenção e suporte contínuos"""
    )

    st.divider()
    faq()

    st.divider()
    st.caption(f"Contato: {cfg.contact_email}")

from __future__ import annotations

import streamlit as st
from src.ui.theme import inject_css
from src.ui.components import hero, pricing_cards, faq
from src.core.catalog import get_default_packages
from src.tools.config_loader import load_config

def render() -> None:
    cfg = load_config()
    inject_css()

    st.title(cfg.company_name)
    st.caption(cfg.tagline)

    hero(
        title="Bombeamento sustentável para sua lavroura e agronegócio",
        subtitle="Mude para a sustentabilidade da energia solar e economize na sua produção rural!",
        bullets=[],
        image_path="assets/images/bomba_fotovoltaico.png",
        form_url=cfg.google_form_url,
        whatsapp_url=cfg.whatsapp_url,
    )

    st.divider()
    st.markdown(
        """
<div class="ag-panel">
  <div class="ag-small-title">Proposta de valor</div>
  <h3 style="margin-top:4px;">A solução é engenharia aplicada, não só equipamento</h3>
  <p style="margin:0;">
    Cuidamos do ciclo completo: levantamento técnico (vazão/altura/perdas), fornecimento do kit
    (bomba + FV), instalação e comissionamento, manutenção preventiva/corretiva e reposição de peças.
  </p>
</div>
        """,
        unsafe_allow_html=True,
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

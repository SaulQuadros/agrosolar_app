from __future__ import annotations

import streamlit as st
from src.ui.theme import inject_css
from src.forms.google_forms import to_embed_url, is_google_forms
from src.tools.config_loader import load_config

def render() -> None:
    cfg = load_config()
    inject_css()

    st.title("Solicitar orçamento")
    st.caption("Preencha o formulário e retornaremos com 3 opções (Essencial, Profissional e Fazenda).")
    st.markdown(
        """
<div class="ag-panel">
  <div class="ag-small-title">Briefing técnico</div>
  <p style="margin: 6px 0 0 0;">
    Quanto melhor o briefing, mais preciso o pré-dimensionamento de bomba, geração FV e estimativa de investimento.
  </p>
</div>
        """,
        unsafe_allow_html=True,
    )

    if not cfg.google_form_url or "SEU-ID" in cfg.google_form_url:
        st.warning("Configure o link do Google Forms em `st.secrets` (recomendado) ou em `config/app_config.py`.")
        st.code('google_form_url = "https://docs.google.com/forms/d/e/SEU-ID/viewform"')
        return

    st.subheader("Formulário")
    if is_google_forms(cfg.google_form_url):
        embed = to_embed_url(cfg.google_form_url)
        st.components.v1.iframe(embed, height=900, scrolling=True)
    else:
        st.info("Link não parece ser do Google Forms. Abrindo como link externo.")
        st.link_button("Abrir formulário", cfg.google_form_url, use_container_width=True)

    st.divider()
    st.subheader("O que enviar (para agilizar)")
    st.markdown(
        """- Cidade/UF  
- Uso (irrigação / abastecimento / outro)  
- Vazão desejada (faixa)  
- Altura manométrica (faixa)  
- Distância aproximada da tubulação  
- Horas/dia de operação"""
    )
    st.image("assets/images/bomba_fotovoltaico.png", use_container_width=True, caption="Bomba-Solar")

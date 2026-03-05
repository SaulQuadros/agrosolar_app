from __future__ import annotations

from typing import Any, Dict
import streamlit as st

from config.app_config import AppConfig

def load_config() -> AppConfig:
    """Carrega configurações priorizando st.secrets (Streamlit Cloud).
    Se não existir, usa defaults do AppConfig.
    """
    defaults = AppConfig()
    data: Dict[str, Any] = {}

    # Streamlit secrets pode não existir localmente
    try:
        secrets = st.secrets
        # st.secrets funciona como dict
        for key in ("company_name", "tagline", "canva_website_url", "google_form_url", "whatsapp_url", "contact_email"):
            if key in secrets:
                data[key] = str(secrets[key])
    except Exception:
        pass

    return AppConfig(
        company_name=data.get("company_name", defaults.company_name),
        tagline=data.get("tagline", defaults.tagline),
        canva_website_url=data.get("canva_website_url", defaults.canva_website_url),
        google_form_url=data.get("google_form_url", defaults.google_form_url),
        whatsapp_url=data.get("whatsapp_url", defaults.whatsapp_url),
        contact_email=data.get("contact_email", defaults.contact_email),
    )

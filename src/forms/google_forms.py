from __future__ import annotations

import re

def to_embed_url(form_url: str) -> str:
    """Converte links comuns do Google Forms para URL embutida (iframe).
    Aceita:
      - .../viewform
      - .../viewform?usp=...
    Retorna:
      - .../viewform?embedded=true&...
    """
    if not form_url:
        return ""

    # Se já tem embedded=true, retorna como está
    if "embedded=true" in form_url:
        return form_url

    # Garantir que é viewform
    if "viewform" not in form_url:
        return form_url

    if "?" in form_url:
        return form_url + "&embedded=true"
    return form_url + "?embedded=true"

def is_google_forms(url: str) -> bool:
    return bool(re.search(r"docs\.google\.com/forms", url or ""))

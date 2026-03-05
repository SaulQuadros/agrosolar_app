from __future__ import annotations

def brl(value: float) -> str:
    """Formata número como BRL aproximado (R$ 1.234,56)."""
    # formata com separador milhar e decimal pt-BR sem depender de locale do SO
    s = f"{value:,.2f}"
    s = s.replace(",", "X").replace(".", ",").replace("X", ".")
    return f"R$ {s}"

def percent(value: float) -> str:
    return f"{value*100:.1f}%"

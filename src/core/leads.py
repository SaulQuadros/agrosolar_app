from __future__ import annotations

from dataclasses import dataclass
from typing import Optional

PIPELINE_STATUSES = ["Novo", "Contato", "Proposta", "Fechado", "Perdido"]

@dataclass
class Lead:
    name: str
    city: str
    phone: str
    demand_note: str = ""
    status: str = "Novo"
    value_brl: Optional[float] = None

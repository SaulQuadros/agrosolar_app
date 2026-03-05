from __future__ import annotations

from dataclasses import dataclass
from typing import List, Tuple

@dataclass(frozen=True)
class Package:
    name: str
    ideal_for: str
    includes: List[str]
    price_range_brl: Tuple[float, float]

def get_default_packages() -> List[Package]:
    """Pacotes de referência comercial (faixas de preço aproximadas)."""
    return [
        Package(
            name="Essencial",
            ideal_for="Pequenas propriedades / baixa demanda",
            includes=[
                "Kit bombeamento solar compacto",
                "Instalação padrão e comissionamento",
                "Treinamento do operador",
                "1 revisão em 90 dias",
            ],
            price_range_brl=(12000.0, 25000.0),
        ),
        Package(
            name="Profissional",
            ideal_for="Uso frequente / maior altura manométrica",
            includes=[
                "Kit otimizado para maior desempenho",
                "Proteções e recomendações de operação",
                "Instalação + checklist de entrega",
                "Plano de manutenção trimestral (opcional)",
            ],
            price_range_brl=(25000.0, 55000.0),
        ),
        Package(
            name="Fazenda",
            ideal_for="Alta demanda / maior robustez",
            includes=[
                "Projeto e dimensionamento completo",
                "Visita técnica (opcional)",
                "Instalação e comissionamento",
                "Contrato anual de manutenção (opcional)",
                "Prioridade de atendimento e peças",
            ],
            price_range_brl=(55000.0, 120000.0),
        ),
    ]

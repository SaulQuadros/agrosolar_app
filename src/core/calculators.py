from __future__ import annotations

from dataclasses import dataclass

@dataclass(frozen=True)
class RoiResult:
    monthly_energy_kwh: float
    monthly_cost_grid_brl: float
    estimated_investment_brl: float
    payback_months: float | None

def estimate_pv_kwp(pump_power_kw: float, hours_per_day: float, psh: float, system_eff: float) -> float:
    """Dimensionamento energético simplificado.
    Energia/dia (kWh) = P_pump(kW) * horas
    Geração/dia ≈ PV(kWp) * PSH * eficiência
    => PV(kWp) = energia_dia / (PSH * eficiência)
    """
    if psh <= 0 or system_eff <= 0:
        return 0.0
    energy_day = pump_power_kw * hours_per_day
    return energy_day / (psh * system_eff)

def roi_simple(
    pump_power_kw: float,
    hours_per_day: float,
    days_per_month: int,
    grid_price_brl_per_kwh: float,
    investment_brl: float,
    maintenance_brl_per_month: float = 0.0,
) -> RoiResult:
    monthly_energy = pump_power_kw * hours_per_day * float(days_per_month)
    monthly_cost_grid = monthly_energy * grid_price_brl_per_kwh
    # economia aproximada: custo na rede - manutenção (solar)
    monthly_saving = max(monthly_cost_grid - maintenance_brl_per_month, 0.0)

    if monthly_saving <= 0:
        payback = None
    else:
        payback = investment_brl / monthly_saving

    return RoiResult(
        monthly_energy_kwh=monthly_energy,
        monthly_cost_grid_brl=monthly_cost_grid,
        estimated_investment_brl=investment_brl,
        payback_months=payback,
    )

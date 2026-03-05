from __future__ import annotations

import streamlit as st
from src.ui.theme import inject_css
from src.forms.google_forms import to_embed_url, is_google_forms
from src.tools.config_loader import load_config
from src.tools.formatting import brl
from src.core.calculators import estimate_pv_kwp, roi_simple
from src.core.catalog import get_default_packages


def _recommend_package(investment_brl: float, flow_m3_h: float, effective_head_m: float) -> str:
    if flow_m3_h >= 18.0 or effective_head_m >= 85.0 or investment_brl >= 55000.0:
        return "Fazenda"
    if flow_m3_h >= 9.0 or effective_head_m >= 45.0 or investment_brl >= 25000.0:
        return "Profissional"
    return "Essencial"

def render() -> None:
    cfg = load_config()
    inject_css()

    st.title("Solicitar orçamento")
    st.caption("Faça um pré-orçamento fictício com dados técnicos e, depois, formalize no formulário.")

    c_top_1, c_top_2 = st.columns([1.35, 1], gap="large")
    with c_top_1:
        st.markdown(
            """
<div class="ag-panel">
  <div class="ag-small-title">Pré-orçamento didático</div>
  <p style="margin: 6px 0 0 0;">
    Informe vazão, altura manométrica, distância de bombeamento e rotina de uso para gerar uma
    estimativa inicial de potência, faixa de investimento e payback.
  </p>
</div>
            """,
            unsafe_allow_html=True,
        )
    with c_top_2:
        st.image("assets/images/Produtos.png", use_container_width=True, caption="Produtos AgroSolar")

    st.subheader("Dados técnicos do cliente")
    a1, a2, a3 = st.columns(3)
    with a1:
        flow_m3_h = st.number_input("Vazão (m³/h)", min_value=0.1, value=8.0, step=0.5)
        head_m = st.number_input("Altura manométrica (m)", min_value=1.0, value=35.0, step=1.0)
    with a2:
        distance_m = st.number_input("Distância média de bombeamento (m)", min_value=1.0, value=220.0, step=10.0)
        hours_per_day = st.number_input("Horas/dia de operação", min_value=0.5, value=5.0, step=0.5)
    with a3:
        days_per_month = st.number_input("Dias/mês de operação", min_value=1, value=25, step=1)
        grid_price = st.number_input("Tarifa de energia (R$/kWh)", min_value=0.10, value=0.95, step=0.05)

    st.subheader("Premissas para estimativa")
    b1, b2, b3 = st.columns(3)
    with b1:
        psh = st.number_input("PSH (h)", min_value=1.0, value=5.0, step=0.5)
    with b2:
        system_eff = st.number_input("Eficiência FV (0-1)", min_value=0.30, max_value=0.95, value=0.75, step=0.05)
    with b3:
        maintenance = st.number_input("Manutenção mensal (R$)", min_value=0.0, value=40.0, step=10.0)

    st.divider()
    st.subheader("Resultado do pré-orçamento")

    # Estimativa simplificada de altura equivalente com perda linear aproximada na tubulação.
    effective_head_m = head_m + (distance_m * 0.015)
    flow_m3_s = flow_m3_h / 3600.0
    hydraulic_kw = 9.81 * flow_m3_s * effective_head_m
    pump_eff = 0.55
    pump_power_kw = hydraulic_kw / pump_eff
    pv_kwp = estimate_pv_kwp(pump_power_kw, hours_per_day, psh, system_eff)

    # Calibração comercial (referência): equipamentos + infraestrutura + engenharia.
    pump_set_cost = 8500.0 + (pump_power_kw * 2900.0)
    pv_set_cost = pv_kwp * 4200.0
    civil_electrical_cost = 4200.0 + (effective_head_m * 45.0)
    piping_cost = distance_m * 26.0
    project_and_commissioning = 3500.0
    subtotal = pump_set_cost + pv_set_cost + civil_electrical_cost + piping_cost + project_and_commissioning
    contingency_factor = 1.0 + min(distance_m / 2500.0, 0.12)
    estimated_investment = subtotal * contingency_factor
    low_range = estimated_investment * 0.90
    high_range = estimated_investment * 1.15

    roi = roi_simple(
        pump_power_kw=pump_power_kw,
        hours_per_day=hours_per_day,
        days_per_month=int(days_per_month),
        grid_price_brl_per_kwh=grid_price,
        investment_brl=estimated_investment,
        maintenance_brl_per_month=maintenance,
    )
    package_name = _recommend_package(estimated_investment, flow_m3_h, effective_head_m)

    r1, r2, r3, r4 = st.columns(4)
    with r1:
        st.metric("Potência estimada da bomba", f"{pump_power_kw:.2f} kW")
    with r2:
        st.metric("PV recomendado", f"{pv_kwp:.2f} kWp")
    with r3:
        st.metric("Faixa estimada", f"{brl(low_range)} - {brl(high_range)}")
    with r4:
        st.metric("Pacote sugerido", package_name)

    if roi.payback_months is None:
        st.warning(
            "Payback não calculado com as premissas atuais. "
            "Para calcular, a economia mensal precisa ser positiva."
        )
    else:
        st.success(f"Payback estimado: **{roi.payback_months:.1f} meses** (~{roi.payback_months/12:.1f} anos).")
    with st.expander("Ver composição estimada de custos"):
        st.markdown(
            f"""- Conjunto bomba/motobomba: **{brl(pump_set_cost)}**  
- Conjunto fotovoltaico (módulos + inversão/controle): **{brl(pv_set_cost)}**  
- Infraestrutura civil/elétrica: **{brl(civil_electrical_cost)}**  
- Tubulação/acessórios (distância): **{brl(piping_cost)}**  
- Projeto, comissionamento e startup: **{brl(project_and_commissioning)}**  
- Fator de contingência logística/técnica: **{(contingency_factor - 1.0) * 100:.1f}%**"""
        )

    st.divider()
    st.subheader("Premissas aplicadas")
    st.markdown(
        f"""- Altura equivalente usada: **{effective_head_m:.1f} m** (altura + perdas simplificadas pela distância)  
- Eficiência da bomba considerada: **55%**  
- Economia mensal estimada: **{brl(roi.monthly_cost_grid_brl - maintenance)}**  
- Estrutura de custo estimada: bomba + FV + infraestrutura + tubulação + engenharia  
- Simulação comercial de referência: valores reais dependem de visita técnica e detalhamento hidráulico"""
    )

    st.divider()
    st.subheader("Formalizar pedido")
    if not cfg.google_form_url or "SEU-ID" in cfg.google_form_url:
        st.warning("Configure o link do Google Forms em `st.secrets` (recomendado) ou em `config/app_config.py`.")
        st.code('google_form_url = "https://docs.google.com/forms/d/e/SEU-ID/viewform"')
        return

    st.link_button("Solicitar orçamento", cfg.google_form_url, use_container_width=True)
    if is_google_forms(cfg.google_form_url):
        with st.expander("Abrir formulário embutido aqui"):
            embed = to_embed_url(cfg.google_form_url)
            st.components.v1.iframe(embed, height=820, scrolling=True)

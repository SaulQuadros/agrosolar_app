from __future__ import annotations

import streamlit as st

from src.ui.theme import inject_css
from src.tools.formatting import brl
from src.core.calculators import estimate_pv_kwp, roi_simple
from src.tools.config_loader import load_config

def render() -> None:
    cfg = load_config()
    inject_css()

    st.title("Simulador (didático)")
    st.caption("Estimativas simplificadas para fins educacionais. Não substitui projeto e dimensionamento técnico.")
    st.markdown(
        """
<div class="ag-panel">
  <div class="ag-small-title">Objetivo</div>
  <p style="margin: 6px 0 0 0;">
    Simular ordem de grandeza de consumo, custo mensal na rede e payback para apoiar conversa comercial inicial.
  </p>
</div>
        """,
        unsafe_allow_html=True,
    )

    st.subheader("Entradas principais")
    c1, c2, c3 = st.columns(3)
    with c1:
        pump_power_kw = st.number_input("Potência da bomba (kW)", min_value=0.1, value=0.75, step=0.05)
        hours_per_day = st.number_input("Horas/dia de operação", min_value=0.5, value=4.0, step=0.5)
    with c2:
        days_per_month = st.number_input("Dias/mês de operação", min_value=1, value=25, step=1)
        grid_price = st.number_input("Tarifa de energia (R$/kWh)", min_value=0.10, value=0.95, step=0.05)
    with c3:
        psh = st.number_input("PSH (h) — horas de sol pico", min_value=1.0, value=5.0, step=0.5)
        eff = st.number_input("Eficiência do sistema (0–1)", min_value=0.30, max_value=0.95, value=0.75, step=0.05)

    st.subheader("Investimento e manutenção")
    c4, c5 = st.columns(2)
    with c4:
        investment = st.number_input("Investimento estimado (R$)", min_value=500.0, value=9000.0, step=500.0)
    with c5:
        maint = st.number_input("Manutenção mensal (R$)", min_value=0.0, value=30.0, step=10.0)

    st.divider()

    pv_kwp = estimate_pv_kwp(pump_power_kw, hours_per_day, psh, eff)
    roi = roi_simple(pump_power_kw, hours_per_day, int(days_per_month), grid_price, investment, maint)

    st.subheader("Resultados")
    r1, r2, r3 = st.columns(3)
    with r1:
        st.metric("Energia mensal estimada", f"{roi.monthly_energy_kwh:,.0f} kWh".replace(",", "."))
    with r2:
        st.metric("Custo mensal na rede", brl(roi.monthly_cost_grid_brl))
    with r3:
        st.metric("PV recomendado (kWp)", f"{pv_kwp:.2f} kWp")

    monthly_saving = roi.monthly_cost_grid_brl - maint
    if roi.payback_months is None:
        st.warning(
            "Payback não calculado. Para calcular, a economia mensal precisa ser maior que zero: "
            "`custo mensal na rede - manutenção mensal > 0`."
        )
        st.info(
            f"Com os valores atuais: custo na rede = {brl(roi.monthly_cost_grid_brl)} e manutenção = {brl(maint)}. "
            f"Economia estimada = {brl(monthly_saving)}."
        )
        st.caption(
            "Para obter payback, aumente consumo/tarifa da rede ou reduza manutenção/investimento."
        )
    else:
        st.success(f"Payback estimado: **{roi.payback_months:.1f} meses** (~{roi.payback_months/12:.1f} anos).")

    st.divider()
    st.markdown(
        """
<div class="ag-blueprint">
  <h4 style="margin:0 0 8px 0; color:#f8fbff;">Próximo passo comercial</h4>
  <p style="margin:0; color:#d8e6f4;">
    Com os dados acima, você já pode solicitar uma proposta com opções Essencial, Profissional e Fazenda.
  </p>
</div>
        """,
        unsafe_allow_html=True,
    )
    st.link_button("Solicitar orçamento", cfg.google_form_url, use_container_width=True)

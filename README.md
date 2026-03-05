# AgroSolar (Template) — App Streamlit de Marketing + Orçamento (Canva + Forms)

Este repositório é um **template didático** em Python/Streamlit para apoiar a disciplina de Administração e Economia:
- **Canva Website** continua sendo a *vitrine principal* (landing page).
- **Google Forms** é o canal de **solicitação de orçamento**.
- O **Streamlit** entra como um **APP complementar**: reforça a oferta, apresenta pacotes, inclui um simulador simples e organiza leads (opcional via upload CSV).

> ✅ Hospedagem sugerida: **Streamlit Community Cloud** (sem Cloud Run).

---

## 1) Rodar localmente

```bash
python -m venv .venv
# Windows: .venv\Scripts\activate
# Linux/Mac: source .venv/bin/activate

pip install -r requirements.txt
streamlit run app.py
```

---

## 2) Publicar no Streamlit Community Cloud

1. Suba este projeto para um repositório no GitHub
2. Acesse Streamlit Community Cloud e clique em **New app**
3. Selecione o repositório e o arquivo **app.py**
4. Configure variáveis/links em **Secrets** (opcional, recomendado)

---

## 3) Configuração (links do Canva, Google Forms e WhatsApp)

Você pode editar em `config/app_config.py` (valores padrão) **ou** definir via `st.secrets`.

Crie um arquivo (local) `.streamlit/secrets.toml` (não versionar) seguindo `secrets.example.toml`.

Exemplos de campos:
- `company_name`
- `canva_website_url`
- `google_form_url`
- `whatsapp_url`
- `contact_email`

---

## 4) Google Forms (orçamento)

No Canva, você pode usar um botão “Solicitar orçamento” apontando para o Forms.
No Streamlit, a página **Orçamento** tenta **embutir o Forms** via iframe:
- Se seu link for do tipo `.../viewform`, o app converte automaticamente para `.../viewform?embedded=true`.

---

## 5) Leads (opcional)

A página **Leads** aceita upload de CSV exportado do Google Forms/Sheets.
- Você consegue filtrar e acompanhar em um funil simples: Novo → Contato → Proposta → Fechado/Perdido.

> Dica didática: peça aos alunos para exportarem as respostas do Forms para CSV e testarem o painel.

---

## Estrutura de pastas

```text
agrosolar_streamlit_app/
  app.py
  pages/
  src/
    ui/
    core/
    forms/
    tools/
  config/
  data/
  .streamlit/
```

---

## Aviso

As contas, preços e simuladores são **educacionais** e usam hipóteses simplificadas.

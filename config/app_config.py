from __future__ import annotations

from dataclasses import dataclass

@dataclass(frozen=True)
class AppConfig:
    company_name: str = "AgroSolar Engenharia (Demo)"
    tagline: str = "Bombeamento solar para irrigação • Venda • Instalação • Manutenção • Peças"
    canva_website_url: str = "https://exemplo.com/seu-canva-website"
    google_form_url: str = "https://docs.google.com/forms/d/e/SEU-ID/viewform"
    whatsapp_url: str = "https://wa.me/55DDDN%C3%9AMERO?text=Ol%C3%A1!%20Quero%20um%20or%C3%A7amento%20para%20bombeamento%20solar."
    contact_email: str = "contato@exemplo.com"

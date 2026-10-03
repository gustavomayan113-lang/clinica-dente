"""Contextos globais de template (dados institucionais compartilhados)."""

from django.conf import settings
from django.utils import timezone

from . import content


def site(request):
    clinic = dict(content.CLINIC)
    clinic.update(
        {
            "phone_link": f"tel:+{clinic['phone_link']}",
            "whatsapp_link": f"https://wa.me/{clinic['whatsapp_link']}",
            "year": timezone.now().year,
        }
    )

    # Páginas cujo topo é escuro: o cabeçalho precisa inverter as cores.
    hero_dark = request.path.rstrip("/") in {"/servicos", "/equipe", "/contato"}

    return {
        "clinic": clinic,
        "nav": content.NAV,
        "socials": content.SOCIALS,
        "hours": content.OPENING_HOURS,
        "portfolio_note": content.PORTFOLIO_NOTE,
        "seo_default": settings.SEO_DEFAULT,
        "static_url": settings.STATIC_URL,
        "site_servicos": content.SERVICES[:5],
        "hero_dark": hero_dark,
    }
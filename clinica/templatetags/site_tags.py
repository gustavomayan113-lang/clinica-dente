"""Tags e filtros de template do site institucional."""

from django import template
from django.conf import settings
from django.utils.safestring import mark_safe

register = template.Library()

# Ícones em traço (stroke) — 24x24, currentColor
STROKE_ICONS = {
    "arrow-right": ["M4 12h15", "M13 6l6 6-6 6"],
    "arrow-up-right": ["M7 17 17 7", "M8.5 7H17v8.5"],
    "chevron-left": ["M15 5l-7 7 7 7"],
    "chevron-right": ["M9 5l7 7-7 7"],
    "close": ["M6 6l12 12", "M18 6 6 18"],
    "check": ["M4.5 12.5 9.5 17.5 19.5 6.5"],
    "check-circle": [
        "M12 21a9 9 0 1 0 0-18 9 9 0 0 0 0 18Z",
        "m8.2 12.2 2.6 2.6 5-5.4",
    ],
    "phone": [
        "M7.5 3h3l1.4 3.6-2 1.4a12.2 12.2 0 0 0 6.1 6.1l1.4-2 3.6 1.4v3a2 2 0 0 1-2.2 2A17.2 17.2 0 0 1 5.5 5.2 2 2 0 0 1 7.5 3Z"
    ],
    "mail": [
        "M4 6.5h16a1.5 1.5 0 0 1 1.5 1.5v8a1.5 1.5 0 0 1-1.5 1.5H4A1.5 1.5 0 0 1 2.5 16V8A1.5 1.5 0 0 1 4 6.5Z",
        "m3 7.5 9 6 9-6",
    ],
    "map-pin": [
        "M12 21.2s7-6.3 7-11.2a7 7 0 1 0-14 0c0 4.9 7 11.2 7 11.2Z",
        "M12 12.6a2.6 2.6 0 1 0 0-5.2 2.6 2.6 0 0 0 0 5.2Z",
    ],
    "clock": ["M12 21a9 9 0 1 0 0-18 9 9 0 0 0 0 18Z", "M12 7.5V12l3.4 2"],
    "star": ["m12 3.6 2.5 5.2 5.7.8-4.1 4 1 5.7-5.1-2.8-5.1 2.8 1-5.7-4.1-4 5.7-.8Z"],
    "quote": [
        "M9.6 6.4C7 7.5 5.5 9.8 5.5 12.8c0 2.6 1.5 4.4 3.6 4.4 1.8 0 3.1-1.3 3.1-3 0-1.7-1.2-2.9-2.7-2.9-.3 0-.6 0-.8.1.3-1.3 1.3-2.5 2.8-3.3Zm8.1 0c-2.6 1.1-4.1 3.4-4.1 6.4 0 2.6 1.5 4.4 3.6 4.4 1.8 0 3.1-1.3 3.1-3 0-1.7-1.2-2.9-2.7-2.9-.3 0-.6 0-.8.1.3-1.3 1.3-2.5 2.8-3.3Z"
    ],
    "ear": [
        "M7 9.2a5 5 0 0 1 10 0c0 2.6-1.9 3.4-3.1 4.4-1 1-1.3 1.8-1.3 3a2.5 2.5 0 0 1-5 0",
        "M11 9.4a1.2 1.2 0 0 1 2.4 0",
    ],
    "scan": [
        "M4 9V6a2 2 0 0 1 2-2h3",
        "M20 9V6a2 2 0 0 0-2-2h-3",
        "M4 15v3a2 2 0 0 0 2 2h3",
        "M20 15v3a2 2 0 0 1-2 2h-3",
        "M4 12h16",
    ],
    "scan3d": ["M12 3.2 20 7.6v8.8L12 20.8 4 16.4V7.6Z", "M12 3.2v17.6", "M20 7.6 12 12 4 7.6"],
    "shield": ["M12 3.2 19 5.8v5.6c0 4-2.9 7.4-7 8.6-4.1-1.2-7-4.6-7-8.6V5.8Z", "m8.8 12 2.2 2.2 4.2-4.4"],
    "sparkle": [
        "M12 3.2 13.7 8l4.8 1.7-4.8 1.7L12 16.2 10.3 11.4 5.5 9.7 10.3 8Z",
        "M18.6 14.6l.8 2.1 2.1.8-2.1.8-.8 2.1-.8-2.1-2.1-.8 2.1-.8Z",
    ],
    "plan": ["M6 3.5h8l4 4v13H6Z", "M14 3.5V8h4", "M9 12.5h6", "M9 16.5h4"],
    "monitor": [
        "M4 5h16a1 1 0 0 1 1 1v9a1 1 0 0 1-1 1H4a1 1 0 0 1-1-1V6a1 1 0 0 1 1-1Z",
        "M9 20.5h6",
        "M12 16.5v4",
    ],
    "card": [
        "M3 8.5h18",
        "M4.5 5.5h15A1.5 1.5 0 0 1 21 7v10a1.5 1.5 0 0 1-1.5 1.5h-15A1.5 1.5 0 0 1 3 17V7a1.5 1.5 0 0 1 1.5-1.5Z",
        "M7 14.5h4",
    ],
    "aligner": ["M4 6.2c0 7 3.6 11.8 8 11.8s8-4.8 8-11.8", "M8.2 8.4v2.8", "M12 9v3.2", "M15.8 8.4v2.8"],
    "implant": ["M12 3.5v4.2", "M9 7.7h6", "M12 7.7c-1.9 0-3 1.3-3 2.7 0 1.6 1.2 2.2 1.5 3.8.3 1.7.2 3.5.5 5.3", "M12 7.7c1.9 0 3 1.3 3 2.7 0 1.6-1.2 2.2-1.5 3.8-.3 1.7-.2 3.5-.5 5.3"],
    "tooth": [
        "M7.6 3.6c2.4-1 3.4 1 4.4 1s2-2 4.4-1c1.9.8 2.6 2.6 2.6 4.6 0 3.4-1.6 4.6-2.3 8.2-.5 2.6-1 3.6-2.2 3.6-1.6 0-1.4-2.4-2.5-4.6-1.1 2.2-.9 4.6-2.5 4.6-1.2 0-1.7-1-2.2-3.6C6.6 13.8 5 12.6 5 9.2c0-2 .7-3.8 2.6-4.6Z"
    ],
    "play": ["M8.5 5.8 18 12l-9.5 6.2Z"],
    "calendar": [
        "M4.5 6.5h15a1 1 0 0 1 1 1V19a1 1 0 0 1-1 1h-15a1 1 0 0 1-1-1V7.5a1 1 0 0 1 1-1Z",
        "M8 3.5v4",
        "M16 3.5v4",
        "M3.5 11h17",
    ],
    "smile": [
        "M12 21a9 9 0 1 0 0-18 9 9 0 0 0 0 18Z",
        "M8.5 14c.8 1.4 2 2.2 3.5 2.2s2.7-.8 3.5-2.2",
        "M9 9.5h.01",
        "M15 9.5h.01",
    ],
}

# Ícones preenchidos (fill) — redes sociais e WhatsApp
FILL_ICONS = {
    "instagram": [
        "M12 2.2c-2.7 0-3 0-4.1.1-1 0-1.8.2-2.4.5-.7.2-1.2.6-1.8 1.1S2.6 5 2.4 5.6c-.3.6-.4 1.3-.5 2.4C1.8 9 1.8 9.4 1.8 12s0 3 .1 4.1c0 1 .2 1.8.5 2.4.2.7.6 1.2 1.1 1.8s1.1.9 1.8 1.1c.6.3 1.3.4 2.4.5 1.1.1 1.4.1 4.1.1s3 0 4.1-.1c1 0 1.8-.2 2.4-.5.7-.2 1.2-.6 1.8-1.1s.9-1.1 1.1-1.8c.3-.6.4-1.3.5-2.4.1-1.1.1-1.4.1-4.1s0-3-.1-4.1c0-1-.2-1.8-.5-2.4-.2-.7-.6-1.2-1.1-1.8s-1.1-.9-1.8-1.1c-.6-.3-1.3-.4-2.4-.5C15 2.2 14.7 2.2 12 2.2Zm0 1.8c2.7 0 2.9 0 4 .1.9 0 1.4.2 1.7.3.4.2.7.4 1 .7.3.3.5.6.7 1 .1.3.3.8.3 1.7.1 1.1.1 1.3.1 4s0 2.9-.1 4c0 .9-.2 1.4-.3 1.7-.2.4-.4.7-.7 1-.3.3-.6.5-1 .7-.3.1-.8.3-1.7.3-1.1.1-1.3.1-4 .1s-2.9 0-4-.1c-.9 0-1.4-.2-1.7-.3-.4-.2-.7-.4-1-.7-.3-.3-.5-.6-.7-1-.1-.3-.3-.8-.3-1.7-.1-1.1-.1-1.3-.1-4s0-2.9.1-4c0-.9.2-1.4.3-1.7.2-.4.4-.7.7-1 .3-.3.6-.5 1-.7.3-.1.8-.3 1.7-.3 1.1-.1 1.3-.1 4-.1Zm0 3a5 5 0 1 0 0 10 5 5 0 0 0 0-10Zm0 8.2a3.2 3.2 0 1 1 0-6.4 3.2 3.2 0 0 1 0 6.4Zm6.4-8.4a1.2 1.2 0 1 1-2.4 0 1.2 1.2 0 0 1 2.4 0Z"
    ],
    "facebook": [
        "M13.6 21.8v-8.3h2.8l.4-3.2h-3.2V8.4c0-.9.3-1.6 1.6-1.6h1.7V3.9c-.3 0-1.3-.1-2.5-.1-2.5 0-4.2 1.5-4.2 4.3v2.4H7.5v3.2h2.7v8.1Z"
    ],
    "linkedin": [
        "M4.5 9.3h4.1v11.2H4.5Zm2.1-5.6a2.4 2.4 0 1 1 0 4.8 2.4 2.4 0 0 1 0-4.8ZM10.9 9.3H15v1.5a4.6 4.6 0 0 1 4.1-2.2c3.1 0 4.4 2 4.4 5.4v6.5h-4.1v-6c0-1.5-.5-2.6-1.9-2.6-1.1 0-1.7.7-2 1.4-.1.2-.1.6-.1.9v6.3h-4.4Z"
    ],
    "whatsapp": [
        "M12.04 2C6.6 2 2.2 6.4 2.2 11.8c0 1.7.4 3.3 1.2 4.8L2 22l5.5-1.4a9.8 9.8 0 0 0 4.5 1.2h.01c5.44 0 9.84-4.4 9.84-9.84 0-2.6-1-5.05-2.86-6.9A9.76 9.76 0 0 0 12.04 2Zm0 17.9h-.01a8.2 8.2 0 0 1-4.13-1.13l-.3-.18-3.1.82.83-3-.2-.3a8.1 8.1 0 0 1-1.24-4.3c0-4.47 3.66-8.1 8.16-8.1 2.18 0 4.22.85 5.76 2.4a8.1 8.1 0 0 1 2.39 5.7c0 4.46-3.67 8.1-8.16 8.1Zm4.48-6.05c-.24-.12-1.45-.71-1.67-.79-.22-.08-.39-.12-.55.12-.16.25-.63.8-.77.96-.14.17-.28.19-.53.06-.24-.12-1.03-.38-1.96-1.21-.73-.65-1.22-1.44-1.36-1.69-.14-.24-.02-.37.11-.5.1-.1.24-.28.36-.42.12-.15.16-.25.24-.41.09-.17.04-.31-.02-.44-.06-.12-.55-1.32-.74-1.8-.2-.48-.39-.42-.54-.43h-.46c-.16 0-.41.06-.63.3-.21.25-.83.81-.83 1.97s.85 2.28.97 2.44c.12.16 1.66 2.64 4.03 3.6.56.24 1 .39 1.34.5.57.18 1.08.15 1.49.1.45-.07 1.45-.6 1.65-1.17.2-.57.2-1.05.14-1.16-.05-.1-.22-.17-.46-.29Z"
    ],
}


@register.simple_tag
def icon(name, size=24, cls=""):
    """Retorna um ícone SVG inline (traço ou preenchido)."""
    size = int(size)

    if name in FILL_ICONS:
        paths = "".join(f'<path d="{d}"/>' for d in FILL_ICONS[name])
        return mark_safe(
            f'<svg class="icon {cls}" width="{size}" height="{size}" viewBox="0 0 24 24" '
            f'fill="currentColor" aria-hidden="true" focusable="false">{paths}</svg>'
        )

    paths = "".join(
        f'<path d="{d}" fill="none" stroke="currentColor" stroke-width="1.6" '
        f'stroke-linecap="round" stroke-linejoin="round"/>'
        for d in STROKE_ICONS.get(name, STROKE_ICONS["sparkle"])
    )
    return mark_safe(
        f'<svg class="icon {cls}" width="{size}" height="{size}" viewBox="0 0 24 24" '
        f'fill="none" aria-hidden="true" focusable="false">{paths}</svg>'
    )


@register.simple_tag
def img(path, alt="", css_class="", width=None, height=None, loading="lazy"):
    """Tag <img> de imagem estática com acessibilidade e performance."""
    attrs = []
    if css_class:
        attrs.append(f'class="{css_class}"')
    attrs.append(f'src="{settings.STATIC_URL}img/{path}"')
    attrs.append(f'alt="{alt}"')
    if width:
        attrs.append(f'width="{width}"')
    if height:
        attrs.append(f'height="{height}"')
    if loading:
        attrs.append(f'loading="{loading}"')
    attrs.append('decoding="async"')
    return mark_safe(f'<img {" ".join(attrs)}>')


@register.simple_tag
def logo(size=38, cls=""):
    """Marca da clínica (dente + feixe de luz) em SVG."""
    return mark_safe(
        f'<svg class="brand__mark {cls}" width="{size}" height="{size}" viewBox="0 0 48 48" '
        f'fill="none" aria-hidden="true" focusable="false">'
        f'<rect width="48" height="48" rx="15" fill="url(#luminaGrad)"/>'
        f'<path d="M15.6 13.6c2.6-1.1 3.7 1.1 4.8 1.1s2.2-2.2 4.8-1.1c2.1.9 2.8 2.9 2.8 5.1 0 3.7-1.7 5-2.5 8.9-.5 2.8-1.1 3.9-2.4 3.9-1.7 0-1.5-2.6-2.7-5-1.2 2.4-1 5-2.7 5-1.3 0-1.9-1.1-2.4-3.9-.8-3.9-2.5-5.2-2.5-8.9 0-2.2.7-4.2 2.8-5.1Z" fill="#fff"/>'
        f'<path d="M24 6.5v3.2M16.5 8l1.6 2.4M31.5 8l-1.6 2.4" stroke="#fff" '
        f'stroke-width="1.7" stroke-linecap="round" opacity=".85"/>'
        f'<defs><linearGradient id="luminaGrad" x1="0" y1="0" x2="48" y2="48" '
        f'gradientUnits="userSpaceOnUse"><stop stop-color="#2563EB"/>'
        f'<stop offset="1" stop-color="#38BDF8"/></linearGradient></defs></svg>'
    )


@register.filter
def get_item(value, key):
    """Acesso a dicionários por variável em templates."""
    try:
        return value[key]
    except (KeyError, IndexError, TypeError):
        return None


@register.filter
def split_lines(value):
    """Divide um texto em linhas preservando quebras explícitas."""
    return str(value).split("\n")


@register.simple_tag(takes_context=True)
def page_class(context, name, current):
    """Retorna uma classe CSS quando a página atual corresponde ao esperado."""
    return name if context.get("page") == current else ""


@register.simple_tag
def stars(count, size=16):
    """Sequência de estrelas para avaliações."""
    markup = "".join(
        f'<svg width="{size}" height="{size}" viewBox="0 0 24 24" fill="currentColor" '
        f'aria-hidden="true"><path d="{STROKE_ICONS["star"][0]}"/></svg>'
        for _ in range(int(count))
    )
    return mark_safe(f'<span class="rating" role="img" aria-label="{count} de 5 estrelas">{markup}</span>')
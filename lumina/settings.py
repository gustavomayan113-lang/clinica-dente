"""
Configurações do projeto — Clínica Odontológica Lumina (projeto de portfólio).

Site institucional fictício, sem banco de dados: todo o conteúdo vive em
`clinica/content.py` e é renderizado por templates.
"""

import mimetypes
import os

from pathlib import Path

# fonts servidos com o tipo correto pelo staticfiles em desenvolvimento
mimetypes.add_type("font/woff2", ".woff2")
mimetypes.add_type("image/webp", ".webp")

BASE_DIR = Path(__file__).resolve().parent.parent

# Em desenvolvimento use um valor local (ex.: "dev-local"). Nunca versionar segredos.
SECRET_KEY = os.environ.get(
    "DJANGO_SECRET_KEY",
    "django-insecure-lumina-portfolio-ficticio-nao-use-em-producao-real",
)

# DJANGO_DEBUG=0 ativa as páginas de erro 404/500 personalizadas.
# Rode com `runserver --insecure` para o Django continuar servindo os arquivos estáticos.
DEBUG = os.environ.get("DJANGO_DEBUG", "1") == "1"

ALLOWED_HOSTS = ["*"]
CSRF_TRUSTED_ORIGINS = [
    "http://localhost:8000",
    "http://127.0.0.1:8000",
    "https://lumina-odontologia.example.com",
]

INSTALLED_APPS = [
    "django.contrib.staticfiles",
    "clinica",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "lumina.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.request",
                "clinica.context_processors.site",
            ],
        },
    },
]

WSGI_APPLICATION = "lumina.wsgi.application"

# Projeto sem banco de dados.
DATABASES: dict = {}

AUTH_PASSWORD_VALIDATORS: list = []

LANGUAGE_CODE = "pt-br"
TIME_ZONE = "America/Sao_Paulo"
USE_I18N = True
USE_TZ = True

STATIC_URL = "static/"
STATICFILES_DIRS = [BASE_DIR / "static"]
STATIC_ROOT = BASE_DIR / "staticfiles"

STORAGES = {
    "default": {"BACKEND": "django.core.files.storage.FileSystemStorage"},
    "staticfiles": {"BACKEND": "django.contrib.staticfiles.storage.StaticFilesStorage"},
}

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

X_FRAME_OPTIONS = "SAMEORIGIN"

# Identidade da clínica fictícia
SITE = {
    "name": "Lumina",
    "legal_name": "Clínica Odontológica Lumina",
    "tagline": "Odontologia com luz",
}

SEO_DEFAULT = {
    "title": "Lumina Odontologia Integral | Clínica Odontológica em Alphaville",
    "description": (
        "Clínica odontológica digital em Alphaville: Harmonização orofacial, "
        "implantes, aparelho invisível e tratamento infantil. Atendimento "
        "humanizado, estrutura aconchegante e resultados que transformam sorrisos."
    ),
    "keywords": (
        "clínica odontológica, dentista em Alphaville, harmonização orofacial, "
        "implante dentário, aparelho invisível, clareamento dental"
    ),
}
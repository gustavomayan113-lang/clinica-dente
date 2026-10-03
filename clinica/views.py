"""Views do site institucional.

Não há banco de dados: o formulário de agendamento valida os dados e responde
em memória (POST-redirect-GET ou JSON quando enviado via fetch).
"""

import re

from django.http import JsonResponse
from django.shortcuts import redirect, render

from . import content

EMAIL_RE = re.compile(r"^[^@\s]+@[^@\s]+\.[a-z]{2,}$", re.IGNORECASE)
PHONE_RE = re.compile(r"^[\d\s()+-]{8,20}$")
MIN_NOME = 2
MIN_MENSAGEM = 10


def home(request):
    return render(
        request,
        "home.html",
        {
            "page": "home",
            "hero_badges": content.HERO_BADGES,
            "credentials": content.CREDENTIALS,
            "about": content.ABOUT,
            "features": content.FEATURES,
            "journey": content.JOURNEY,
            "tech": content.TECH,
            "services": content.SERVICES,
            "services_featured": [s for s in content.SERVICES if s["featured"]],
            "team": content.TEAM,
            "testimonials": content.TESTIMONIALS,
            "gallery": content.GALLERY,
            "faq": content.FAQ,
            "stats": content.STATS,
            "newsletter": content.NEWSLETTER,
        },
    )


def servicos(request):
    return render(
        request,
        "servicos.html",
        {
            "page": "servicos",
            "services": content.SERVICES,
            "faq": content.FAQ,
            "newsletter": content.NEWSLETTER,
        },
    )


def servico_detalhe(request, slug: str):
    servico = content.servico_por_slug(slug)
    if servico is None:
        return pagina_inexistente(request, exception=None)
    outros = [s for s in content.SERVICES if s["slug"] != slug][:3]
    return render(
        request,
        "servico_detalhe.html",
        {
            "page": "servicos",
            "servico": servico,
            "outros": outros,
            "faq": content.FAQ[:3],
            "newsletter": content.NEWSLETTER,
        },
    )


def equipe(request):
    return render(
        request,
        "equipe.html",
        {
            "page": "equipe",
            "team": content.TEAM,
            "tech": content.TECH,
            "stats": content.STATS,
            "testimonials": content.TESTIMONIALS[:3],
        },
    )


def _validar_agendamento(dados: dict) -> dict:
    """Valida o formulário e devolve um dicionário de erros por campo."""
    erros: dict[str, str] = {}

    nome = (dados.get("nome") or "").strip()
    email = (dados.get("email") or "").strip()
    telefone = (dados.get("telefone") or "").strip()
    assunto = (dados.get("assunto") or "").strip()
    preferencia = (dados.get("preferencia") or "").strip()
    mensagem = (dados.get("mensagem") or "").strip()

    if len(nome) < MIN_NOME:
        erros["nome"] = "Conte seu nome para a equipe conseguir te chamar."
    if not EMAIL_RE.match(email):
        erros["email"] = "Confira o e-mail: parece faltar alguma coisa."
    if not PHONE_RE.match(telefone):
        erros["telefone"] = "Informe um telefone com DDD para confirmarmos."
    if not assunto:
        erros["assunto"] = "Escolha o assunto do seu contato."
    if not preferencia:
        erros["preferencia"] = "Prefere manhã ou tarde para vir?"
    if not mensagem:
        erros["mensagem"] = "Conte um pouco do que você precisa."

    return {
        "erros": erros,
        "valido": not erros,
        "dados": {
            "nome": nome,
            "email": email,
            "telefone": telefone,
            "assunto": assunto,
            "preferencia": preferencia,
            "mensagem": mensagem,
        },
    }


def contato(request):
    contexto = {
        "page": "contato",
        "subjects": content.FORM_SUBJECTS,
        "times": content.FORM_TIMES,
        "enviado": False,
        "form": {},
        "erros": {},
    }

    if request.method == "POST":
        resultado = _validar_agendamento(request.POST)
        contexto["erros"] = resultado["erros"]
        contexto["form"] = resultado["dados"]

        ajax = request.headers.get("X-Requested-With") == "fetch"

        if resultado["valido"]:
            # Sem banco de dados: em produção este ponto enviaria o e-mail
            # (Django EmailBackend) ou integraria com uma agenda externa.
            if ajax:
                return JsonResponse(
                    {
                        "ok": True,
                        "mensagem": (
                            f"Recebemos seu contato, {resultado['dados']['nome'].split()[0]}. "
                            "A equipe responde em até 1 dia útil."
                        ),
                    }
                )
            return redirect(f"{request.path}?enviado=1#formulario")

        if ajax:
            return JsonResponse(
                {"ok": False, "erros": resultado["erros"]}, status=400
            )

    if request.GET.get("enviado") == "1":
        contexto["enviado"] = True

    return render(request, "contato.html", contexto)


def pagina_inexistente(request, exception=None):
    return render(request, "404.html", {"page": "404"}, status=404)


def erro_servidor(request):
    return render(request, "500.html", {"page": "500"}, status=500)
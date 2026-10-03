"""Testes de fumaça do site institucional (sem banco de dados)."""

import re

from django.shortcuts import render
from django.test import Client, SimpleTestCase, override_settings
from django.urls import reverse

from . import content


class PaginasTest(SimpleTestCase):
    def test_home_responde_com_conteudo_essencial(self):
        response = self.client.get(reverse("clinica:home"))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Lumina")
        self.assertContains(response, "hero-principal.webp")
        self.assertContains(response, "Escaneamento 3D")

    def test_paginas_internas_respondem(self):
        rotas = [
            reverse("clinica:servicos"),
            reverse("clinica:equipe"),
            reverse("clinica:contato"),
        ]
        for rota in rotas:
            with self.subTest(rota=rota):
                self.assertEqual(self.client.get(rota).status_code, 200)

    def test_detalhe_de_cada_servico(self):
        for servico in content.SERVICES:
            with self.subTest(servico=servico["slug"]):
                response = self.client.get(
                    reverse("clinica:servico_detalhe", args=[servico["slug"]])
                )
                self.assertEqual(response.status_code, 200)
                self.assertContains(response, servico["title"])

    def test_slug_desconhecido_cai_no_404(self):
        response = self.client.get("/servicos/nao-existe/")
        self.assertEqual(response.status_code, 404)

    @override_settings(DEBUG=False)
    def test_404_customizado(self):
        response = self.client.get("/rota-inexistente/")
        self.assertEqual(response.status_code, 404)
        self.assertContains(response, "Essa página sorriu para outro lugar", status_code=404)

    def test_pagina_500_renderiza(self):
        response = render(self.client.request().wsgi_request, "500.html")
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Algo travou por aqui", response.content)


class FormularioTest(SimpleTestCase):
    dados_validos = {
        "nome": "Ana Beatriz Moreira",
        "email": "ana@example.com",
        "telefone": "(11) 98888-7777",
        "assunto": content.FORM_SUBJECTS[0],
        "preferencia": content.FORM_TIMES[0],
        "mensagem": "Gostaria de agendar uma avaliação de alinhadores.",
    }

    def test_formulario_invalido_mantem_a_pagina_e_marca_erros(self):
        response = self.client.post(reverse("clinica:contato"), data={"nome": "A"})

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "has-error")

    def test_formulario_valido_redireciona(self):
        response = self.client.post(reverse("clinica:contato"), data=self.dados_validos)

        self.assertEqual(response.status_code, 302)
        self.assertIn("enviado=1", response["Location"])

    def test_formulario_via_fetch_retorna_json(self):
        response = self.client.post(
            reverse("clinica:contato"),
            data=self.dados_validos,
            headers={"x-requested-with": "fetch"},
        )

        self.assertEqual(response.status_code, 200)
        payload = response.json()
        self.assertTrue(payload["ok"])
        self.assertIn("Ana", payload["mensagem"])

    def test_formulario_via_fetch_devolve_erros_por_campo(self):
        response = self.client.post(
            reverse("clinica:contato"),
            data={"nome": "", "email": "invalido"},
            headers={"x-requested-with": "fetch"},
        )

        self.assertEqual(response.status_code, 400)
        erros = response.json()["erros"]
        self.assertIn("nome", erros)
        self.assertIn("email", erros)


class AcessibilidadeTest(SimpleTestCase):
    def test_imagens_tem_alt_e_lazy_loading(self):
        html = self.client.get(reverse("clinica:home")).content.decode()

        imagens = re.findall(r"<img\b[^>]*>", html)
        self.assertGreater(len(imagens), 20)

        # Só o placeholder do lightbox pode ter alt vazio
        sem_alt = [tag for tag in imagens if 'alt=""' in tag]
        self.assertEqual(len(sem_alt), 1, sem_alt)
        self.assertIn('class="lightbox"', html)  # placeholder fica no lightbox

        self.assertIn('loading="lazy"', html)
        self.assertIn("Pular para o conteúdo", html)

    def test_html_nao_contem_tags_de_template(self):
        html = self.client.get(reverse("clinica:home")).content.decode()

        for residuo in ("{%", "{{", "</script>{%"):
            self.assertNotIn(residuo, html)

    def test_navegacao_presente_em_todas_as_paginas(self):
        client = Client()
        for rota in (
            reverse("clinica:home"),
            reverse("clinica:servicos"),
            reverse("clinica:equipe"),
            reverse("clinica:contato"),
        ):
            with self.subTest(rota=rota):
                self.assertContains(client.get(rota), 'aria-label="Navegação principal"')
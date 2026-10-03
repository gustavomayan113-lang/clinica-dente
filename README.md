# Clínica Odontológica Lumina

Site institucional de uma clínica odontológica **fictícia**, construído em Django sem banco de dados.
Projeto de portfólio com foco em identidade visual azul/branco, layout responsivo, animações avançadas
de rolagem e acessibilidade.

> ⚠️ **Projeto fictício.** Clínica, CRO-SP, profissionais, depoimentos, telefones, CNPJ e imagens de
> apoio não representam nenhuma clínica real e não têm vínculo com o CRO. Conteúdo apenas demonstrativo.

## Stack

| Camada        | Tecnologia                                                        |
| ------------- | ----------------------------------------------------------------- |
| Backend       | Django 6.1 (Python 3.13) — sem models, sem banco de dados          |
| Templates     | Django Template Language + tags/filters próprios                  |
| Animações     | GSAP 3.15 (ScrollTrigger, CustomEase) + Lenis 1.3                 |
| Estilos       | CSS puro em camadas (`base`, `components`, `layout`, `pages`, `motion`) |
| Tipografia    | Sora, Inter e Instrument Serif em `.woff2` locais                  |
| Imagens       | WebP locais (37 arquivos), sem imagens externas                   |

## Como executar

Requer Python 3.13+ (testado em 3.13.9) e Node 18+ apenas para re-gerar fontes/imagens.

```bash
# 1. Dependências Python
python -m venv .venv
.venv\Scripts\activate            # Windows: .venv\Scripts\activate
pip install -r requirements.txt

# 2. Servidor de desenvolvimento
python manage.py runserver         # http://127.0.0.1:8000
```

Não há migrations, fixtures nem comandos de carga: todo o conteúdo é estático em Python.

### Páginas de erro personalizadas

Por padrão `DEBUG=1`, então o Django mostra a página de debug em vez das telas 404/500.
Para visualizar as versões finais do projeto:

```bash
# PowerShell
$env:DJANGO_DEBUG="0"; python manage.py runserver 8001 --insecure

# bash / zsh
DJANGO_DEBUG=0 python manage.py runserver 8001 --insecure
```

`--insecure` mantém o servidor servindo `static/` com `DEBUG=False`. Em produção use whitenoise
ou o servidor de arquivos do seu provedor.

### Testes e checagens

```bash
python manage.py check             # checagem de configuração
python manage.py test              # 13 testes: páginas, 404/500, formulário e acessibilidade
```

## Estrutura

```
clinica-odontologia-portifolio/
├── clinica/                  app único
│   ├── content.py            TODO o conteúdo (clínica, serviços, equipe, FAQ, depoimentos…)
│   ├── views.py              views, validação do formulário e resposta via fetch
│   ├── urls.py               rotas da clínica
│   ├── context_processors.py SEO, navegação, estado de hero e globals
│   ├── templatetags/
│   │   └── site_tags.py      icon, img, logo, page_class, stars e filtros
│   └── tests.py              suíte de testes
├── lumina/                   projeto Django (settings, urls, wsgi, asgi)
├── templates/
│   ├── base.html             shell, SEO, preloader, lightbox e structured data
│   ├── home.html  servicos.html  servico_detalhe.html
│   ├── equipe.html  contato.html
│   ├── 404.html  500.html
│   └── partials/             header, footer, menu mobile e preloader
├── static/
│   ├── css/                  base, components, layout, pages, motion, fonts
│   ├── js/                   main.js (interações) e animations.js (GSAP)
│   ├── fonts/                Sora, Inter, Instrument Serif (.woff2)
│   ├── img/                  WebP locais por contexto
│   └── vendor/               GSAP e Lenis vendorizados (sem CDN)
└── tools/fetch-fonts.mjs     utilitário que baixa os .woff2 das fontes
```

## Rotas

| Rota                                | View            | Conteúdo                                    |
| ----------------------------------- | --------------- | ------------------------------------------- |
| `/`                                 | `home`          | Institutional completa                     |
| `/servicos/`                        | `servicos`      | Listagem dos 8 tratamentos                  |
| `/servicos/<slug>/`                 | `servico_detalhe` | Detalhe de cada tratamento                |
| `/equipe/`                          | `equipe`        | Equipe de especialistas                     |
| `/contato/`                         | `contato`       | Contato, mapa, horários e FAQ              |
| qualquer rota inexistente           | `handler404`    | Página 404 da clínica                       |
| erro não tratado                    | `handler500`    | Página 500 da clínica                       |

## Personalização

Quase tudo é conteúdo, não código. Edite `clinica/content.py`:

- `CLINIC` — nome, CRO, CNPJ, endereço, telefone, WhatsApp, e-mail, Instagram e ano de fundação;
- `SERVICES` — os 8 tratamentos (`slug`, `title`, `short`, `intro`, `text`, `items`, `duration`,
  `price`, `image`, `featured`);
- `TEAM` (4 especialistas), `TESTIMONIALS` (6 depoimentos), `FAQ` (7 perguntas), `GALLERY` (9 fotos),
  `STATS`, `FEATURES`, `JOURNEY`, `ABOUT`, `CREDENTIALS`, `OPENING_HOURS`, `SOCIALS`;
- `NAV`, `HERO_BADGES`, `FORM_SUBJECTS`, `FORM_TIMES`, `NEWSLETTER`, `TECH`, `PORTFOLIO_NOTE`.

Cores, tipografia e espaçamentos ficam em `static/css/base.css` (custom properties no topo do arquivo).

## Detalhes técnicos

- **Sem banco de dados**: os serviços, a equipe e o FAQ são dicionários Python; não há `models.py`.
- **Formulário de contato**: valida no servidor (nome, telefone, e-mail, assunto, mensagem e aceite)
  e responde em JSON quando a requisição traz o cabeçalho `X-Requested-With: fetch`, com degradação
  para POST-redirect-GET sem JavaScript. Nada é persistido — o ponto de integração está marcado
  em `clinica/views.py`.
- **Animações**: GSAP + ScrollTrigger + Lenis com `gsap.ticker` sincronizado. Split-text em títulos,
  reveals, parallax, pin horizontal da seção de serviços e contadores animados.
- **Acessibilidade**: `prefers-reduced-motion` desliga as animações; o HTML continua legível sem
  JavaScript (classe `.no-gsap` garante opacidade 1); foco visível, `aria-*` nos componentes
  interativos e landmarks semânticos.
- **SEO**: metatags Open Graph e Twitter Card, canonical e JSON-LD `Dentist` com endereço,
  coordenadas, horário de atendimento e avaliação agregada.
- **Performance**: fontes e imagens locais com `font-display: swap`, WebP dimensionadas, GSAP e Lenis
  vendorizados (nenhuma requisição a CDN em produção).

## Créditos e licenças

- **GSAP**, **ScrollTrigger** e **CustomEase**: GreenSock — licença padrão da GSAP.
  **Lenis**: Darkroom Engineering, licença MIT.
- **Imagens**: fotografias de apoio do [StockSnap](https://stocksnap.io) (CC0) e do
  [Unsplash](https://unsplash.com) (licença Unsplash), convertidas para WebP.
- **Fontes**: Sora, Inter e Instrument Serif, obtidas via [Google Fonts](https://fonts.google.com)
  e salvas em `static/fonts/` pelo script `tools/fetch-fonts.mjs`.

Nenhum recurso externo é carregado em tempo de execução: o projeto funciona offline após a instalação.
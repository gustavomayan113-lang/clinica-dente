"""Conteúdo editorial da Clínica Odontológica Lumina.

Projeto de portfólio: clínica, profissionais, serviços e depoimentos são
fictícios. Nenhum dado é persistido — tudo é estático e servido por views.
"""

CLINIC = {
    "name": "Lumina",
    "full_name": "Clínica Odontológica Lumina",
    "signature": "Odontologia Integral",
    "tagline": "Ciência e afeto no mesmo sorriso.",
    "founded": "2016",
    "cro": "CRO-SP 128.440",
    "cnpj": "41.882.907/0001-33",
    "email": "ola@lumina.odontologia.com.br",
    "phone": "(11) 4003-8922",
    "phone_link": "+551140038922",
    "whatsapp": "(11) 99123-4477",
    "whatsapp_link": "5511991234477",
    "address": "Av. Professor Walter Accordi, 855 — Jardim Esperança",
    "city": "Alphaville · Barueri — SP",
    "coords": "-23.5037, -46.8487",
    "instagram": "lumina.odontologia",
    "instagram_url": "https://instagram.com/",
    "instagram_followers": "12,4 mil",
    "since": "desde 2016",
}

OPENING_HOURS = [
    {"days": "Segunda a sexta", "hours": "08h00 — 19h00"},
    {"days": "Sábado", "hours": "08h00 — 14h00"},
    {"days": "Domingo", "hours": "Somente urgências"},
]

NAV = [
    {"label": "Início", "href": "/#inicio"},
    {"label": "A clínica", "href": "/#clinica"},
    {"label": "Tratamentos", "href": "/servicos/"},
    {"label": "Equipe", "href": "/equipe/"},
    {"label": "Depoimentos", "href": "/#depoimentos"},
    {"label": "Contato", "href": "/contato/"},
]

SOCIALS = [
    {"label": "Instagram", "icon": "instagram", "url": "https://instagram.com/"},
    {"label": "Facebook", "icon": "facebook", "url": "https://facebook.com/"},
    {"label": "LinkedIn", "icon": "linkedin", "url": "https://linkedin.com/"},
    {"label": "WhatsApp", "icon": "whatsapp", "url": "https://wa.me/5511991234477"},
]

STATS = [
    {"value": 12400, "suffix": "+", "label": "sorrisos acompanhados desde 2016"},
    {"value": 4.9, "decimals": 1, "suffix": "/5", "label": "em 312 avaliações verificadas"},
    {"value": 18, "suffix": "", "label": "especialistas na equipe clínica"},
    {"value": 98, "suffix": "%", "label": "dos pacientes recomendam a Lumina"},
]

HERO_BADGES = [
    {"value": "4,9/5", "label": "312 avaliações"},
    {"value": "48h", "label": "para a primeira consulta"},
    {"value": "100%", "label": "digital, do scan ao sorriso"},
]

CREDENTIALS = [
    "CRO-SP 128.440",
    "Escaneador intraoral 3D",
    "Tomografia cone-beam própria",
    "Esterilização classe D",
    "Selo Sorriso Kids",
    "Convênios e reembolso dental",
    "Pix e parcelamento em até 12x",
    "Alphaville · Barueri — SP",
]

ABOUT = {
    "eyebrow": "A clínica",
    "title": "Uma clínica feita para gente, não para pacientes.",
    "lead": (
        "A Lumina nasceu em 2016 com uma ideia simples: tratar dente não é tarefa de "
        "máquina. É diagnóstico, é tempo, é conversa. Nove anos depois, seguimos com o "
        "mesmo princípio — cada pessoa entra com uma história e sai com um plano."
    ),
    "paragraphs": [
        (
            "Reformamos uma sala de atendimento familiar em Alphaville e construímos uma "
            "clínica de consultórios integrados, com luz natural, cheiro de eucalipto e "
            "nada de barulho de motor na sala."
        ),
        (
            "Investimos em tecnologia que o paciente sente: escaneamento 3D dentro do "
            "consultório, tomografia própria, simulação digital do resultado antes de "
            "qualquer intervenção e prontuário digital completo."
        ),
    ],
    "signature": "Helena Vasconcelos",
    "role": "Fundadora e coordenadora clínica",
}

FEATURES = [
    {
        "index": "01",
        "icon": "ear",
        "title": "Escuta clínica real",
        "text": (
            "Cada consulta começa com 20 minutos de conversa sobre rotina, histórico e "
            "medo. Nada de protocolo corrido."
        ),
    },
    {
        "index": "02",
        "icon": "scan",
        "title": "Digital de ponta a ponta",
        "text": (
            "Scan intraoral, tomografia 3D e simulação de resultado entregues antes de "
            "qualquer procedimento."
        ),
    },
    {
        "index": "03",
        "icon": "shield",
        "title": "Nada de surpresa",
        "text": (
            "Orçamento em PDF com valores, prazo e alternativas. Você aprova antes de "
            "começar — por escrito."
        ),
    },
    {
        "index": "04",
        "icon": "sparkle",
        "title": "Conforto que se sente",
        "text": (
            "Maca com massagem, ruído branco, sedação consciente e café da manhã para a "
            "criança sair feliz."
        ),
    },
]

JOURNEY = [
    {
        "number": "01",
        "icon": "ear",
        "title": "Escuta",
        "text": "Conversa de 20 minutos sobre o que incomoda, o que já tentou e o que você teme.",
        "detail": "Sem custo · 20 min",
    },
    {
        "number": "02",
        "icon": "scan",
        "title": "Diagnóstico",
        "text": "Scan intraoral, tomografia 3D e fotografias registrados no prontuário digital.",
        "detail": "Mesmo dia · 40 min",
    },
    {
        "number": "03",
        "icon": "plan",
        "title": "Plano",
        "text": "Você recebe de duas a três opções com preços fechados e a simulação do resultado.",
        "detail": "Arquivo em PDF · 24h",
    },
    {
        "number": "04",
        "icon": "sparkle",
        "title": "Sorriso",
        "text": "Execução por etapas, agenda flexível e acompanhamento por mensagem a cada 15 dias.",
        "detail": "Acompanhamento contínuo",
    },
]

TECH = [
    {
        "icon": "scan",
        "title": "Escaneamento 3D",
        "text": "Nada de molde de silicone: digital, em três minutos, com arquivo que vira planejamento.",
        "metric": "3 min",
    },
    {
        "icon": "scan3d",
        "title": "Tomografia cone-beam",
        "text": "Imagem 3D dentro da própria clínica, com radiologista avaliando o caso no mesmo dia.",
        "metric": "Dose baixa",
    },
    {
        "icon": "monitor",
        "title": "Simulação digital",
        "text": "Você vê o antes e o depois renderizado do seu próprio sorriso antes de decidir.",
        "metric": "48h",
    },
    {
        "icon": "shield",
        "title": "Esterilização classe D",
        "text": "Autoclave a vácuo, indicador químico a cada ciclo e rastreabilidade por lote.",
        "metric": "Classe D",
    },
    {
        "icon": "ear",
        "title": "Conforto sem medo",
        "text": "Ruído branco, massagem, sedação consciente e protocolo específico para fobia.",
        "metric": "Ansiedade zero",
    },
    {
        "icon": "card",
        "title": "Condições transparentes",
        "text": "Convênios, reembolso, Pix e parcelamento em até 12x sem juros.",
        "metric": "12x",
    },
]

SERVICES = [
    {
        "slug": "limpeza-preventiva",
        "number": "01",
        "icon": "sparkle",
        "title": "Prevenção e limpeza",
        "short": "Profilaxia, orientação de higiene e acompanhamento de cáries.",
        "intro": "A consulta mais importante da odontologia é a que ainda não dói.",
        "text": (
            "Higienização profissional com jato de bicarbonato, polimento profilático e "
            "orientação individual de escovação, fio dental e irrigador. Monitoramos cáries e "
            "saúde gengival em ciclos de seis meses — antes de qualquer procedimento invasivo."
        ),
        "items": [
            "Higienização com jato de bicarbonato e polimento",
            "Detecção de cáries e sangramento gengival",
            "Orientação de higiene com escova e fio adequados",
            "Plano preventivo anual para você e sua família",
        ],
        "duration": "40 min",
        "price": "a partir de R$ 280",
        "image": "servicos/limpeza-preventiva.webp",
        "featured": True,
    },
    {
        "slug": "clareamento-dental",
        "number": "02",
        "icon": "sparkle",
        "title": "Clareamento dental",
        "short": "Whitening em consultório e kits domésticos com molde individual.",
        "intro": "Mais branco, sempre sem desgastar o esmalte.",
        "text": (
            "Protocolo em consultório com gel de peróxido em concentrações controladas, "
            "complementado por kit de uso doméstico. Avaliamos tom de partida, sensibilidade "
            "e restaurações existentes para definir quantos tons são realistas no seu caso — "
            "sem prometer o que a saúde do dente não permite."
        ),
        "items": [
            "Avaliação de tom com guia e fotografia",
            "Whitening em consultório em sessão única",
            "Kits domésticos com molde individual",
            "Controle de sensibilidade e reposição de flúor",
        ],
        "duration": "90 min",
        "price": "a partir de R$ 690",
        "image": "servicos/clareamento-dental.webp",
        "featured": True,
    },
    {
        "slug": "aparelho-invisivel",
        "number": "03",
        "icon": "aligner",
        "title": "Aparelho invisível",
        "short": "Alinhadores transparentes para adulto, adolescente e caso complexo.",
        "intro": "Alinhar os dentes sem parar a sua vida.",
        "text": (
            "Planejamento 3D dos alinhadores, com cada etapa renderizada a partir do seu "
            "escaneamento. Você acompanha a evolução pelo aplicativo, troca os marcadores "
            "a cada sete a dez dias e usa o alinhador de 20 a 22 horas por dia. Sem aparelho "
            "fixo e sem metal no rosto."
        ),
        "items": [
            "Escaneamento e planejamento 3D sem moldes",
            "Simulação do resultado antes de fabricar",
            "Marcadores trocados a cada 7 a 10 dias",
            "Acompanhamento por mensagem e consulta de controle",
        ],
        "duration": "12 a 18 meses",
        "price": "a partir de R$ 4.900",
        "image": "servicos/aparelho-invisivel.webp",
        "featured": True,
    },
    {
        "slug": "implantes-dentarios",
        "number": "04",
        "icon": "implant",
        "title": "Implantes dentários",
        "short": "Reposição de dentes perdidos com planejamento digital e carga imediata.",
        "intro": "Voltar a mastigar sem esperar meses.",
        "text": (
            "Implantes de titânio com planejamento guiado por tomografia 3D, carga imediata "
            "quando o caso permite e prótese em zircônia feita em CAD/CAM. Analisamos osso, "
            "gengiva e histórico para definir número, posição e tempo de cicatrização com "
            "segurança."
        ),
        "items": [
            "Planejamento guiado por tomografia 3D",
            "Carga imediata quando o caso permite",
            "Prótese em zircônia ou resina CAD/CAM",
            "Manutenção preventiva a cada 6 meses",
        ],
        "duration": "3 a 6 meses",
        "price": "sob avaliação",
        "image": "servicos/implantes-dentarios.webp",
        "featured": True,
    },
    {
        "slug": "harmonizacao-orofacial",
        "number": "05",
        "icon": "sparkle",
        "title": "Harmonização orofacial",
        "short": "Botox, preenchimento e estética avançada planejada no seu rosto.",
        "intro": "Expressão natural, proporcionada, sem máscara.",
        "text": (
            "Planejamos com fotografia e análise de proporção: linhas de expressão, volume "
            "labial, sorriso gengival e contorno mandibular. Protocolos conservadores, com "
            "produtos selecionados e rastreabilidade por lote. Nada de estourar o resultado — "
            "é o seu rosto, não um modelo pronto."
        ),
        "items": [
            "Avaliação facial com fotografia e vídeo",
            "Botox e preenchimento com rastreabilidade",
            "Planejamento de sorriso gengival",
            "Manutenção a cada 4 a 6 meses",
        ],
        "duration": "60 min",
        "price": "a partir de R$ 1.200",
        "image": "servicos/harmonizacao-orofacial.webp",
        "featured": True,
    },
    {
        "slug": "endodontia-com-microscopia",
        "number": "06",
        "icon": "scan",
        "title": "Endodontia com microscopia",
        "short": "Tratamento de canal sob microscópio e instrumentação digital.",
        "intro": "Salvar o dente é quase sempre possível.",
        "text": (
            "Sob microscópio, o canal é mapeado canal por canal — isso aumenta a taxa de "
            "sucesso e reduz a dor. Indicamos canal ou outro caminho apenas com evidência: "
            "a magnificação mostra exatamente onde a infecção está."
        ),
        "items": [
            "Mapeamento dos canais com microscópio",
            "Instrumentação digital e obturação tridimensional",
            "Diagnóstico de dor orofacial",
            "Retratamento de casos de outros consultórios",
        ],
        "duration": "1 a 2 sessões",
        "price": "a partir de R$ 980",
        "image": "servicos/microscopia-endodontica.webp",
        "featured": False,
    },
    {
        "slug": "odontopediatria",
        "number": "07",
        "icon": "sparkle",
        "title": "Odontopediatria",
        "short": "Primeira consulta sem medo, com o selo Sorriso Kids.",
        "intro": "A primeira visita não precisa ser um trauma.",
        "text": (
            "Consultas curtas, brincadeira, música e tempo sem pressa: a criança conhece o "
            "consultório antes de qualquer instrumento. Selantes, flúor, raspagem e orientação "
            "para os pais em linguagem simples. E, quando é preciso, existe sedação consciente "
            "para os casos mais ansiosos."
        ),
        "items": [
            "Consulta de acolhimento sem aparelho",
            "Selantes, flúor e raspagem escolar",
            "Orientação de escovação para os responsáveis",
            "Sedação consciente para casos ansiosos",
        ],
        "duration": "30 min",
        "price": "a partir de R$ 220",
        "image": "servicos/odontopediatria.webp",
        "featured": False,
    },
    {
        "slug": "reabilitacao-oral",
        "number": "08",
        "icon": "implant",
        "title": "Reabilitação oral",
        "short": "Reconstrução de dentes desgastados, função e estética em um único plano.",
        "intro": "Voltar a comer e sorrir com segurança.",
        "text": (
            "Para quem perdeu vários dentes ou desgasta os dentes há anos: análise funcional "
            "de articulação e oclusão, reabilitação em fases e próteses sobre implantes ou "
            "dentes naturais. Um plano, um cronograma, um orçamento."
        ),
        "items": [
            "Análise funcional de articulação e oclusão",
            "Reabilitação em fases com próteses provisórias",
            "Overdentures e próteses fixas sobre implantes",
            "Acompanhamento de manutenção a longo prazo",
        ],
        "duration": "3 a 12 meses",
        "price": "sob avaliação",
        "image": "servicos/reabilitacao-oral.webp",
        "featured": False,
    },
]

TEAM = [
    {
        "slug": "helena-vasconcelos",
        "name": "Helena Vasconcelos",
        "role": "Harmonização orofacial",
        "cro": "CRO-SP 128.440",
        "image": "equipe/helena-vasconcelos.webp",
        "short": "Fundadora da Lumina e especialista em estética e função.",
        "bio": (
            "Formada em Odontologia pela USP em 2008 e especializada em Harmonização "
            "Orofacial. É responsável pela coordenação clínica e pelos protocolos de "
            "planejamento digital que viraram marca da casa."
        ),
        "education": [
            "Odontologia — Universidade de São Paulo (USP)",
            "Harmonização Orofacial — FOM",
            "Pós-graduação em DOR Orofacial — UNIFESP",
        ],
        "focus": ["Harmonização", "Estética", "Planejamento digital"],
    },
    {
        "slug": "rafael-montealegre",
        "name": "Rafael Montealegre",
        "role": "Implantes e reabilitação",
        "cro": "CRO-SP 154.902",
        "image": "equipe/rafael-montealegre.webp",
        "short": "Cuida dos casos de implante e reabilitação com carga imediata.",
        "bio": (
            "Especialista em Implantodontia e certificado em sistema de implantes. "
            "Referência da equipe no planejamento cirúrgico guiado por tomografia 3D."
        ),
        "education": [
            "Odontologia — UNIFESP",
            "Implantodontia — APCE",
            "Cirurgia avançada — Straumann",
        ],
        "focus": ["Implantes", "Carga imediata", "Zircônia"],
    },
    {
        "slug": "camila-aoki",
        "name": "Camila Aoki",
        "role": "Odontopediatria e ortodontia",
        "cro": "CRO-SP 176.331",
        "image": "equipe/camila-aoki.webp",
        "short": "Transforma a consulta da criança em uma aventura leve.",
        "bio": (
            "Pediatra-dentista formada pela UNIFESP, com formação em sedação consciente e "
            "ortodontia interceptiva. Conduz o selo Sorriso Kids da Lumina desde 2019."
        ),
        "education": [
            "Odontologia — UNIFESP",
            "Odontopediatria — ABO São Paulo",
            "Sedação consciente — Hospital Sírio-Libanês",
        ],
        "focus": ["Crianças", "Sorriso Kids", "Sedação"],
    },
    {
        "slug": "bruno-tavares",
        "name": "Bruno Tavares",
        "role": "Endodontia e microscopia",
        "cro": "CRO-SP 132.775",
        "image": "equipe/bruno-tavares.webp",
        "short": "Trabalha sob microscópio: mais precisão, menos dor.",
        "bio": (
            "Endodontista há mais de doze anos, atua com microscopia operatoria e "
            "ultrassom. É o responsável pelos casos complexos que chegam de outros "
            "consultórios."
        ),
        "education": [
            "Odontologia — USP Ribeirão Preto",
            "Endodontia — ABO São Paulo",
            "Microscopia operatoria — TESE",
        ],
        "focus": ["Microscopia", "Retratamento", "Dor orofacial"],
    },
]

TESTIMONIALS = [
    {
        "name": "Ana Beatriz Moreira",
        "role": "Alphaville · paciente há 4 anos",
        "quote": (
            "Cheguei com medo de dentista desde a infância. Hoje me explicaram cada som, "
            "me deram tempo e nunca apressaram nada. Hoje sou eu que indico a Lumina."
        ),
        "rating": 5,
        "image": "depoimentos/ana.webp",
    },
    {
        "name": "Rafael Nogueira",
        "role": "Alinhadores invisíveis · 2025",
        "quote": (
            "Vi a simulação do meu próprio sorriso antes de fabricar o primeiro marcador. "
            "Foi exatamente o que veio. Catorze meses, três fotos de antes e depois."
        ),
        "rating": 5,
        "image": "depoimentos/rafael.webp",
    },
    {
        "name": "Joana Prado",
        "role": "Harmonização orofacial",
        "quote": (
            "A Dra. Helena não quis mudar minha expressão, quis devolver a minha. "
            "Meus amigos acharam que eu tinha dormido bem por uma semana."
        ),
        "rating": 5,
        "image": "depoimentos/joana.webp",
    },
    {
        "name": "Marcos Vinícius Alves",
        "role": "Implante com carga imediata",
        "quote": (
            "Perdi dois dentes num acidente. Saí do consultório com a prótese provisória "
            "no mesmo dia. O orçamento veio fechado, como prometiam."
        ),
        "rating": 5,
        "image": "depoimentos/marcos.webp",
    },
    {
        "name": "Luíza Campos",
        "role": "Mãe da Esther, 6 anos",
        "quote": (
            "Minha filha saiu perguntando quando volta. Nunca imaginei ouvir isso de uma "
            "consulta dentária — e ela já fez a segunda."
        ),
        "rating": 5,
        "image": "depoimentos/luiza.webp",
    },
    {
        "name": "Daniele Ferraz",
        "role": "Retratamento de canal",
        "quote": (
            "Outro dentista tinha descartado meu dente. O Dr. Bruno abriu sob microscópio "
            "e mostrou onde era a infecção. Dente salvo e sem dor."
        ),
        "rating": 5,
        "image": "depoimentos/daniele.webp",
    },
]

GALLERY = [
    {"image": "galeria/01.webp", "caption": "Consultório 2 — luz natural da manhã", "tag": "Consultórios"},
    {"image": "galeria/02.webp", "caption": "Sala de tomografia cone-beam", "tag": "Tecnologia"},
    {"image": "galeria/03.webp", "caption": "Maca com massagem e ruído branco", "tag": "Conforto"},
    {"image": "galeria/04.webp", "caption": "Mesa de materiais esterilizados", "tag": "Biossegurança"},
    {"image": "galeria/05.webp", "caption": "Copos de escovação para pequenos", "tag": "Sorriso Kids"},
    {"image": "galeria/06.webp", "caption": "Recepção com café e música", "tag": "Recepção"},
    {"image": "galeria/07.webp", "caption": "Atendimento guiado por imagem", "tag": "Consulta"},
    {"image": "galeria/08.webp", "caption": "Centro cirúrgico e recuperação", "tag": "Cirurgia"},
    {"image": "galeria/09.webp", "caption": "Detalhe da unidade de ortodontia", "tag": "Ortodontia"},
]

FAQ = [
    {
        "question": "A primeira consulta tem custo?",
        "answer": (
            "A conversa inicial e o plano de tratamento são gratuitos. Apenas os exames "
            "complementares — escaneamento, tomografia ou exames de laboratório — são "
            "cobrados, e o valor é informado antes do agendamento."
        ),
    },
    {
        "question": "Quanto tempo demora para ver o resultado de um aparelho invisível?",
        "answer": (
            "Nos alinhadores você costuma perceber mudança nas primeiras quatro a seis "
            "semanas, mas o tratamento completo leva de 12 a 18 meses. No clareamento em "
            "consultório, o resultado aparece na primeira sessão."
        ),
    },
    {
        "question": "Vocês atendem crianças? Qual é a idade mínima?",
        "answer": (
            "Sim. A partir de três anos fazemos a consulta de acolhimento — sem aparelho, "
            "só conhecimento e confiança. O selo Sorriso Kids reúne protocolos de manejo do "
            "medo, com sedação consciente quando necessário."
        ),
    },
    {
        "question": "Aceitam convênio ou reembolso?",
        "answer": (
            "Trabalhamos com os principais convênios odontológicos da região e também com "
            "reembolso em saúde. O atendimento particular pode ser parcelado em até 12x."
        ),
    },
    {
        "question": "E se eu tiver medo de dentista?",
        "answer": (
            "Faz parte — e é mais comum do que você imagina. Fazemos uma consulta de "
            "acomodação sem procedimento, usamos ruído branco, massagem e, se necessário, "
            "sedação consciente conduzida por profissional habilitado."
        ),
    },
    {
        "question": "Vocês atendem urgências no mesmo dia?",
        "answer": (
            "Sim. Há reserva de agenda diária para urgências — dor, trauma ou inchaço. "
            "Basta ligar para (11) 4003-8922 ou escrever no WhatsApp que a equipe te atende rápido."
        ),
    },
    {
        "question": "Como funcionam o pagamento e o orçamento?",
        "answer": (
            "Você recebe um PDF com as opções de tratamento, valores fechados e prazo de "
            "cada etapa. Nada começa sem sua aprovação por escrito, nem em caso de urgência."
        ),
    },
]

NEWSLETTER = {
    "title": "Carta de luz",
    "text": (
        "Um e-mail por mês com verdade odontológica: sem clickbait e sem medo. "
        "Dicas de higiene, novidades da clínica e horários."
    ),
    "placeholder": "seu@email.com.br",
    "button": "Quero receber",
    "note": "Sem spam. Um e-mail por mês, cancele quando quiser.",
}

PORTFOLIO_NOTE = (
    "Projeto de portfólio: clínica, profissionais, imagens de apoio e depoimentos são "
    "fictícios. Desenvolvido com Django, GSAP e Lenis."
)

FORM_SUBJECTS = [
    "Primeira consulta",
    "Tratamento ortodôntico",
    "Implantes",
    "Harmonização orofacial",
    "Criança / Sorriso Kids",
    "Urgência",
    "Convênio e reembolso",
    "Outro assunto",
]

FORM_TIMES = [
    "Manhã (8h — 12h)",
    "Tarde (12h — 17h)",
    "Fim de tarde (17h — 20h)",
    "Sábado",
]


def servico_por_slug(slug: str) -> dict | None:
    for item in SERVICES:
        if item["slug"] == slug:
            return item
    return None


def equipe_por_slug(slug: str) -> dict | None:
    for item in TEAM:
        if item["slug"] == slug:
            return item
    return None
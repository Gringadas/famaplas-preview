#!/usr/bin/env python3
"""Gera o site estático da Famaplás em ./site a partir dos dados abaixo.

Rodar:  python3 build.py
PREVIEW = True coloca noindex em todas as páginas e bloqueia o robots.txt.
Trocar para False só quando o site for para o domínio oficial.
"""
from pathlib import Path
from html import escape
from urllib.parse import quote
import json

PREVIEW = True
DOMAIN = "https://www.famaplas.com.br"
OUT = Path(__file__).parent / "site"

WA_NUMBER = "5511989833238"
PHONE_1 = ("(11) 2601-6881", "+551126016881")
PHONE_2 = ("(11) 2606-1166", "+551126061166")
EMAIL = "famaplas@famaplas.com"
ADDRESS = "Rua Madre de Deus, 683, Mooca, São Paulo/SP"
INSTAGRAM = "https://www.instagram.com/famaplas/"


def wa(msg: str) -> str:
    return f"https://wa.me/{WA_NUMBER}?text={quote(msg)}"


APLIC_FULL = ["Áreas internas e externas", "Decks de piscina e ambientes", "Escritórios comerciais", "Palcos e espaços para eventos"]

# ------------------------------------------------------------------ produtos
PRODUTOS = [
    dict(
        slug="pedestal-para-piso-elevado", old="pedestal-para-piso-elevado.html",
        nome="Pedestal para Piso Elevado", curto="Pedestal completo",
        grupo="pedestal", img=["pedestal", "pedestal-2", "pedestal-3", "pedestal-4"],
        resumo="O conjunto completo que sustenta o piso: regulável, certificado pela ABNT e livre de oxidação.",
        texto=[
            "O piso elevado cria um vão livre entre o piso e o contrapiso para a passagem de cabeamento, encanamento e dutos de ar-condicionado. O pedestal é a peça que decide se esse piso fica firme, nivelado e fácil de manter por anos.",
            "A Famaplás fabrica os próprios pedestais em polipropileno, com tecnologia de injeção própria e resistência certificada pela norma ABNT. O material não oxida, então o conjunto mantém a mesma regulagem com o passar do tempo.",
            "Cada pedestal é montado a partir de componentes que se combinam conforme a altura do projeto: apoio da placa, porca niveladora, base, prolongador, tubo de acoplamento, base para tubo e porca base.",
        ],
        monta=["apoio-da-placa", "porca-niveladora", "base-para-pedestal", "prolongador", "tubo-de-acoplamento", "porca-base"],
        monta_label="Composto por",
        aplic=APLIC_FULL,
        destaques=["Certificado pela norma ABNT", "Não oxida", "Altura regulável", "Fabricação própria"],
    ),
    dict(
        slug="apoio-da-placa", old="apoio-da-placa-piso-elevado.html",
        nome="Apoio da Placa para Piso Elevado", curto="Apoio da placa",
        grupo="componente", img=["apoio", "apoio-2"],
        resumo="O topo do pedestal: reforço completo e rosca dupla para manter as placas niveladas.",
        texto=[
            "É no apoio que a placa do piso descansa. O da Famaplás tem reforço completo e rosca dupla, produzido com tecnologia de injeção de última geração e 100% certificado pela norma ABNT.",
            "O resultado é resistência, durabilidade e nivelamento das placas mantido ao longo do tempo, sem oxidação.",
        ],
        regra="Uso obrigatório com porca niveladora e base. Conforme o projeto, também pode receber prolongador, porca base ou tubo de acoplamento com base para tubo.",
        monta=["porca-niveladora", "base-para-pedestal", "prolongador", "porca-base", "tubo-de-acoplamento"],
        aplic=APLIC_FULL,
        destaques=["Rosca dupla", "Reforço completo", "Certificado ABNT"],
    ),
    dict(
        slug="porca-niveladora", old="porca-niveladora-para-piso-elevado.html",
        nome="Porca Niveladora para Piso Elevado", curto="Porca niveladora",
        grupo="componente", img=["porca-niveladora", "porca-niveladora-2"],
        resumo="Ajuste milimétrico de altura e roscas de travamento que impedem o conjunto de girar.",
        texto=[
            "Depois de instalado, o conjunto não pode girar. A porca niveladora da Famaplás garante isso com roscas de travamento.",
            "A rosca dupla de entrada permite ajustar a altura e o nível do piso milímetro a milímetro, sempre que for preciso. Como todas as peças da linha, é certificada pela norma ABNT e não oxida.",
        ],
        regra="Uso obrigatório com o conjunto de peças do pedestal para piso elevado.",
        monta=["pedestal-para-piso-elevado", "apoio-da-placa", "base-para-pedestal"],
        aplic=APLIC_FULL,
        destaques=["Ajuste milimétrico", "Roscas de travamento", "Certificada ABNT"],
    ),
    dict(
        slug="base-para-pedestal", old="base-para-pedestal-de-piso-elevado.html",
        nome="Bases para Pedestal de Piso Elevado", curto="Bases",
        grupo="componente", img=["base", "base-2", "base-3"],
        resumo="Dois modelos de base, com formato pensado para encaixar até nas extremidades das paredes.",
        texto=[
            "A base é o ponto de contato do pedestal com o contrapiso. As da Famaplás são certificadas pela norma ABNT e têm formas que facilitam o encaixe, alcançando as extremidades das paredes durante a montagem.",
        ],
        modelos=[
            ("Base 02 (estrela)", "Para altura acabada de até 150 mm, ou alturas maiores com o uso de prolongadores. Tem dentes de travamento que impedem rotações não planejadas."),
            ("Base 03 (para tubo)", "Para alturas acima de 400 mm, sempre com o tubo de acoplamento."),
        ],
        regra="Monta com apoio da placa e porca niveladora. Em casos específicos, também com prolongador ou com tubo de acoplamento.",
        monta=["apoio-da-placa", "porca-niveladora", "prolongador", "tubo-de-acoplamento"],
        aplic=APLIC_FULL,
        destaques=["2 modelos", "Dentes de travamento", "Certificada ABNT"],
    ),
    dict(
        slug="prolongador", old="prolongador-para-pedestal-de-piso-elevado.html",
        nome="Prolongador para Pedestal de Piso Elevado", curto="Prolongador",
        grupo="componente", img=["prolongador", "prolongador-2"],
        resumo="Para projetos que pedem mais altura, com dentes de travamento que mantêm o piso estável.",
        texto=[
            "Alguns projetos precisam de um ajuste de altura específico. O prolongador resolve isso e, com seus dentes de travamento, garante a estabilidade do piso depois da aplicação completa.",
            "É produzido com certificação ABNT e em material que não oxida com o tempo.",
        ],
        regra="Monta com apoio da placa, porca niveladora e base.",
        monta=["apoio-da-placa", "porca-niveladora", "base-para-pedestal"],
        aplic=APLIC_FULL,
        destaques=["Ganho de altura", "Dentes de travamento", "Certificado ABNT"],
    ),
    dict(
        slug="tubo-de-acoplamento", old="tubo-de-acoplamento-de-pedestal-para-piso-elevado.html",
        nome="Tubo de Acoplamento para Pedestal de Piso Elevado", curto="Tubo de acoplamento",
        grupo="componente", img=["tubo", "tubo-2"],
        resumo="A solução para vãos grandes, quando a altura mínima do piso passa de 400 mm.",
        texto=[
            "Quando o vão entre o solo e o piso precisa ser maior, com altura mínima de 400 mm, o tubo de acoplamento é a melhor opção para elevar o pedestal.",
            "É feito em material de alta resistência, certificado pela norma ABNT, e garante segurança e estabilidade depois da instalação, sem oxidar.",
        ],
        regra="Uso obrigatório com apoio da placa, porca niveladora e base para tubo (Base 03).",
        monta=["apoio-da-placa", "porca-niveladora", "base-para-pedestal"],
        aplic=APLIC_FULL,
        destaques=["Acima de 400 mm", "Alta resistência", "Certificado ABNT"],
    ),
    dict(
        slug="porca-base", old="porca-base-pedestal-para-piso-elevado.html",
        nome="Porca Base para Pedestal de Piso Elevado", curto="Porca base",
        grupo="componente", img=["porca-base", "porca-base-2", "porca-base-3"],
        resumo="O pedestal mais baixo possível: só duas peças, para projetos com pouca fiação sob o piso.",
        texto=[
            "Desenvolvida pela Famaplás para aplicações específicas, a porca base permite pedestais de regulagem mínima.",
            "Com apenas duas peças, o apoio da placa e a porca base, forma um pedestal ideal para projetos com pouca fiação ou poucos materiais sob a placa.",
        ],
        regra="Monta com o apoio da placa.",
        monta=["apoio-da-placa"],
        aplic=["Áreas internas e externas", "Escritórios comerciais"],
        destaques=["Regulagem mínima", "Só 2 peças", "Desenvolvimento próprio"],
    ),
    dict(
        slug="piso-elevado-completo", old="piso-elevado-completo.html",
        nome="Piso Elevado Completo", curto="Piso elevado completo",
        grupo="sistema", img=["piso-elevado", "piso-elevado-2"],
        resumo="Placas e pedestais em um só fornecedor, com instalação feita pela equipe da Famaplás.",
        texto=[
            "O piso elevado da Famaplás é formado por suportes telescópicos (pedestais) de altura regulável e placas intercambiáveis de pedra natural laminada e calibrada, que entregam um acabamento uniforme.",
            "Também há placas em mármore e granito estruturadas em fiberglass (fibra de vidro) com resina, que ganham resistência à carga e são assentadas diretamente sobre os pedestais (sob consulta).",
            "Na prática: layout flexível, montagem e desmontagem rápidas, regulagem milimétrica de altura, quatro opções de pedestal, arremate preciso inclusive em paredes curvas e pilares, e pouca manutenção.",
        ],
        regra="Fornecido com placas e pedestais para piso elevado, o que reduz custo e aumenta a durabilidade do conjunto.",
        monta=["pedestal-para-piso-elevado", "apoio-da-placa", "porca-niveladora", "base-para-pedestal"],
        aplic=APLIC_FULL,
        destaques=["Placas e pedestais", "Instalação própria", "Laudos disponíveis"],
        specs=True,
    ),
    dict(
        slug="alcas-plasticas", old="alcas-plasticas.html",
        nome="Alças Plásticas", curto="Alças plásticas",
        grupo="embalagem", img=["alcas", "alcas-2"],
        resumo="Alças em polietileno de baixa densidade para caixas de papelão e embalagens de presente.",
        texto=[
            "Fabricadas em polietileno de baixa densidade, as alças da Famaplás seguem o mesmo padrão de qualidade e resistência da linha de pisos.",
            "São usadas em embalagens de papelão de vários produtos, como sapatos, panelas, toner, kits de vinho e brinquedos, e facilitam o transporte do produto pelo cliente final.",
            "Podem ser fabricadas em cores variadas. Consulte a disponibilidade.",
        ],
        monta=[],
        aplic=["Caixas de presente", "Caixas de papelão em geral"],
        destaques=["PEBD", "Cores sob consulta", "Multiuso"],
    ),
]
P = {p["slug"]: p for p in PRODUTOS}

SPECS = [
    ("Indicações", "Edifícios inteligentes, escritórios, centros de controle industrial, CPDs, lojas, escolas e áreas técnicas hospitalares"),
    ("Composição", "Placas de pedra natural e suportes telescópicos de polipropileno Famaplás"),
    ("Dimensões das placas", "600 × 600 × 25 mm (outras medidas conforme especificação)"),
    ("Altura do piso", "Mínima 6 cm, máxima 180 cm"),
    ("Acabamento final", "Carpete em placa, laminado, melamínico, vinílico, condutivo e outros, além do Famaplás Mármore e Granito"),
    ("Suportes telescópicos", "A norma ABNT exige 18.000 N. O pedestal Famaplás resiste a 20.740 N sem deformação"),
    ("Carga concentrada", "741 kg"),
    ("Carga distribuída", "1.800 kg/m²"),
    ("Flecha no centro da placa (carga de 440 kg)", "0,47 mm"),
    ("Peso do sistema (H até 200 mm)", "46 kg/m²"),
    ("Instalação", "Equipe Famaplás, média de 50 m² por dia por instalador"),
    ("Mudança de layout", "Basta retirar a placa e reposicionar"),
]

CLIENTES = [("cyrela", "Cyrela"), ("gafisa", "Gafisa"), ("even", "Even"), ("rossi", "Rossi"), ("camargo-correa", "Camargo Corrêa"),
            ("odebrech", "Odebrecht"), ("wtorre", "WTorre"), ("jhs", "JHSF"), ("rochavera", "Rochaverá"), ("sinco", "Sinco"),
            ("gail", "Gail"), ("encevix", "Engevix"), ("htf", "Hochtief"), ("marques", "Marques"), ("rochenback", "Rockenbach")]

NAV = [("/", "Início"), ("/sobre", "Sobre"), ("/produtos", "Produtos"), ("/aplicacoes", "Aplicações"), ("/calculadora", "Calculadora"), ("/contato", "Contato")]

# ------------------------------------------------------------------ peças de layout

LOGO = """<svg class="logo-mark" viewBox="0 0 66 40" aria-hidden="true"><path d="M0 0h29v8H8v7h17v8H8v17H0z"/><path fill-rule="evenodd" d="M33 0h24a9 9 0 0 1 9 9v13a9 9 0 0 1-9 9H41v9h-8zm8 8v15h15a2 2 0 0 0 2-2V10a2 2 0 0 0-2-2z"/></svg>"""


def logo(cls="logo"):
    return f'<a class="{cls}" href="/" aria-label="Famaplás, página inicial">{LOGO}<span class="logo-type"><span class="logo-name">FamaPlás</span><span class="logo-tag">Pisos elevados</span></span></a>'


def icon(name):
    paths = {
        "wa": '<path d="M12 2a10 10 0 0 0-8.6 15.1L2 22l5-1.3A10 10 0 1 0 12 2Zm0 18.2a8.2 8.2 0 0 1-4.2-1.2l-.3-.2-3 .8.8-2.9-.2-.3A8.2 8.2 0 1 1 12 20.2Zm4.5-6.1c-.2-.1-1.5-.7-1.7-.8-.2-.1-.4-.1-.6.1l-.8 1c-.1.2-.3.2-.5.1a6.7 6.7 0 0 1-3.3-2.9c-.2-.4.2-.4.7-1.3.1-.2 0-.3 0-.4l-.8-1.8c-.2-.5-.4-.4-.6-.4h-.5a1 1 0 0 0-.7.3 3 3 0 0 0-.9 2.2 5.2 5.2 0 0 0 1.1 2.7 11.8 11.8 0 0 0 4.5 4c1.7.7 2.3.8 3.2.6a2.7 2.7 0 0 0 1.8-1.2c.2-.6.2-1.1.2-1.2-.1-.1-.3-.2-.6-.3Z" fill="currentColor"/>',
        "arrow": '<path d="M5 12h14m-6-6 6 6-6 6" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="square"/>',
        "phone": '<path d="M6.6 10.8a15.1 15.1 0 0 0 6.6 6.6l2.2-2.2a1 1 0 0 1 1-.2 11.4 11.4 0 0 0 3.6.6 1 1 0 0 1 1 1V20a1 1 0 0 1-1 1A17 17 0 0 1 3 4a1 1 0 0 1 1-1h3.5a1 1 0 0 1 1 1c0 1.2.2 2.5.6 3.6a1 1 0 0 1-.3 1Z" fill="currentColor"/>',
        "mail": '<path d="M3 5h18v14H3z M3 6l9 7 9-7" fill="none" stroke="currentColor" stroke-width="1.8"/>',
        "pin": '<path d="M12 22s7-6.2 7-12a7 7 0 1 0-14 0c0 5.8 7 12 7 12Zm0-9.5a2.5 2.5 0 1 1 0-5 2.5 2.5 0 0 1 0 5Z" fill="currentColor"/>',
        "check": '<path d="m5 12 4.5 4.5L19 7" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="square"/>',
        "ig": '<rect x="3" y="3" width="18" height="18" rx="5" fill="none" stroke="currentColor" stroke-width="1.8"/><circle cx="12" cy="12" r="4" fill="none" stroke="currentColor" stroke-width="1.8"/><circle cx="17.3" cy="6.7" r="1.2" fill="currentColor"/>',
        "menu": '<path d="M3 7h18M3 12h18M3 17h18" stroke="currentColor" stroke-width="2"/>',
        "close": '<path d="M5 5l14 14M19 5 5 19" stroke="currentColor" stroke-width="2"/>',
        "down": '<path d="m6 9 6 6 6-6" fill="none" stroke="currentColor" stroke-width="2"/>',
    }
    return f'<svg class="i i-{name}" viewBox="0 0 24 24" width="20" height="20" aria-hidden="true">{paths[name]}</svg>'


def header(active):
    links = []
    for href, label in NAV:
        cur = ' aria-current="page"' if active == href else ""
        if href == "/produtos":
            sub = "".join(f'<li><a href="/produtos/{p["slug"]}">{escape(p["curto"])}</a></li>' for p in PRODUTOS)
            links.append(
                f'<li class="has-sub"><a href="/produtos"{cur}>Produtos</a>'
                f'<button class="sub-toggle" type="button" aria-expanded="false" aria-controls="sub-produtos" aria-label="Abrir lista de produtos">{icon("down")}</button>'
                f'<ul class="sub" id="sub-produtos">{sub}<li class="sub-all"><a href="/produtos">Ver catálogo completo</a></li></ul></li>')
        else:
            links.append(f'<li><a href="{href}"{cur}>{label}</a></li>')
    return f"""<a class="skip" href="#conteudo">Pular para o conteúdo</a>
<div class="topbar"><div class="wrap topbar-in">
  <span class="topbar-note">Fábrica própria na Mooca, São Paulo, desde 2003.</span>
  <span class="topbar-links"><a href="tel:{PHONE_1[1]}">{icon("phone")}{PHONE_1[0]}</a><a href="mailto:{EMAIL}">{icon("mail")}{EMAIL}</a></span>
</div></div>
<header class="site-header" id="topo">
  <div class="wrap header-in">
    {logo()}
    <nav class="nav" id="nav" aria-label="Principal">
      <ul class="nav-list">{''.join(links)}</ul>
      <a class="btn btn-sm btn-primary nav-cta" href="/orcamento" data-cta="header_orcamento">Pedir orçamento</a>
    </nav>
    <button class="menu-btn" type="button" aria-expanded="false" aria-controls="nav"><span class="sr">Menu</span>{icon("menu")}{icon("close")}</button>
  </div>
</header>"""


def _foot_cta():
    return f"""<div class="foot-cta" data-reveal>
      <p class="foot-cta-t">Tem um projeto de piso elevado? Mande as medidas e a altura, a gente responde com a composição e o orçamento.</p>
      <div class="foot-cta-a">
        <a class="btn btn-primary" href="/orcamento" data-cta="footer_orcamento">Pedir orçamento {icon("arrow")}</a>
        <a class="btn btn-ghost-dark" href="{wa('Olá! Vim pelo site da Famaplás e gostaria de falar com um atendente.')}" target="_blank" rel="noopener" data-cta="footer_whatsapp">{icon("wa")} WhatsApp</a>
      </div>
    </div>"""


FOOT_CTA = None


def footer(cta=True):
    foot_cta = _foot_cta() if cta else ""
    prods = "".join(f'<li><a href="/produtos/{p["slug"]}">{escape(p["curto"])}</a></li>' for p in PRODUTOS)
    return f"""<footer class="site-footer">
  <div class="wrap">
    {foot_cta}
    <div class="foot-grid">
      <div class="foot-brand">
        {logo("logo logo-inv")}
        <p>Pedestais para piso elevado, piso elevado completo e alças plásticas. Fabricação própria em São Paulo desde 2003.</p>
        <a class="foot-ig" href="{INSTAGRAM}" target="_blank" rel="noopener">{icon("ig")} @famaplas</a>
      </div>
      <div><p class="foot-h">Produtos</p><ul class="foot-list">{prods}</ul></div>
      <div><p class="foot-h">Empresa</p><ul class="foot-list">
        <li><a href="/sobre">Sobre a Famaplás</a></li><li><a href="/aplicacoes">Aplicações</a></li><li><a href="/calculadora">Calculadora de pedestais</a></li><li><a href="/#duvidas">Dúvidas frequentes</a></li>
        <li><a href="/produtos/piso-elevado-completo#ficha">Ficha técnica</a></li><li><a href="/orcamento">Orçamento</a></li><li><a href="/contato">Contato</a></li></ul></div>
      <div><p class="foot-h">Contato</p><ul class="foot-list foot-contact">
        <li><a href="tel:{PHONE_1[1]}">{PHONE_1[0]}</a></li><li><a href="tel:{PHONE_2[1]}">{PHONE_2[0]}</a></li>
        <li><a href="mailto:{EMAIL}">{EMAIL}</a></li><li>{ADDRESS}</li></ul></div>
    </div>
    <div class="foot-bottom"><span>© 2026 Famaplás Indústria e Comércio de Peças Plásticas</span><a href="#topo">Voltar ao topo</a></div>
  </div>
</footer>
<a class="wa-float" href="{wa('Olá! Vim pelo site da Famaplás e gostaria de um orçamento.')}" target="_blank" rel="noopener" data-cta="whatsapp_float" aria-label="Falar com a Famaplás pelo WhatsApp">{icon("wa")}<span>Orçamento pelo WhatsApp</span></a>"""


def page(path, title, desc, body, active=None, extra_head="", extra_js="", jsonld=None, og_img="/img/piso-escritorio.webp"):
    canonical = DOMAIN + (path if path != "/" else "/")
    robots = '<meta name="robots" content="noindex, nofollow">' if PREVIEW else ""
    ld = "".join(f'<script type="application/ld+json">{json.dumps(j, ensure_ascii=False)}</script>' for j in (jsonld or []))
    html = f"""<!doctype html>
<html lang="pt-BR">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{escape(title)}</title>
<meta name="description" content="{escape(desc)}">
{robots}
<link rel="canonical" href="{canonical}">
<meta property="og:type" content="website"><meta property="og:locale" content="pt_BR">
<meta property="og:title" content="{escape(title)}"><meta property="og:description" content="{escape(desc)}">
<meta property="og:url" content="{canonical}"><meta property="og:image" content="{DOMAIN}{og_img}">
<meta name="theme-color" content="#1b1d20">
<link rel="icon" href="/img/favicon.svg" type="image/svg+xml">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Archivo:wdth,wght@62..125,300..800&family=JetBrains+Mono:wght@400;500&display=swap" rel="stylesheet">
<link rel="stylesheet" href="/css/page-transition.css">
<link rel="stylesheet" href="/css/reveal-on-scroll.css">
<link rel="stylesheet" href="/css/image-tilt.css">
<link rel="stylesheet" href="/css/style.css">
<script src="/js/page-transition.js"></script>
<script>window.dataLayer = window.dataLayer || [];</script>
{extra_head}{ld}
</head>
<body>
{header(active)}
<main id="conteudo">
{body}
</main>
{footer("band-cta" not in body)}
<script src="/js/reveal-on-scroll.js" defer></script>
<script src="/js/image-tilt.js" defer></script>
<script src="/js/main.js" defer></script>
<script src="/js/wa-widget.js" defer></script>
{extra_js}
</body>
</html>
"""
    target = OUT / ("index.html" if path == "/" else path.strip("/") + ".html")
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(html, encoding="utf-8")
    return path


def crumbs(items):
    lis = "".join(
        f'<li><a href="{h}">{escape(t)}</a></li>' if h else f'<li aria-current="page">{escape(t)}</li>' for h, t in items)
    ld = {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": i + 1, "name": t, **({"item": DOMAIN + h} if h else {})} for i, (h, t) in enumerate(items)]}
    return f'<nav class="crumbs" aria-label="Você está em"><ol>{lis}</ol></nav>', ld


def card(p, eager=False):
    load = 'fetchpriority="high"' if eager else 'loading="lazy"'
    return f"""<a class="pcard" href="/produtos/{p['slug']}" data-tilt="4">
  <div class="pcard-img" data-tilt-inner><img src="/img/produtos/{p['img'][0]}.webp" alt="{escape(p['nome'])} Famaplás" width="481" height="478" {load} style="view-transition-name: p-{p['slug']}"></div>
  <div class="pcard-body"><span class="pcard-k">{ {'pedestal':'Sistema','componente':'Componente','sistema':'Solução completa','embalagem':'Embalagens'}[p['grupo']] }</span>
  <h3 class="pcard-t">{escape(p['curto'])}</h3><p class="pcard-d">{escape(p['resumo'])}</p>
  <span class="pcard-go">Ver produto {icon('arrow')}</span></div>
</a>"""


def numbers(dark=False):
    items = [("20.740 N", "de resistência por pedestal, sem deformação", "A norma ABNT exige 18.000 N"),
             ("741 kg", "de carga concentrada", "Ensaio Falcão Bauer"),
             ("1.800 kg/m²", "de carga distribuída", "Ensaio Falcão Bauer"),
             ("6 a 180 cm", "de altura de piso", "Com o mesmo sistema")]
    lis = "".join(f'<li><strong class="num">{a}</strong><span>{b}</span><small>{c}</small></li>' for a, b, c in items)
    return f'<ul class="numbers{" numbers-dark" if dark else ""}">{lis}</ul>'


def norma_bar():
    return """<figure class="norma" data-reveal>
  <figcaption><span class="eyebrow">Resistência por pedestal</span><span class="norma-note">Dados de ensaio Falcão Bauer. Laudos disponíveis sob solicitação.</span></figcaption>
  <div class="norma-row"><span class="norma-l">Exigência ABNT</span><div class="norma-track"><div class="norma-fill norma-abnt" style="--v:.868"></div></div><span class="norma-v">18.000 N</span></div>
  <div class="norma-row"><span class="norma-l">Pedestal Famaplás</span><div class="norma-track"><div class="norma-fill norma-fp" style="--v:1"></div></div><span class="norma-v">20.740 N</span></div>
  <p class="norma-diff"><strong>+15%</strong> acima do que a norma pede, sem deformação.</p>
</figure>"""


def clientes():
    lis = "".join(f'<li><img src="/img/clientes/{s}.webp" alt="{n}" width="140" height="95" loading="lazy"></li>' for s, n in CLIENTES)
    return f'<ul class="logos">{lis}</ul>'


def cta_band(title, text, msg, cta_id):
    return f"""<section class="band-cta"><div class="wrap band-cta-in" data-reveal>
  <div><h2 class="h2">{title}</h2><p class="lead">{text}</p></div>
  <div class="band-cta-a"><a class="btn btn-primary" href="/orcamento" data-cta="{cta_id}_orcamento">Pedir orçamento {icon('arrow')}</a>
  <a class="btn btn-ghost" href="{wa(msg)}" target="_blank" rel="noopener" data-cta="{cta_id}_whatsapp">{icon('wa')} Falar no WhatsApp</a></div>
</div></section>"""



FAQ = [
    ("Qual é a altura mínima e máxima do piso elevado?", "O sistema Famaplás vai de 6 cm a 180 cm de altura de piso. A altura define a composição do pedestal: até 150 mm com a base estrela, mais altura com prolongadores e, a partir de 400 mm, com o tubo de acoplamento."),
    ("Quanto peso o pedestal aguenta?", "Cada pedestal resiste a 20.740 N sem deformação, acima dos 18.000 N exigidos pela norma ABNT. O sistema suporta 741 kg de carga concentrada e 1.800 kg/m² de carga distribuída, segundo ensaios do laboratório Falcão Bauer. Os laudos estão disponíveis sob solicitação."),
    ("Pode usar em área externa e deck de piscina?", "Pode. Os pedestais são de polipropileno, que não oxida com água nem com o tempo, e são usados em decks de piscina e áreas externas."),
    ("Quantos pedestais vou precisar?", "Numa grade de placas de 600 × 600 mm, a conta é de cerca de 2,8 pedestais por metro quadrado, mais os das bordas. A calculadora do site faz essa estimativa a partir das medidas do ambiente."),
    ("Vocês vendem peças avulsas?", "Sim. Além do pedestal completo, vendemos apoio da placa, porca niveladora, bases, prolongador, tubo de acoplamento e porca base separadamente, para reposição ou montagem própria."),
    ("A Famaplás faz a instalação?", "Faz. A instalação do piso elevado completo é feita pela equipe da Famaplás, com média de 50 m² por dia por instalador."),
    ("Quais revestimentos posso usar por cima?", "Carpete em placa, laminado, melamínico, vinílico, condutivo e outros, além das placas Famaplás em pedra natural, mármore e granito."),
    ("Dá para mudar o layout depois de instalado?", "Dá. Basta retirar a placa, reposicionar o que estiver embaixo e recolocar. Não precisa de obra."),
]


def faq_block(title="Dúvidas frequentes", sec_cls="sec"):
    items = "".join(f'<details class="faq-i"><summary>{escape(q)}{icon("down")}</summary><div class="faq-a"><p>{escape(a)}</p></div></details>' for q, a in FAQ)
    return f"""<section class="{sec_cls}" id="duvidas"><div class="wrap faq">
  <div class="faq-head" data-reveal><p class="eyebrow">Perguntas frequentes</p><h2 class="h2">{title}</h2>
  <p class="lead">Não achou sua resposta? Fale com a equipe técnica.</p>
  <a class="link-arrow" href="{wa('Olá! Vim pelo site da Famaplás e tenho uma dúvida técnica.')}" target="_blank" rel="noopener" data-cta="faq_whatsapp">Perguntar no WhatsApp {icon('arrow')}</a></div>
  <div class="faq-list" data-reveal>{items}</div>
</div></section>"""


FAQ_LD = {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [
    {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in FAQ]}

# ------------------------------------------------------------------ anatomia (SVG do pedestal)

def anatomia_svg():
    import math

    def persp(n, cx, r, y1, y2, cls, sw=3):
        # nervuras distribuídas em volta de um cilindro, com espaçamento em perspectiva
        out = []
        for i in range(n):
            t = -math.pi / 2 + (i + .5) * math.pi / n
            x = cx + r * math.sin(t)
            op = .35 + .65 * math.cos(t)
            out.append(f'<line x1="{x:.1f}" x2="{x:.1f}" y1="{y1}" y2="{y2}" stroke-width="{sw * (.5 + .5 * math.cos(t)):.2f}" opacity="{op:.2f}"/>')
        return f'<g class="{cls}">' + "".join(out) + "</g>"

    threads = "".join(f'<path d="M146 {y} a54 6 0 0 0 108 0" />' for y in range(116, 200, 8))
    callout = lambda n, y, x0: (f'<g class="co"><line x1="{x0}" x2="384" y1="{y}" y2="{y}"/><circle cx="398" cy="{y}" r="13"/>'
                                f'<text x="398" y="{y + 4}" text-anchor="middle">{n}</text></g>')
    return f"""<svg class="anat-svg" viewBox="0 0 420 560" role="img" aria-labelledby="anat-title">
<title id="anat-title">Pedestal Famaplás montado, de baixo para cima: base, prolongador, porca niveladora, apoio da placa e placa</title>
<defs>
  <linearGradient id="gP" x1="0" x2="1"><stop offset="0" stop-color="#121315"/><stop offset=".28" stop-color="#3d4046"/><stop offset=".42" stop-color="#4a4e55"/><stop offset=".7" stop-color="#25272b"/><stop offset="1" stop-color="#0f1012"/></linearGradient>
  <linearGradient id="gP2" x1="0" x2="1"><stop offset="0" stop-color="#18191c"/><stop offset=".35" stop-color="#34373c"/><stop offset="1" stop-color="#141517"/></linearGradient>
  <linearGradient id="gTop" x1="0" x2="1" y1="0" y2="1"><stop offset="0" stop-color="#4b4f56"/><stop offset="1" stop-color="#2a2c30"/></linearGradient>
  <linearGradient id="gStone" x1="0" x2="1" y1="0" y2="1"><stop offset="0" stop-color="#f1ede6"/><stop offset="1" stop-color="#d6d0c5"/></linearGradient>
  <linearGradient id="gFinL" x1="1" x2="0"><stop offset="0" stop-color="#2c2e33"/><stop offset="1" stop-color="#16171a"/></linearGradient>
  <linearGradient id="gFinR" x1="0" x2="1"><stop offset="0" stop-color="#26282c"/><stop offset="1" stop-color="#0f1012"/></linearGradient>
</defs>

<g class="dim" aria-hidden="true">
  <line x1="18" x2="18" y1="44" y2="484"/><path d="M12 52 L18 42 L24 52 M12 476 L18 486 L24 476"/>
  <text x="0" y="0" transform="translate(32 264) rotate(-90)" text-anchor="middle">ALTURA ACABADA 6 A 180 CM</text>
</g>

<g class="part" data-part="placa">
  <path d="M52 44 H340 V70 H52 Z" fill="url(#gStone)" stroke="#bdb5a8"/>
  <path d="M52 44 L80 26 H368 L340 44 Z" fill="#f7f4ef" stroke="#bdb5a8"/>
  <path d="M340 44 L368 26 V52 L340 70 Z" fill="#c9c1b4" stroke="#bdb5a8"/>
  <path d="M80 26 H368" stroke="#fff" stroke-width="1.5" opacity=".8"/>
  {callout("05", 57, 344)}
</g>

<g class="part" data-part="apoio">
  <rect x="136" y="74" width="10" height="20" rx="1" fill="#2b2d31"/><rect x="254" y="74" width="10" height="20" rx="1" fill="#2b2d31"/>
  <rect x="166" y="70" width="9" height="20" rx="1" fill="#383b40"/><rect x="225" y="70" width="9" height="20" rx="1" fill="#383b40"/>
  <rect x="196" y="68" width="8" height="24" rx="1" fill="#44474d"/>
  <path d="M80 96 a120 15 0 0 0 240 0 v9 a120 15 0 0 1 -240 0z" fill="url(#gP2)"/>
  <ellipse cx="200" cy="96" rx="120" ry="15" fill="url(#gTop)"/>
  <ellipse cx="200" cy="96" rx="118" ry="13.5" fill="none" stroke="#5a5e65" stroke-width="1"/>
  <path d="M146 110 H254 V200 a54 6 0 0 1 -108 0z" fill="url(#gP)"/>
  <g class="thr" fill="none" stroke="#0d0e10" stroke-width="2.4" opacity=".85">{threads}</g>
  <g fill="none" stroke="#6a6e75" stroke-width="1" opacity=".6">{"".join(f'<path d="M146 {y + 2} a54 6 0 0 0 108 0" />' for y in range(116, 200, 8))}</g>
  {callout("04", 140, 258)}
</g>

<g class="part" data-part="porca">
  <path d="M124 206 H276 V240 a76 9 0 0 1 -152 0z" fill="url(#gP)"/>
  {persp(14, 200, 78, 208, 246, "ribs")}
  <ellipse cx="200" cy="206" rx="76" ry="9" fill="#3c3f45"/>
  <ellipse cx="200" cy="206" rx="56" ry="6.5" fill="#101113"/>
  <path d="M117 236 H283 V242 a83 10 0 0 1 -166 0z" fill="#1d1e21"/>
  {callout("03", 224, 280)}
</g>

<g class="part" data-part="prolongador">
  <path d="M144 252 H256 V338 a56 7 0 0 1 -112 0z" fill="url(#gP)"/>
  <path d="M140 300 H260 V306 a60 7 0 0 1 -120 0z" fill="#1b1c1f"/>
  {persp(30, 200, 56, 254, 266, "knurl", 1.6)}
  <ellipse cx="200" cy="252" rx="56" ry="7" fill="#45484e"/>
  <ellipse cx="200" cy="252" rx="44" ry="5" fill="#111214"/>
  {callout("02", 290, 260)}
</g>

<g class="part" data-part="base">
  <path d="M150 346 H250 V392 a50 6 0 0 1 -100 0z" fill="url(#gP)"/>
  {persp(40, 200, 50, 346, 354, "knurl", 1.2)}
  <ellipse cx="200" cy="346" rx="50" ry="6" fill="#45484e"/>
  <ellipse cx="200" cy="346" rx="40" ry="4.5" fill="#111214"/>
  <path d="M232 372 L300 460 H246 Z" fill="#141518" opacity=".9"/>
  <path d="M168 372 L100 460 H154 Z" fill="#1a1b1e" opacity=".9"/>
  <path d="M152 376 L66 470 H152 Z" fill="url(#gFinL)"/>
  <path d="M248 376 L334 470 H248 Z" fill="url(#gFinR)"/>
  <path d="M194 392 H206 L214 474 H186 Z" fill="#3b3e44"/>
  <path d="M152 376 L66 470 M248 376 L334 470" stroke="#55595f" stroke-width="1.2"/>
  <path d="M60 470 H340 V478 a140 6 0 0 1 -280 0z" fill="#121315"/>
  <path d="M60 470 H340" stroke="#4a4d53" stroke-width="1.5"/>
  {callout("01", 420, 316)}
</g>

<g class="ground" aria-hidden="true"><path d="M44 488 H372" stroke="#8b8f95" stroke-width="1.5" stroke-dasharray="5 6"/>
  <path d="M44 494 l10 10 M64 494 l10 10 M84 494 l10 10 M104 494 l10 10 M124 494 l10 10 M144 494 l10 10 M164 494 l10 10 M184 494 l10 10 M204 494 l10 10 M224 494 l10 10 M244 494 l10 10 M264 494 l10 10 M284 494 l10 10 M304 494 l10 10 M324 494 l10 10 M344 494 l10 10" stroke="#3a3d42" stroke-width="1.2"/>
  <text x="46" y="526">CONTRAPISO</text></g>
</svg>"""


ANAT_PARTS = [
    ("base", "base-para-pedestal", "Base", "Apoia no contrapiso. Modelo estrela, com dentes de travamento, ou modelo para tubo."),
    ("prolongador", "prolongador", "Prolongador", "Entra quando o projeto pede mais altura, sem perder estabilidade."),
    ("porca", "porca-niveladora", "Porca niveladora", "Ajuste milimétrico da altura e roscas que travam o conjunto."),
    ("apoio", "apoio-da-placa", "Apoio da placa", "Recebe a placa. Reforço completo e rosca dupla."),
    ("placa", None, "Placa", "Pedra natural laminada, 600 × 600 mm. Sai e volta para o lugar quando o layout muda."),
]

# ------------------------------------------------------------------ páginas

ORG_LD = {
    "@context": "https://schema.org", "@type": "LocalBusiness", "@id": DOMAIN + "/#empresa",
    "name": "Famaplás", "legalName": "Famaplás Indústria e Comércio de Peças Plásticas",
    "description": "Fabricante de pedestais para piso elevado, piso elevado completo e alças plásticas, desde 2003.",
    "url": DOMAIN + "/", "logo": DOMAIN + "/img/favicon.svg", "image": DOMAIN + "/img/fabrica-1.webp",
    "telephone": "+55 11 2601-6881", "email": EMAIL, "foundingDate": "2003",
    "address": {"@type": "PostalAddress", "streetAddress": "Rua Madre de Deus, 683", "addressLocality": "São Paulo",
                "addressRegion": "SP", "addressCountry": "BR", "postalCode": ""},
    "areaServed": "BR", "sameAs": [INSTAGRAM],
}
ORG_LD["address"].pop("postalCode")


def build_home():
    feat = [P[s] for s in ["pedestal-para-piso-elevado", "piso-elevado-completo", "apoio-da-placa", "porca-niveladora", "base-para-pedestal", "prolongador"]]
    parts_list = "".join(
        f'<li class="anat-item" data-step="{k}"><span class="anat-n">0{i+1}</span><div><h3>{"<a href=/produtos/" + s + ">" + t + "</a>" if s else t}</h3><p>{d}</p></div></li>'
        for i, (k, s, t, d) in enumerate(ANAT_PARTS))
    body = f"""
<section class="hero">
  <div class="hero-grid-bg" aria-hidden="true"></div>
  <div class="wrap hero-top">
    <div>
      <p class="eyebrow">Fabricante de pedestais para piso elevado desde 2003</p>
      <h1 class="h1">O que fica embaixo do piso decide se ele dura.</h1>
    </div>
    <div class="hero-side">
      <p class="lead">Pedestais em polipropileno fabricados em São Paulo, 15% mais resistentes do que a norma ABNT exige, sem oxidação e com altura regulável de 6 a 180 cm.</p>
      <div class="hero-a">
        <a class="btn btn-primary" href="/orcamento" data-cta="hero_orcamento">Pedir orçamento {icon('arrow')}</a>
        <a class="btn btn-ghost" href="/calculadora" data-cta="hero_calculadora">Calcular pedestais</a>
      </div>
    </div>
  </div>
  <div class="hero-stage">
    <figure class="hero-visual">
      <img src="/img/piso-escritorio.webp" alt="Escritório com placas de piso elevado levantadas mostrando pedestais e cabeamento passando por baixo" width="1970" height="750" fetchpriority="high">
      <figcaption class="hv-tags">
        <span class="hv-tag" style="--x:53%;--y:57%"><i></i>Pedestal Famaplás</span>
        <span class="hv-tag hv-tag-l" style="--x:41%;--y:83%"><i></i>Cabos e dutos no vão técnico</span>
        <span class="hv-tag" style="--x:80%;--y:66%"><i></i>Placa removível</span>
      </figcaption>
    </figure>
  </div>
  <div class="wrap">{numbers()}</div>
</section>

<section class="anat" id="anatomia" aria-labelledby="anat-h">
  <div class="wrap anat-in">
    <div class="anat-copy">
      <p class="eyebrow">Anatomia do pedestal</p>
      <h2 class="h2" id="anat-h">Monte de baixo para cima. Nivele no milímetro.</h2>
      <p class="lead">Cada pedestal é montado com as peças que o projeto pede. É assim que o mesmo sistema vai de um piso quase rente ao chão até um vão de 1,8 m para cabos e dutos.</p>
      <ol class="anat-list">{parts_list}</ol>
    </div>
    <div class="anat-stage">{anatomia_svg()}</div>
  </div>
</section>

<section class="sec">
  <div class="wrap">
    <div class="sec-head" data-reveal><div><p class="eyebrow">Linha de produtos</p><h2 class="h2">Do pedestal completo à peça avulsa.</h2></div>
    <a class="link-arrow" href="/produtos">Catálogo completo {icon('arrow')}</a></div>
    <div class="pgrid">{''.join(card(p) for p in feat)}</div>
  </div>
</section>

<section class="calc-band"><div class="wrap calc-band-in" data-reveal>
  <div class="calc-band-n" aria-hidden="true"><span class="mono">≈</span>2,8<small>pedestais / m²</small></div>
  <div><p class="eyebrow">Calculadora</p><h2 class="h2">Quantos pedestais o seu ambiente precisa?</h2>
  <p class="lead">Informe as medidas e a altura do piso. A calculadora estima as peças e a composição, e você manda o resultado direto para a equipe.</p></div>
  <a class="btn btn-primary btn-lg" href="/calculadora" data-cta="home_calculadora">Abrir calculadora {icon('arrow')}</a>
</div></section>

<section class="sec sec-paper">
  <div class="wrap split">
    <div data-reveal>{norma_bar()}</div>
    <div class="split-copy" data-reveal>
      <p class="eyebrow">Por que Famaplás</p>
      <h2 class="h2">Polipropileno injetado na nossa fábrica, testado em laboratório.</h2>
      <ul class="ticks">
        <li><strong>Não oxida.</strong> O pedestal mantém a mesma regulagem anos depois, em área interna ou externa.</li>
        <li><strong>Trava sozinho.</strong> Roscas e dentes de travamento impedem que o conjunto gire depois de nivelado.</li>
        <li><strong>Muda de layout sem obra.</strong> Basta retirar a placa e reposicionar.</li>
        <li><strong>Instalação própria.</strong> Equipe Famaplás com média de 50 m² por dia por instalador.</li>
      </ul>
      <a class="link-arrow" href="/produtos/piso-elevado-completo#ficha">Ver a ficha técnica completa {icon('arrow')}</a>
    </div>
  </div>
</section>

<section class="sec">
  <div class="wrap">
    <div class="sec-head" data-reveal><div><p class="eyebrow">Aplicações</p><h2 class="h2">Onde nossos pedestais trabalham.</h2></div>
    <a class="link-arrow" href="/aplicacoes">Ver aplicações {icon('arrow')}</a></div>
    <div class="apps">
      <figure class="apps-img" data-reveal><img src="/img/piso-escritorio.webp" alt="Piso elevado em escritório com cabeamento passando sob as placas" width="1970" height="750" loading="lazy"></figure>
      <ul class="apps-list" data-reveal>
        <li><span class="mono">01</span>Escritórios e edifícios inteligentes</li>
        <li><span class="mono">02</span>CPDs e centros de controle</li>
        <li><span class="mono">03</span>Decks de piscina e áreas externas</li>
        <li><span class="mono">04</span>Palcos e espaços para eventos</li>
        <li><span class="mono">05</span>Lojas, escolas e áreas técnicas hospitalares</li>
      </ul>
    </div>
  </div>
</section>

<section class="sec sec-dark">
  <div class="wrap split split-rev">
    <div class="factory-imgs" data-reveal>
      <img src="/img/fabrica-1.webp" alt="Injetora da fábrica Famaplás produzindo peças" width="724" height="516" loading="lazy">
      <img src="/img/obra-pedestais.webp" alt="Pedestais Famaplás posicionados em obra antes da colocação das placas" width="610" height="390" loading="lazy">
    </div>
    <div class="split-copy" data-reveal>
      <p class="eyebrow">Fábrica própria</p>
      <h2 class="h2">Mais de 20 anos fabricando o que sustenta o piso.</h2>
      <p>Fundada em 2003 na Mooca, em São Paulo, a Famaplás injeta seus próprios pedestais. Controlar a produção da peça é o que permite garantir a resistência, a precisão da rosca e o prazo de entrega.</p>
      <a class="btn btn-ghost-dark" href="/sobre">Conhecer a Famaplás {icon('arrow')}</a>
    </div>
  </div>
</section>

<section class="sec">
  <div class="wrap">
    <div class="sec-head" data-reveal><div><p class="eyebrow">Quem já construiu com a gente</p><h2 class="h2">Construtoras e incorporadoras que confiam na Famaplás.</h2></div></div>
    <div data-reveal>{clientes()}</div>
  </div>
</section>
{faq_block("O que mais perguntam para a gente.", "sec sec-paper")}
{cta_band("Mande a planta. A gente indica o pedestal.", "Informe a área, a altura acabada do piso e o tipo de ambiente. A equipe técnica responde com a composição ideal e o orçamento.", "Olá! Vim pelo site da Famaplás e quero um orçamento de piso elevado.", "home")}
"""
    intro_head = ("<script>(function(){try{if(matchMedia('(prefers-reduced-motion: reduce)').matches||localStorage.getItem('fp-intro'))return;"
                  "var d=document.documentElement;d.classList.add('fp-intro-on');window.FP_INTRO=1;"
                  "setTimeout(function(){d.classList.remove('fp-intro-on')},3500)}catch(e){}})();</script>")
    extra_js = '<script src="/js/gsap.min.js" defer></script><script src="/js/intro.js" defer></script><script src="/js/ScrollTrigger.min.js" defer></script><script src="/js/SplitText.min.js" defer></script><script src="/js/home-intro.js" defer></script><script src="/js/anatomia.js" defer></script>'
    return page("/", "Famaplás | Pedestais para piso elevado e piso elevado completo",
                "Fabricante de pedestais para piso elevado em São Paulo desde 2003. Certificação ABNT, 20.740 N de resistência, altura de 6 a 180 cm. Peça seu orçamento.",
                body, "/", extra_head=intro_head, extra_js=extra_js, jsonld=[ORG_LD, FAQ_LD])


def build_sobre():
    nav, ld = crumbs([("/", "Início"), (None, "Sobre")])
    body = f"""
<section class="phead"><div class="wrap">{nav}
  <p class="eyebrow">Sobre a Famaplás</p>
  <h1 class="h1">Uma fábrica de pedestais, não uma revenda.</h1>
  <p class="lead">Desde 2003 a Famaplás fabrica na Mooca, em São Paulo, os pedestais e componentes para piso elevado que vende e instala.</p>
</div></section>

<section class="sec sec-tight"><div class="wrap split">
  <div class="split-copy" data-reveal>
    <h2 class="h3">Qualidade que começa na injeção da peça</h2>
    <p>Ao longo desses anos a Famaplás se consolidou na fabricação de pedestais com alta tecnologia, seguindo os padrões de qualidade e as normas da ABNT (Associação Brasileira de Normas Técnicas).</p>
    <p>Garantia, qualidade e a experiência dos nossos profissionais são a base do trabalho. Produzimos em polipropileno, com produção personalizada, os componentes para instalação e manutenção de pisos elevados, além de alças plásticas para embalagens.</p>
    <h2 class="h3">Parceria de longo prazo</h2>
    <p>Alianças fiéis e duradouras somam forças. É assim que tratamos clientes e fornecedores: nossas soluções sustentam, literalmente, o crescimento de quem nos escolheu como fornecedor.</p>
  </div>
  <div class="stack-imgs" data-reveal>
    <img src="/img/fabrica-1.webp" alt="Injetora industrial na fábrica Famaplás" width="724" height="516" loading="lazy">
    <img src="/img/fabrica-2.webp" alt="Linha de produção de peças plásticas da Famaplás" width="724" height="516" loading="lazy">
  </div>
</div></section>

<section class="sec sec-paper"><div class="wrap">
  <div class="sec-head" data-reveal><div><p class="eyebrow">Em números</p><h2 class="h2">O que o laboratório mediu.</h2></div></div>
  {numbers()}
  <div class="mt">{norma_bar()}</div>
</div></section>

<section class="sec"><div class="wrap">
  <div class="sec-head" data-reveal><div><p class="eyebrow">O que fazemos</p><h2 class="h2">Três frentes, uma fábrica.</h2></div></div>
  <div class="trio">
    <a class="trio-c" href="/produtos/pedestal-para-piso-elevado" data-reveal><span class="mono">01</span><h3>Pedestais e componentes</h3><p>Pedestal completo e todas as peças avulsas: apoio da placa, porca niveladora, bases, prolongador, tubo de acoplamento e porca base.</p></a>
    <a class="trio-c" href="/produtos/piso-elevado-completo" data-reveal><span class="mono">02</span><h3>Piso elevado completo</h3><p>Placas de pedra natural ou mármore e granito com pedestais, instalados pela nossa equipe.</p></a>
    <a class="trio-c" href="/produtos/alcas-plasticas" data-reveal><span class="mono">03</span><h3>Alças plásticas</h3><p>Alças em polietileno de baixa densidade para caixas e embalagens, em cores sob consulta.</p></a>
  </div>
</div></section>

<section class="sec sec-paper"><div class="wrap">
  <div class="sec-head" data-reveal><div><p class="eyebrow">Clientes</p><h2 class="h2">Alguns de nossos clientes.</h2></div></div>
  <div data-reveal>{clientes()}</div>
</div></section>
{cta_band("Vamos conversar sobre o seu projeto?", "Atendemos construtoras, instaladores e empresas em todo o Brasil.", "Olá! Vim pelo site da Famaplás e gostaria de falar com um atendente.", "sobre")}
"""
    return page("/sobre", "Sobre a Famaplás | Fábrica de pedestais para piso elevado desde 2003",
                "Conheça a Famaplás: fábrica própria de pedestais para piso elevado na Mooca, São Paulo, desde 2003, com certificação ABNT e laudos Falcão Bauer.",
                body, "/sobre", jsonld=[ld])


def build_produtos():
    nav, ld = crumbs([("/", "Início"), (None, "Produtos")])
    groups = [("Pedestal e sistema completo", ["pedestal-para-piso-elevado", "piso-elevado-completo"]),
              ("Componentes avulsos", ["apoio-da-placa", "porca-niveladora", "base-para-pedestal", "prolongador", "tubo-de-acoplamento", "porca-base"]),
              ("Embalagens", ["alcas-plasticas"])]
    secs = "".join(f'<div class="pgroup"><h2 class="h3 pgroup-t" data-reveal>{t}</h2><div class="pgrid">{"".join(card(P[s]) for s in ss)}</div></div>' for t, ss in groups)
    guia = [("Regulagem mínima", "Apoio da placa + porca base", "Pouca fiação sob o piso"),
            ("Até 150 mm de altura acabada", "Apoio da placa + porca niveladora + Base 02 (estrela)", "Montagem padrão"),
            ("Acima de 150 mm", "Montagem padrão + prolongador", "Ganho de altura com travamento"),
            ("A partir de 400 mm", "Apoio da placa + porca niveladora + Base 03 + tubo de acoplamento", "Vãos grandes para dutos e cabos")]
    rows = "".join(f"<tr><th scope=row>{a}</th><td>{b}</td><td>{c}</td></tr>" for a, b, c in guia)
    body = f"""
<section class="phead"><div class="wrap">{nav}
  <p class="eyebrow">Catálogo</p>
  <h1 class="h1">Produtos Famaplás</h1>
  <p class="lead">Pedestais para piso elevado, componentes avulsos e o piso elevado completo, todos fabricados em polipropileno com certificação ABNT. E alças plásticas para embalagens.</p>
</div></section>
<section class="sec sec-tight"><div class="wrap">{secs}</div></section>
<section class="sec sec-paper" id="guia"><div class="wrap">
  <div class="sec-head" data-reveal><div><p class="eyebrow">Guia rápido</p><h2 class="h2">Qual composição para qual altura?</h2></div></div>
  <div class="table-wrap" data-reveal><table class="tbl">
    <thead><tr><th scope="col">Altura do piso</th><th scope="col">Composição</th><th scope="col">Quando usar</th></tr></thead>
    <tbody>{rows}</tbody></table></div>
  <p class="note">Referência geral. Cada projeto é confirmado pela equipe técnica da Famaplás antes do orçamento.</p>
</div></section>
{cta_band("Não sabe quais peças pedir?", "Mande a altura acabada e a área. A gente monta a lista de componentes para você.", "Olá! Vim pelo site da Famaplás e preciso de ajuda para escolher os componentes do pedestal.", "produtos")}
"""
    return page("/produtos", "Produtos | Pedestais, componentes e piso elevado completo | Famaplás",
                "Catálogo Famaplás: pedestal para piso elevado, apoio da placa, porca niveladora, bases, prolongador, tubo de acoplamento, porca base, piso elevado completo e alças plásticas.",
                body, "/produtos", jsonld=[ld])


def build_produto(p):
    nav, ld = crumbs([("/", "Início"), ("/produtos", "Produtos"), (None, p["curto"])])
    imgs = p["img"]
    thumbs = "".join(
        f'<li><button type="button" class="thumb" aria-pressed="{"true" if i == 0 else "false"}" data-src="/img/produtos/{im}.webp" aria-label="Ver foto {i+1} de {len(imgs)}"><img src="/img/produtos/{im}.webp" alt="" width="481" height="478" loading="lazy"></button></li>'
        for i, im in enumerate(imgs)) if len(imgs) > 1 else ""
    texto = "".join(f"<p>{escape(t)}</p>" for t in p["texto"])
    modelos = ""
    if p.get("modelos"):
        modelos = '<div class="modelos">' + "".join(f'<div class="modelo"><h3>{escape(a)}</h3><p>{escape(b)}</p></div>' for a, b in p["modelos"]) + "</div>"
    regra = f'<div class="regra"><span class="eyebrow">Como aplicar</span><p>{escape(p["regra"])}</p></div>' if p.get("regra") else ""
    monta = ""
    if p["monta"]:
        chips = "".join(f'<li><a href="/produtos/{s}">{escape(P[s]["curto"])}</a></li>' for s in p["monta"])
        monta = f'<div class="monta"><span class="eyebrow">{p.get("monta_label", "Combina com")}</span><ul class="chips">{chips}</ul></div>'
    aplic = "".join(f"<li>{icon('check')}{escape(a)}</li>" for a in p["aplic"])
    dest = "".join(f"<li>{escape(d)}</li>" for d in p["destaques"])
    msg = f"Olá! Vim pelo site da Famaplás e quero um orçamento de {p['curto'].lower()}."
    specs = ""
    if p.get("specs"):
        rows = "".join(f"<tr><th scope=row>{escape(a)}</th><td>{escape(b)}</td></tr>" for a, b in SPECS)
        specs = f"""<section class="sec sec-paper" id="ficha"><div class="wrap">
  <div class="sec-head" data-reveal><div><p class="eyebrow">Ficha técnica</p><h2 class="h2">Sistema de piso elevado Famaplás</h2></div></div>
  <div class="split split-top"><div class="table-wrap" data-reveal><table class="tbl tbl-spec"><tbody>{rows}</tbody></table></div>
  <div data-reveal>{norma_bar()}</div></div>
  <p class="note">Dados de carga medidos pelo laboratório Falcão Bauer. Laudos disponíveis sob solicitação.</p>
</div></section>"""
    others = [q for q in PRODUTOS if q["slug"] != p["slug"] and q["grupo"] != "embalagem"]
    if p["grupo"] == "embalagem":
        others = [P["pedestal-para-piso-elevado"], P["piso-elevado-completo"], P["apoio-da-placa"]]
    else:
        pref = [P[s] for s in p["monta"] if s in P][:3]
        others = pref + [q for q in others if q not in pref][: 3 - len(pref)]
    body = f"""
<section class="phead phead-prod"><div class="wrap">{nav}</div></section>
<section class="prod"><div class="wrap prod-in">
  <div class="gallery">
    <figure class="gallery-main"><img id="gal-main" src="/img/produtos/{imgs[0]}.webp" alt="{escape(p['nome'])} Famaplás" width="481" height="478" fetchpriority="high" style="view-transition-name: p-{p['slug']}"></figure>
    {"<ul class='thumbs'>" + thumbs + "</ul>" if thumbs else ""}
  </div>
  <div class="prod-copy">
    <p class="eyebrow">{ {'pedestal':'Sistema','componente':'Componente do pedestal','sistema':'Solução completa','embalagem':'Embalagens'}[p['grupo']] }</p>
    <h1 class="h1 h1-prod">{escape(p['nome'])}</h1>
    <p class="lead">{escape(p['resumo'])}</p>
    <ul class="dest">{dest}</ul>
    <div class="prod-a">
      <a class="btn btn-primary" href="/orcamento?produto={p['slug']}" data-cta="produto_orcamento" data-produto="{p['slug']}">Solicitar orçamento {icon('arrow')}</a>
      <a class="btn btn-ghost" href="{wa(msg)}" target="_blank" rel="noopener" data-cta="produto_whatsapp" data-produto="{p['slug']}">{icon('wa')} WhatsApp</a>
    </div>
  </div>
</div></section>
<section class="sec sec-tight"><div class="wrap prod-detail">
  <div class="prose" data-reveal><h2 class="h3">Sobre o produto</h2>{texto}{modelos}</div>
  <aside class="prod-side" data-reveal>
    <div class="aplic"><span class="eyebrow">Aplicações</span><ul>{aplic}</ul></div>
    {regra}{monta}
  </aside>
</div></section>
{specs}
<section class="sec"><div class="wrap">
  <div class="sec-head" data-reveal><div><p class="eyebrow">Veja também</p><h2 class="h2">Produtos relacionados</h2></div><a class="link-arrow" href="/produtos">Todos os produtos {icon('arrow')}</a></div>
  <div class="pgrid">{''.join(card(q) for q in others)}</div>
</div></section>
"""
    prod_ld = {"@context": "https://schema.org", "@type": "Product", "name": p["nome"], "description": p["resumo"],
               "image": [f"{DOMAIN}/img/produtos/{i}.webp" for i in imgs], "brand": {"@type": "Brand", "name": "Famaplás"},
               "manufacturer": {"@id": DOMAIN + "/#empresa"}, "category": "Piso elevado" if p["grupo"] != "embalagem" else "Embalagens"}
    return page(f"/produtos/{p['slug']}", f"{p['nome']} | Famaplás", p["resumo"] + " Fabricação própria em São Paulo. Peça seu orçamento.",
                body, "/produtos", jsonld=[ld, prod_ld], og_img=f"/img/produtos/{imgs[0]}.webp")


def build_aplicacoes():
    nav, ld = crumbs([("/", "Início"), (None, "Aplicações")])
    apps = [
        ("Escritórios e edifícios inteligentes", "Cabeamento de dados e elétrica passa sob o piso e chega a qualquer ponto. Mudar o layout das estações é tirar a placa e reposicionar.", "pedestal-para-piso-elevado"),
        ("CPDs e centros de controle", "Vãos maiores para dutos de ar-condicionado e bandejas de cabos, com o tubo de acoplamento para alturas a partir de 400 mm.", "tubo-de-acoplamento"),
        ("Decks de piscina e áreas externas", "O polipropileno não oxida com água nem com o tempo. O pedestal mantém o nível do deck e deixa a água escoar por baixo.", "base-para-pedestal"),
        ("Palcos e espaços para eventos", "Altura regulável milímetro a milímetro e montagem rápida para estruturas que precisam ficar firmes.", "porca-niveladora"),
        ("Lojas, escolas e áreas hospitalares", "Acabamento com carpete em placa, vinílico, laminado, condutivo ou pedra, sobre um piso fácil de manter.", "piso-elevado-completo"),
        ("Projetos de vão mínimo", "Com apoio da placa e porca base, o pedestal fica o mais baixo possível, para quando há pouca fiação sob o piso.", "porca-base"),
    ]
    cards = "".join(
        f'<article class="app-c" data-reveal><span class="mono">0{i+1}</span><h2 class="h3">{t}</h2><p>{d}</p><a class="link-arrow" href="/produtos/{s}">{escape(P[s]["curto"])} {icon("arrow")}</a></article>'
        for i, (t, d, s) in enumerate(apps))
    body = f"""
<section class="phead"><div class="wrap">{nav}
  <p class="eyebrow">Aplicações</p>
  <h1 class="h1">Um vão livre sob o piso resolve problemas diferentes.</h1>
  <p class="lead">Cabos, dutos, encanamento, escoamento de água ou só um layout que muda toda hora. Veja onde os pedestais Famaplás são usados.</p>
</div></section>
<section class="sec sec-tight"><div class="wrap">
  <figure class="wide-img" data-reveal><img src="/img/piso-escritorio.webp" alt="Piso elevado em escritório com placas removidas mostrando o cabeamento" width="1970" height="750" loading="lazy"></figure>
  <div class="apps-grid">{cards}</div>
</div></section>
<section class="sec sec-paper"><div class="wrap split">
  <div data-reveal><img class="r-img" src="/img/obra-pedestais.webp" alt="Pedestais distribuídos em obra antes da colocação das placas" width="610" height="390" loading="lazy"></div>
  <div class="split-copy" data-reveal><p class="eyebrow">Acabamentos</p><h2 class="h2">Qualquer revestimento por cima.</h2>
  <p>Sobre o sistema Famaplás cabe carpete em placa, laminado, melamínico, vinílico, condutivo e outros. Ou as placas Famaplás em pedra natural, mármore e granito.</p>
  <a class="link-arrow" href="/produtos/piso-elevado-completo">Piso elevado completo {icon('arrow')}</a></div>
</div></section>
{cta_band("Qual é o seu ambiente?", "Conte o tipo de uso e a altura necessária. A gente indica o pedestal certo.", "Olá! Vim pelo site da Famaplás e quero indicação de pedestal para o meu projeto.", "aplicacoes")}
"""
    return page("/aplicacoes", "Aplicações do piso elevado | Escritórios, CPDs, decks e palcos | Famaplás",
                "Onde usar pedestais para piso elevado: escritórios, CPDs, decks de piscina, áreas externas, palcos, lojas, escolas e áreas hospitalares.",
                body, "/aplicacoes", jsonld=[ld])


def build_orcamento():
    nav, ld = crumbs([("/", "Início"), (None, "Orçamento")])
    opts = "".join(f'<label class="check"><input type="checkbox" name="produtos" value="{p["slug"]}" data-nome="{escape(p["curto"])}"><span>{escape(p["curto"])}</span></label>' for p in PRODUTOS)
    body = f"""
<section class="phead"><div class="wrap">{nav}
  <p class="eyebrow">Orçamento</p>
  <h1 class="h1">Peça seu orçamento em 1 minuto.</h1>
  <p class="lead">Preencha o que souber. A mensagem chega pronta no WhatsApp da equipe comercial, que responde com a composição e o valor.</p>
</div></section>
<section class="sec sec-tight"><div class="wrap orc">
  <form class="form" id="form-orcamento" novalidate>
    <fieldset><legend>Seus dados</legend>
      <div class="f2">
        <label class="field"><span>Nome *</span><input name="nome" autocomplete="name" required></label>
        <label class="field"><span>Empresa</span><input name="empresa" autocomplete="organization"></label>
        <label class="field"><span>WhatsApp *</span><input name="telefone" type="tel" autocomplete="tel" inputmode="tel" required placeholder="(11) 90000-0000"></label>
        <label class="field"><span>Cidade / UF</span><input name="cidade" autocomplete="address-level2"></label>
      </div>
    </fieldset>
    <fieldset><legend>O que você precisa</legend>
      <div class="checks">{opts}</div>
    </fieldset>
    <fieldset><legend>Sobre o projeto</legend>
      <div class="f3">
        <label class="field"><span>Área aproximada (m²)</span><input name="area" inputmode="decimal"></label>
        <label class="field"><span>Altura acabada do piso</span><input name="altura" placeholder="ex.: 15 cm"></label>
        <label class="field"><span>Ambiente</span><select name="ambiente"><option value="">Selecione</option><option>Escritório</option><option>CPD / sala técnica</option><option>Deck / área externa</option><option>Palco / evento</option><option>Loja / escola / hospital</option><option>Embalagens (alças)</option><option>Outro</option></select></label>
      </div>
      <label class="field"><span>Mensagem</span><textarea name="mensagem" rows="4" placeholder="Prazo, quantidade de peças, se precisa de instalação..."></textarea></label>
    </fieldset>
    <p class="form-err" id="form-err" role="alert" hidden></p>
    <button class="btn btn-primary btn-lg" type="submit">{icon('wa')} Enviar pelo WhatsApp</button>
    <p class="note">Ao enviar, abrimos o WhatsApp com a mensagem pronta. Nada é enviado sem você confirmar lá.</p>
  </form>
  <aside class="orc-side">
    <div class="orc-box"><span class="eyebrow">Prefere ligar?</span>
      <p><a class="big-link" href="tel:{PHONE_1[1]}">{PHONE_1[0]}</a><br><a class="big-link" href="tel:{PHONE_2[1]}">{PHONE_2[0]}</a></p>
      <p><a href="mailto:{EMAIL}">{EMAIL}</a></p></div>
    <div class="orc-box"><span class="eyebrow">Para agilizar</span>
      <ul class="ticks ticks-sm"><li>Planta ou croqui com a área</li><li>Altura acabada desejada</li><li>Tipo de revestimento por cima</li><li>Se precisa de instalação</li></ul></div>
  </aside>
</div></section>
"""
    return page("/orcamento", "Orçamento de pedestal e piso elevado | Famaplás",
                "Peça orçamento de pedestais para piso elevado, componentes, piso elevado completo ou alças plásticas. Resposta pelo WhatsApp.",
                body, "/orcamento", jsonld=[ld])


def build_contato():
    nav, ld = crumbs([("/", "Início"), (None, "Contato")])
    maps = "https://www.google.com/maps?q=" + quote("Rua Madre de Deus, 683, Mooca, São Paulo - SP") + "&output=embed"
    body = f"""
<section class="phead"><div class="wrap">{nav}
  <p class="eyebrow">Contato</p>
  <h1 class="h1">Fale com a Famaplás.</h1>
  <p class="lead">Atendimento comercial e técnico de segunda a sexta. Pelo WhatsApp a resposta costuma ser mais rápida.</p>
</div></section>
<section class="sec sec-tight"><div class="wrap contact">
  <ul class="contact-list">
    <li><span class="ci">{icon('wa')}</span><div><span class="eyebrow">WhatsApp</span><a class="big-link" href="{wa('Olá! Vim pelo site da Famaplás e gostaria de falar com um atendente.')}" target="_blank" rel="noopener" data-cta="contato_whatsapp">(11) 98983-3238</a></div></li>
    <li><span class="ci">{icon('phone')}</span><div><span class="eyebrow">Central</span><a class="big-link" href="tel:{PHONE_1[1]}">{PHONE_1[0]}</a><a class="big-link" href="tel:{PHONE_2[1]}">{PHONE_2[0]}</a></div></li>
    <li><span class="ci">{icon('mail')}</span><div><span class="eyebrow">E-mail</span><a class="big-link" href="mailto:{EMAIL}">{EMAIL}</a></div></li>
    <li><span class="ci">{icon('pin')}</span><div><span class="eyebrow">Fábrica e escritório</span><p>Rua Madre de Deus, 683<br>Mooca, São Paulo/SP</p></div></li>
  </ul>
  <div class="map"><iframe title="Mapa: Famaplás na Rua Madre de Deus, 683, Mooca" src="{maps}" loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe></div>
</div></section>
{cta_band("Já sabe o que precisa?", "Use o formulário de orçamento e mande tudo de uma vez.", "Olá! Vim pelo site da Famaplás e gostaria de um orçamento.", "contato")}
"""
    return page("/contato", "Contato | Famaplás Pisos Elevados | Mooca, São Paulo",
                "Telefones, WhatsApp, e-mail e endereço da Famaplás, fábrica de pedestais para piso elevado na Mooca, São Paulo.",
                body, "/contato", jsonld=[ld, ORG_LD])



def build_calculadora():
    nav, ld = crumbs([("/", "Início"), (None, "Calculadora")])
    body = f"""
<section class="phead"><div class="wrap">{nav}
  <p class="eyebrow">Calculadora de pedestais</p>
  <h1 class="h1">Quantos pedestais você precisa?</h1>
  <p class="lead">Uma estimativa rápida para placas de 600 × 600 mm. Informe as medidas e a altura acabada do piso, e mande o resultado para a equipe confirmar.</p>
</div></section>
<section class="sec sec-tight"><div class="wrap calc" id="calc">
  <form class="calc-form form" id="calc-form" novalidate>
    <fieldset><legend>1. Medidas do ambiente</legend>
      <div class="seg" role="radiogroup" aria-label="Como informar as medidas">
        <label><input type="radio" name="modo" value="dim" checked><span>Comprimento × largura</span></label>
        <label><input type="radio" name="modo" value="area"><span>Só a área</span></label>
      </div>
      <div class="f2" data-modo="dim">
        <label class="field"><span>Comprimento (m)</span><input name="comp" inputmode="decimal" value="10"></label>
        <label class="field"><span>Largura (m)</span><input name="larg" inputmode="decimal" value="6"></label>
      </div>
      <div class="f2" data-modo="area" hidden>
        <label class="field"><span>Área (m²)</span><input name="area" inputmode="decimal" value="60"></label>
      </div>
    </fieldset>
    <fieldset><legend>2. Altura acabada do piso</legend>
      <div class="range">
        <input type="range" name="altura" min="6" max="180" step="1" value="15" aria-describedby="alt-out">
        <output id="alt-out" for="altura"><strong>15</strong> cm</output>
      </div>
      <div class="range-scale" aria-hidden="true"><span style="--p:0">6 cm</span><span style="--p:1">180 cm</span></div>
      <label class="check check-inline"><input type="checkbox" name="minimo"><span>Vão mínimo, com pouca fiação sob o piso</span></label>
    </fieldset>
    <fieldset><legend>3. O que você precisa</legend>
      <label class="check check-inline"><input type="checkbox" name="placas"><span>Quero as placas também (piso elevado completo)</span></label>
    </fieldset>
  </form>
  <aside class="calc-out" aria-live="polite">
    <p class="eyebrow">Estimativa</p>
    <div class="calc-big"><strong id="c-ped">0</strong><span>pedestais</span></div>
    <p class="calc-sub" id="c-sub"></p>
    <ul class="calc-list" id="c-list"></ul>
    <p class="calc-err" id="c-err" hidden></p>
    <a class="btn btn-primary btn-lg" id="c-send" href="{wa('Olá! Vim pelo site da Famaplás.')}" target="_blank" rel="noopener" data-cta="calculadora_whatsapp">{icon('wa')} Enviar para a equipe</a>
    <p class="note">Estimativa para uma grade retangular de placas 600 × 600 mm. Pilares, recortes e paredes curvas mudam a conta. A equipe técnica confirma antes do orçamento.</p>
  </aside>
</div></section>
{faq_block()}
"""
    return page("/calculadora", "Calculadora de pedestais para piso elevado | Famaplás",
                "Calcule quantos pedestais para piso elevado o seu ambiente precisa e qual composição usar para a altura do piso. Estimativa gratuita da Famaplás.",
                body, "/calculadora", extra_js='<script src="/js/calculadora.js" defer></script>', jsonld=[ld, FAQ_LD])


def build_404():
    body = f"""<section class="phead phead-404"><div class="wrap">
  <p class="eyebrow mono">Erro 404</p><h1 class="h1">Essa página saiu do nível.</h1>
  <p class="lead">O endereço pode ter mudado com o novo site. Tente pelo catálogo ou fale com a gente.</p>
  <div class="hero-a"><a class="btn btn-primary" href="/produtos">Ver produtos {icon('arrow')}</a><a class="btn btn-ghost" href="/">Página inicial</a></div>
</div></section>"""
    page("/404", "Página não encontrada | Famaplás", "Página não encontrada.", body)


if __name__ == "__main__":
    pages = [build_home(), build_sobre(), build_produtos(), build_aplicacoes(), build_orcamento(), build_contato(), build_calculadora()]
    pages += [build_produto(p) for p in PRODUTOS]
    build_404()
    (OUT / "img" / "favicon.svg").write_text(
        '<svg xmlns="http://www.w3.org/2000/svg" viewBox="-6 -18 78 76"><rect x="-6" y="-18" width="78" height="76" rx="14" fill="#1b1d20"/>'
        + LOGO.replace('<svg class="logo-mark" viewBox="0 0 66 40" aria-hidden="true">', '<g fill="#E0761E">').replace("</svg>", "</g>") + "</svg>", encoding="utf-8")
    if PREVIEW:
        (OUT / "robots.txt").write_text("User-agent: *\nDisallow: /\n", encoding="utf-8")
    else:
        (OUT / "robots.txt").write_text(f"User-agent: *\nAllow: /\n\nSitemap: {DOMAIN}/sitemap.xml\n", encoding="utf-8")
    urls = "".join(f"<url><loc>{DOMAIN}{u if u != '/' else '/'}</loc></url>" for u in pages)
    (OUT / "sitemap.xml").write_text(f'<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">{urls}</urlset>', encoding="utf-8")
    # cleanUrls tira o .html antes dos redirects, então a origem vai sem extensão
    old = [(p["old"][:-5], f"/produtos/{p['slug']}") for p in PRODUTOS] + [("sobre-nos-famaplas", "/sobre")]
    redirects = [{"source": f"/{o}", "destination": d, "permanent": True} for o, d in old]
    vercel = {"$schema": "https://openapi.vercel.sh/vercel.json", "framework": None, "buildCommand": None, "installCommand": None,
              "outputDirectory": "site", "cleanUrls": True, "trailingSlash": False, "redirects": redirects}
    if PREVIEW:
        vercel["headers"] = [{"source": "/(.*)", "headers": [{"key": "X-Robots-Tag", "value": "noindex, nofollow"}]}]
    (OUT.parent / "vercel.json").write_text(json.dumps(vercel, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"{len(pages) + 1} páginas geradas em {OUT}")

# Famaplás - novo site (preview)

Site estático multipágina, gerado por `build.py` em `site/`. Pronto para Vercel (`vercel.json` na raiz desta pasta).

## Rodar e editar

- Editar textos, produtos e ficha técnica: `build.py` (dados no topo). Depois: `python3 build.py`.
- Estilo: `site/css/style.css`. Comportamento: `site/js/main.js`. Animação da anatomia: `site/js/anatomia.js`.
- `PREVIEW = True` em `build.py` põe noindex em tudo e bloqueia o robots.txt. Trocar para `False` só no domínio oficial.

## Páginas (17)

`/`, `/sobre`, `/produtos`, `/produtos/<9 produtos>`, `/aplicacoes`, `/calculadora`, `/orcamento`, `/contato`, `404`.
As URLs antigas (`/pedestal-para-piso-elevado.html` etc.) têm redirect 301 para as novas no `vercel.json`, para não perder SEO.

## Motion (e por quê)

| Onde | O quê | Motivo | Origem |
|---|---|---|---|
| Todas | transição entre páginas; foto do produto "viaja" do card para a página | continuidade: o produto clicado vira a página | web-lab `page-transition` |
| Blocos abaixo da dobra | entrada leve na rolagem | orientação de leitura | web-lab `reveal-on-scroll` |
| Cards de produto | inclinação 4° no hover (só mouse) | feedback de que o card é clicável | web-lab `image-tilt` |
| Home, "Anatomia" (desenho técnico com cotas e chamadas numeradas) | pedestal se monta peça a peça com a rolagem (seção presa no desktop) | explicar como as peças se combinam | GSAP + ScrollTrigger (`site/js/`) |
| Home, entrada | linhas do título sobem de uma máscara, texto e botões entram em sequência, foto do hero assenta (sem sumir) e as etiquetas aparecem | conduzir o olhar na ordem da mensagem, ~1,1 s, sem loop | GSAP + SplitText (`site/js/home-intro.js`) |
| Barra ABNT x Famaplás | barras enchem ao entrar na tela | mostrar a margem de 15% sobre a norma | CSS |

Reduced motion desliga tudo; sem JS o pedestal aparece montado e todo o texto fica visível.

## Pendências com o cliente

1. **Logo em vetor.** O do site atual é um JPG de 153 px. O do preview foi redesenhado em SVG a partir dele: pedir o arquivo original.
2. **Tempo de mercado.** O site atual diz "há 14 anos", o "Sobre" diz "fundada em 2003" e o Instagram diz "+20 anos". Usei "desde 2003" e "mais de 20 anos". Confirmar.
3. **Guia de altura** (página Produtos) foi montado a partir dos textos de cada peça. Validar com a equipe técnica.
4. **Fotos.** As de produto são boas (fundo branco). Faltam fotos de obras prontas em alta resolução para Aplicações e Sobre.
5. **Clientes.** Logos copiados do site atual. Confirmar se ainda podem ser exibidos.
6. **Rastreamento.** O `dataLayer` já recebe `cta_click`, `whatsapp_click`, `form_start` e `generate_lead`. Falta o GTM/GA4 (skill `rastreamento-e-indexacao`).
7. **Formulário de orçamento** envia para o WhatsApp (11) 98983-3238, sem backend. Se quiserem receber por e-mail ou planilha também, é um passo a mais.
8. **Calculadora** (`site/js/calculadora.js`): pedestais = (colunas + 1) × (linhas + 1) numa grade de 600 × 600 mm; só com a área, 1 por placa + 15% de borda. Composição por faixa de altura (até 15 cm, 15 a 40 cm com prolongador, 40 cm ou mais com tubo). Validar a conta e as faixas com a equipe técnica.
9. **Perguntas frequentes**: respostas montadas só com dados do site atual. Confirmar a resposta sobre venda de peças avulsas para reposição.
10. **Norma ABNT pelo número e CNPJ no rodapé**: o site atual não informa nenhum dos dois. Pedir ao cliente.
11. **Widget de WhatsApp** (`site/js/wa-widget.js`): todos os botões de WhatsApp abrem a pré-qualificação (nome, WhatsApp, empresa, interesse, perfil, tamanho da área ou quantidade de alças, prazo) e mandam a mensagem pronta para (11) 98983-3238. Nas páginas de produto o interesse já vem preenchido. Dispara `wa_widget_open` e `generate_lead` (com nome e telefone, no mesmo padrão dos outros sites) no dataLayer. Validar as perguntas com o comercial.
12. Newsletter do site antigo foi retirada (não havia destino configurado aparente).

## Fontes

Extração do site atual em `_extracao/` (HTML de todas as páginas e ficha técnica). Imagens originais em `assets-orig/`.

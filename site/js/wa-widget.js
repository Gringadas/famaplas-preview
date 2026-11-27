/* Widget de pré-qualificação do WhatsApp.
   Base: widget do Site Manuela (portado para JS puro na Escola Clara Luz), adaptado para B2B.
   Intercepta os links de WhatsApp do site (data-cta terminando em "whatsapp" e o botão flutuante).
   Sem JS os links continuam abrindo o WhatsApp direto. */
(function () {
  'use strict';
  var WHATS = '5511989833238';
  var INTERESSE = ['Pedestal para piso elevado', 'Piso elevado completo (placas + pedestais)', 'Peças avulsas para reposição', 'Alças plásticas', 'Ainda não sei, quero ajuda técnica'];
  var PERFIL = ['Construtora ou incorporadora', 'Instalador ou revenda', 'Arquiteto ou engenheiro', 'Empresa, para uso próprio', 'Pessoa física'];
  var AREA = ['Até 50 m²', 'De 50 a 200 m²', 'De 200 a 1.000 m²', 'Acima de 1.000 m²', 'Ainda não sei'];
  var QTD = ['Até 1.000 unidades', 'De 1.000 a 10.000 unidades', 'Acima de 10.000 unidades', 'Ainda não sei'];
  var PRAZO = ['Obra já em andamento', 'Nos próximos 30 dias', 'Em 1 a 3 meses', 'Ainda estou orçando'];
  var POR_PRODUTO = {
    'pedestal-para-piso-elevado': INTERESSE[0], 'piso-elevado-completo': INTERESSE[1], 'alcas-plasticas': INTERESSE[3],
    'apoio-da-placa': INTERESSE[2], 'porca-niveladora': INTERESSE[2], 'base-para-pedestal': INTERESSE[2],
    'prolongador': INTERESSE[2], 'tubo-de-acoplamento': INTERESSE[2], 'porca-base': INTERESSE[2]
  };
  var GLYPH = '<svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M12 2a10 10 0 0 0-8.6 15.1L2 22l5-1.3A10 10 0 1 0 12 2Zm0 18.2a8.2 8.2 0 0 1-4.2-1.2l-.3-.2-3 .8.8-2.9-.2-.3A8.2 8.2 0 1 1 12 20.2Zm4.5-6.1c-.2-.1-1.5-.7-1.7-.8-.2-.1-.4-.1-.6.1l-.8 1c-.1.2-.3.2-.5.1a6.7 6.7 0 0 1-3.3-2.9c-.2-.4.2-.4.7-1.3.1-.2 0-.3 0-.4l-.8-1.8c-.2-.5-.4-.4-.6-.4h-.5a1 1 0 0 0-.7.3 3 3 0 0 0-.9 2.2 5.2 5.2 0 0 0 1.1 2.7 11.8 11.8 0 0 0 4.5 4c1.7.7 2.3.8 3.2.6a2.7 2.7 0 0 0 1.8-1.2c.2-.6.2-1.1.2-1.2-.1-.1-.3-.2-.6-.3Z"/></svg>';
  var CLOSE = '<svg viewBox="0 0 24 24" fill="none" aria-hidden="true"><path d="M6 6l12 12M18 6L6 18" stroke="currentColor" stroke-width="2" stroke-linecap="round"/></svg>';

  var root = null, lastFocus = null, st = null;

  function esc(t) { return String(t).replace(/[&<>"]/g, function (c) { return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c]; }); }
  function fmtPhone(raw) {
    var d = raw.replace(/\D/g, '').slice(0, 11), n = d.length;
    if (n <= 2) return d;
    if (n <= 6) return '(' + d.slice(0, 2) + ') ' + d.slice(2);
    if (n <= 10) return '(' + d.slice(0, 2) + ') ' + d.slice(2, 6) + '-' + d.slice(6);
    return '(' + d.slice(0, 2) + ') ' + d.slice(2, 7) + '-' + d.slice(7);
  }
  function track(name, data) { window.dataLayer = window.dataLayer || []; data.event = name; window.dataLayer.push(data); }
  function isAlca() { return st.interesse === INTERESSE[3]; }

  var STEP = {
    id: { t: 'Como podemos te chamar?', hint: 'Assim a equipe comercial já te atende pelo nome.' },
    interesse: { t: 'O que você procura?', opts: function () { return INTERESSE; } },
    perfil: { t: 'Você é…', opts: function () { return PERFIL; } },
    tamanho: { t: function () { return isAlca() ? 'Qual a quantidade aproximada?' : 'Qual o tamanho da área?'; }, opts: function () { return isAlca() ? QTD : AREA; } },
    prazo: { t: 'Para quando é o projeto?', opts: function () { return PRAZO; } }
  };

  function valid() {
    var k = st.steps[st.i];
    if (k === 'id') return st.nome.trim().length > 1 && st.tel.replace(/\D/g, '').length >= 10;
    return !!st[k];
  }

  function waUrl() {
    var tamLabel = isAlca() ? 'Quantidade' : 'Área';
    var msg = ['Olá, Famaplás! Vim pelo site e gostaria de um orçamento.', '',
      '*Nome:* ' + st.nome.trim() + (st.empresa.trim() ? ' (' + st.empresa.trim() + ')' : ''),
      '*Telefone:* ' + st.tel,
      '*Interesse:* ' + st.interesse + (st.produto ? ' - ' + st.produtoNome : ''),
      '*Perfil:* ' + st.perfil,
      '*' + tamLabel + ':* ' + st.tamanho,
      '*Prazo:* ' + st.prazo].join('\n');
    return 'https://wa.me/' + WHATS + '?text=' + encodeURIComponent(msg);
  }

  function render(focus) {
    var k = st.steps[st.i], n = st.steps.length, body = '', bars = '';
    for (var b = 0; b < n; b++) bars += '<i class="' + (b <= st.i ? 'on' : '') + '"></i>';
    var def = STEP[k];
    var title = typeof def.t === 'function' ? def.t() : def.t;
    if (k === 'id') {
      body = '<h3 tabindex="-1">' + title + '</h3><p class="hint">' + def.hint + '</p>' +
        '<label class="wa-field"><span>Seu nome*</span><input id="wa-nome" autocomplete="name" autocapitalize="words" enterkeyhint="next" placeholder="Nome e sobrenome"></label>' +
        '<label class="wa-field"><span>Seu WhatsApp*</span><input id="wa-tel" type="tel" inputmode="tel" autocomplete="tel" enterkeyhint="next" placeholder="(11) 99999-9999"></label>' +
        '<label class="wa-field"><span>Empresa</span><input id="wa-emp" autocomplete="organization" enterkeyhint="next" placeholder="Opcional"></label>';
    } else {
      body = '<h3 tabindex="-1">' + title + '</h3><div class="wa-opts">' + def.opts().map(function (o) {
        return '<button type="button" class="wa-opt" data-v="' + esc(o) + '" aria-pressed="' + (st[k] === o) + '">' + esc(o) + '</button>';
      }).join('') + '</div>';
    }
    var last = st.i === n - 1;
    var foot = (st.i > 0 ? '<button type="button" class="wa-back">Voltar</button>' : '') +
      (last ? '<a class="wa-go" target="_blank" rel="noopener" href="#">' + GLYPH + 'Abrir no WhatsApp</a>' : '<button type="button" class="wa-next">Continuar</button>');
    var sub = st.produto ? st.produtoNome + ' · ' : '';
    root.querySelector('.wa-panel').innerHTML =
      '<div class="wa-head"><div><b>Orçamento pelo WhatsApp</b><span>' + esc(sub) + 'Passo ' + (st.i + 1) + ' de ' + n + '</span></div><button type="button" class="wa-x" aria-label="Fechar">' + CLOSE + '</button></div>' +
      '<div class="wa-bars">' + bars + '</div><div class="wa-body">' + body + '</div><div class="wa-foot">' + foot + '</div>';
    if (k === 'id') {
      var ni = root.querySelector('#wa-nome'), ti = root.querySelector('#wa-tel'), ei = root.querySelector('#wa-emp');
      ni.value = st.nome; ti.value = st.tel; ei.value = st.empresa;
      ni.addEventListener('input', function () { st.nome = ni.value; sync(); });
      ti.addEventListener('input', function () { ti.value = st.tel = fmtPhone(ti.value); sync(); });
      ei.addEventListener('input', function () { st.empresa = ei.value; });
      if (focus !== false) ni.focus();
    } else if (focus !== false) {
      root.querySelector('h3').focus();
    }
    sync();
  }

  function sync() {
    var ok = valid(), nx = root.querySelector('.wa-next'), go = root.querySelector('.wa-go');
    if (nx) nx.disabled = !ok;
    if (go) { go.setAttribute('aria-disabled', ok ? 'false' : 'true'); go.setAttribute('href', ok ? waUrl() : '#'); }
  }

  function open(source, produto, produtoNome) {
    if (root) return;
    lastFocus = document.activeElement;
    var pre = produto && POR_PRODUTO[produto];
    st = { source: source, nome: '', tel: '', empresa: '', interesse: pre || '', perfil: '', tamanho: '', prazo: '', produto: produto || '', produtoNome: produtoNome || '', i: 0 };
    st.steps = pre ? ['id', 'perfil', 'tamanho', 'prazo'] : ['id', 'interesse', 'perfil', 'tamanho', 'prazo'];
    root = document.createElement('div');
    root.className = 'wa-overlay';
    root.setAttribute('role', 'dialog');
    root.setAttribute('aria-modal', 'true');
    root.setAttribute('aria-label', 'Pedir orçamento à Famaplás pelo WhatsApp');
    root.innerHTML = '<div class="wa-panel"></div>';
    document.body.appendChild(root);
    document.documentElement.classList.add('wa-open');
    track('wa_widget_open', { lead_source: source, produto: produto || undefined });

    root.addEventListener('click', function (e) {
      if (e.target === root || e.target.closest('.wa-x')) return close();
      var opt = e.target.closest('.wa-opt');
      if (opt) {
        st[st.steps[st.i]] = opt.getAttribute('data-v');
        [].forEach.call(root.querySelectorAll('.wa-opt'), function (b) { b.setAttribute('aria-pressed', String(b === opt)); });
        sync();
        // escolha única: avança sozinho, sem precisar clicar em Continuar
        if (st.i < st.steps.length - 1) setTimeout(function () { if (root) { st.i++; render(); } }, 180);
        return;
      }
      if (e.target.closest('.wa-back')) { st.i--; return render(); }
      if (e.target.closest('.wa-next')) { if (valid()) { st.i++; render(); } return; }
      var go = e.target.closest('.wa-go');
      if (go) {
        if (!valid()) return e.preventDefault();
        track('generate_lead', {
          form_name: 'whatsapp_widget', lead_source: st.source, lead_nome: st.nome.trim(), lead_empresa: st.empresa.trim() || undefined,
          lead_telefone: st.tel, lead_telefone_e164: '+55' + st.tel.replace(/\D/g, ''), lead_interesse: st.interesse,
          lead_perfil: st.perfil, lead_tamanho: st.tamanho, lead_prazo: st.prazo, produto: st.produto || undefined, destination_phone: WHATS
        });
        setTimeout(close, 60);
      }
    });
    root.addEventListener('keydown', function (e) {
      if (e.key === 'Escape') return close();
      if (e.key === 'Enter' && e.target.tagName === 'INPUT' && st.steps[st.i] === 'id' && valid()) { e.preventDefault(); st.i++; return render(); }
      if (e.key !== 'Tab') return;
      var f = root.querySelectorAll('button:not(:disabled), a[href], input');
      if (!f.length) return;
      var first = f[0], lastEl = f[f.length - 1];
      if (e.shiftKey && document.activeElement === first) { e.preventDefault(); lastEl.focus(); }
      else if (!e.shiftKey && document.activeElement === lastEl) { e.preventDefault(); first.focus(); }
    });
    render();
  }

  function close() {
    if (!root) return;
    root.remove();
    root = null;
    document.documentElement.classList.remove('wa-open');
    if (lastFocus && lastFocus.focus) lastFocus.focus();
  }

  document.addEventListener('click', function (e) {
    var a = e.target.closest('a.wa-float, a[data-cta$="whatsapp"]');
    if (!a || a.id === 'c-send') return;
    if (e.metaKey || e.ctrlKey || e.shiftKey) return; // abrir em nova aba continua indo direto
    e.preventDefault();
    var produto = a.dataset.produto || '';
    var nome = '';
    if (produto) { var h1 = document.querySelector('.h1-prod'); nome = h1 ? h1.textContent.trim() : ''; }
    open(a.dataset.cta || 'whatsapp_float', produto, nome);
  });

  // botão flutuante aparece depois de rolar um pouco (no topo já existem os CTAs do hero)
  var fl = document.querySelector('.wa-float');
  if (fl) {
    fl.classList.add('wa-js');
    var onScroll = function () { fl.classList.toggle('show', window.scrollY > 320); };
    onScroll();
    window.addEventListener('scroll', onScroll, { passive: true });
  }
})();

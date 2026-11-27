/* Famaplás - comportamento geral (sem dependências) */
(function () {
  'use strict';
  var WA = '5511989833238';
  var root = document.documentElement;

  /* ---------- menu mobile */
  var btn = document.querySelector('.menu-btn');
  var nav = document.getElementById('nav');
  function setNavTop() {
    var h = document.querySelector('.site-header');
    if (h) root.style.setProperty('--nav-top', Math.max(0, h.getBoundingClientRect().bottom) + 'px');
  }
  function closeMenu() {
    if (!btn) return;
    btn.setAttribute('aria-expanded', 'false');
    nav.classList.remove('open');
    root.classList.remove('menu-open');
  }
  if (btn && nav) {
    btn.addEventListener('click', function () {
      var open = btn.getAttribute('aria-expanded') !== 'true';
      setNavTop();
      btn.setAttribute('aria-expanded', String(open));
      nav.classList.toggle('open', open);
      root.classList.toggle('menu-open', open);
    });
    document.addEventListener('keydown', function (e) {
      if (e.key === 'Escape' && nav.classList.contains('open')) { closeMenu(); btn.focus(); }
    });
    window.matchMedia('(min-width: 1001px)').addEventListener('change', closeMenu);
  }

  /* ---------- submenu de produtos */
  document.querySelectorAll('.sub-toggle').forEach(function (t) {
    var li = t.closest('.has-sub');
    t.addEventListener('click', function () {
      var open = t.getAttribute('aria-expanded') !== 'true';
      t.setAttribute('aria-expanded', String(open));
      li.classList.toggle('open', open);
    });
    document.addEventListener('click', function (e) {
      if (!li.contains(e.target) && li.classList.contains('open')) {
        li.classList.remove('open');
        t.setAttribute('aria-expanded', 'false');
      }
    });
  });

  /* ---------- galeria de produto */
  var main = document.getElementById('gal-main');
  if (main) {
    var thumbs = document.querySelectorAll('.thumb');
    thumbs.forEach(function (th) {
      th.addEventListener('click', function () {
        var swap = function () {
          main.src = th.dataset.src;
          thumbs.forEach(function (o) { o.setAttribute('aria-pressed', String(o === th)); });
        };
        // web-lab page-transition: troca com crossfade quando suportado
        if (window.pageTransition) window.pageTransition(swap); else swap();
      });
    });
  }

  /* ---------- eventos de clique em CTA (dataLayer, para o GTM) */
  document.addEventListener('click', function (e) {
    var a = e.target.closest('[data-cta]');
    if (!a) return;
    var isWa = /wa\.me|whatsapp/.test(a.getAttribute('href') || '');
    window.dataLayer.push({
      event: isWa ? 'whatsapp_click' : 'cta_click',
      cta_id: a.dataset.cta,
      produto: a.dataset.produto || undefined,
      page_path: location.pathname
    });
  });

  /* ---------- formulário de orçamento -> WhatsApp */
  var form = document.getElementById('form-orcamento');
  if (form) {
    var params = new URLSearchParams(location.search);
    var pre = params.get('produto');
    if (pre) {
      var box = form.querySelector('input[name="produtos"][value="' + CSS.escape(pre) + '"]');
      if (box) box.checked = true;
    }
    var err = document.getElementById('form-err');
    var started = false;
    form.addEventListener('input', function () {
      if (started) return;
      started = true;
      window.dataLayer.push({ event: 'form_start', form_id: 'orcamento' });
    });
    form.addEventListener('submit', function (e) {
      e.preventDefault();
      var f = form.elements;
      var missing = [];
      ['nome', 'telefone'].forEach(function (n) {
        var ok = f[n].value.trim().length > 1;
        f[n].setAttribute('aria-invalid', String(!ok));
        if (!ok) missing.push(f[n]);
      });
      if (missing.length) {
        err.hidden = false;
        err.textContent = 'Preencha seu nome e WhatsApp para enviarmos o orçamento.';
        missing[0].focus();
        return;
      }
      err.hidden = true;
      var prods = Array.prototype.map.call(form.querySelectorAll('input[name="produtos"]:checked'), function (c) { return c.dataset.nome; });
      var lines = ['Olá! Vim pelo site da Famaplás e quero um orçamento.', ''];
      function add(label, v) { if (v && v.trim()) lines.push('*' + label + ':* ' + v.trim()); }
      add('Nome', f.nome.value);
      add('Empresa', f.empresa.value);
      add('WhatsApp', f.telefone.value);
      add('Cidade/UF', f.cidade.value);
      add('Produtos', prods.join(', '));
      add('Área', f.area.value && f.area.value + ' m²');
      add('Altura acabada', f.altura.value);
      add('Ambiente', f.ambiente.value);
      add('Mensagem', f.mensagem.value);
      window.dataLayer.push({ event: 'generate_lead', form_id: 'orcamento', produtos: prods.join('|'), ambiente: f.ambiente.value || undefined });
      window.location.href = 'https://wa.me/' + WA + '?text=' + encodeURIComponent(lines.join('\n'));
    });
  }
})();

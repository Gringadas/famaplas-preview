/* Abertura da home: o piso elevado se monta (contrapiso -> pedestais -> placas -> logo) e a tela sobe.
   Motivo: apresentar o produto antes da página, em ~2,6 s, só na primeira visita (localStorage).
   Só roda se o script inline do <head> ligou window.FP_INTRO (sem reduced motion, primeira visita).
   Pular: botão, clique, Esc/Enter/Espaço. Sem GSAP ou com erro: some na hora (e o <head> tem trava de 3,5 s). */
(function () {
  'use strict';
  var html = document.documentElement;
  function done() {
    html.classList.remove('fp-intro-on');
    window.dispatchEvent(new Event('fp:reveal'));
  }
  if (!window.FP_INTRO) return;
  try { localStorage.setItem('fp-intro', '1'); } catch (e) {}
  if (!window.gsap) { done(); return; }

  var NS = 'http://www.w3.org/2000/svg';
  var N = 4;              // placas por lado
  var S = 62;             // lado da placa (px no viewBox)
  var A = S * 0.866, B = S * 0.5;
  var H = 34;             // altura do pedestal
  var T = 7;              // espessura da placa
  var W = 2 * N * A + 40, VH = 2 * N * B + H + T + 60;
  var CX = W / 2, CY = H + 30;

  function pt(i, j, lift) { return [CX + (i - j) * A, CY + (i + j) * B - (lift || 0)]; }
  function el(tag, attrs, parent) {
    var e = document.createElementNS(NS, tag);
    for (var k in attrs) e.setAttribute(k, attrs[k]);
    if (parent) parent.appendChild(e);
    return e;
  }
  function poly(points) { return points.map(function (p) { return p[0].toFixed(1) + ',' + p[1].toFixed(1); }).join(' '); }

  // ---------- monta o DOM
  var box = document.createElement('div');
  box.className = 'fp-intro';
  box.setAttribute('role', 'presentation');
  box.innerHTML = '<div class="fp-intro-stage"></div>' +
    '<div class="fp-intro-brand"><svg viewBox="0 0 66 40" aria-hidden="true"><path d="M0 0h29v8H8v7h17v8H8v17H0z"/><path fill-rule="evenodd" d="M33 0h24a9 9 0 0 1 9 9v13a9 9 0 0 1-9 9H41v9h-8zm8 8v15h15a2 2 0 0 0 2-2V10a2 2 0 0 0-2-2z"/></svg>' +
    '<span class="fp-intro-name">FamaPlás</span><span class="fp-intro-tag">Pisos elevados</span></div>' +
    '<p class="fp-intro-cap" aria-hidden="true"><span>Contrapiso</span><span>Pedestais</span><span>Placas</span></p>' +
    '<button type="button" class="fp-intro-skip">Pular abertura</button>';
  var svg = el('svg', { viewBox: '0 0 ' + W.toFixed(0) + ' ' + VH.toFixed(0), 'aria-hidden': 'true', class: 'fp-intro-svg' });
  box.querySelector('.fp-intro-stage').appendChild(svg);

  // contrapiso (grade no chão)
  var ground = el('g', { class: 'fpi-ground' }, svg);
  for (var g = 0; g <= N; g++) {
    var a1 = pt(g, 0), a2 = pt(g, N), b1 = pt(0, g), b2 = pt(N, g);
    el('line', { x1: a1[0], y1: a1[1], x2: a2[0], y2: a2[1] }, ground);
    el('line', { x1: b1[0], y1: b1[1], x2: b2[0], y2: b2[1] }, ground);
  }

  // pedestais, de trás para a frente
  var peds = [];
  var pedLayer = el('g', {}, svg);
  var cells = [];
  for (var i = 0; i <= N; i++) for (var j = 0; j <= N; j++) cells.push([i, j]);
  cells.sort(function (p, q) { return (p[0] + p[1]) - (q[0] + q[1]); });
  cells.forEach(function (c) {
    var p = pt(c[0], c[1]);
    var gp = el('g', { class: 'fpi-ped' }, pedLayer);
    el('ellipse', { cx: p[0], cy: p[1], rx: 11, ry: 5.5, class: 'fpi-foot' }, gp);
    el('rect', { x: p[0] - 5, y: p[1] - H, width: 10, height: H, class: 'fpi-body' }, gp);
    el('ellipse', { cx: p[0], cy: p[1] - H, rx: 10, ry: 5, class: 'fpi-cap' }, gp);
    gp.dataset.d = c[0] + c[1];
    peds.push(gp);
  });

  // placas, de trás para a frente
  var plates = [];
  var plateLayer = el('g', {}, svg);
  var pcells = [];
  for (i = 0; i < N; i++) for (j = 0; j < N; j++) pcells.push([i, j]);
  pcells.sort(function (p, q) { return (p[0] + p[1]) - (q[0] + q[1]) || p[0] - q[0]; });
  pcells.forEach(function (c, idx) {
    var i0 = c[0], j0 = c[1], gap = 1.2;
    var t0 = pt(i0, j0, H), t1 = pt(i0 + 1, j0, H), t2 = pt(i0 + 1, j0 + 1, H), t3 = pt(i0, j0 + 1, H);
    // pequena folga entre placas
    t0 = [t0[0], t0[1] + gap]; t2 = [t2[0], t2[1] - gap]; t1 = [t1[0] - gap, t1[1]]; t3 = [t3[0] + gap, t3[1]];
    var gpl = el('g', { class: 'fpi-plate' + (idx === pcells.length - 1 ? ' fpi-last' : '') }, plateLayer);
    el('polygon', { points: poly([t3, t2, [t2[0], t2[1] + T], [t3[0], t3[1] + T]]), class: 'fpi-side-l' }, gpl);
    el('polygon', { points: poly([t2, t1, [t1[0], t1[1] + T], [t2[0], t2[1] + T]]), class: 'fpi-side-r' }, gpl);
    el('polygon', { points: poly([t0, t1, t2, t3]), class: 'fpi-top' }, gpl);
    plates.push(gpl);
  });

  document.body.appendChild(box);
  html.classList.add('fp-intro-lock');
  html.classList.remove('fp-intro-on'); // o overlay real assumiu, o pseudo-elemento sai

  // ---------- anima
  var caps = box.querySelectorAll('.fp-intro-cap span');
  var tl = gsap.timeline({ defaults: { ease: 'power2.out' }, onComplete: finish });
  tl.from(ground.children, { opacity: 0, duration: 0.35, stagger: 0.015 }, 0)
    .fromTo(caps[0], { opacity: 0, y: 6 }, { opacity: 1, y: 0, duration: 0.25 }, 0.05)
    .from(peds, {
      scaleY: 0, opacity: 0, transformOrigin: '50% 100%', duration: 0.32, ease: 'back.out(2.2)',
      stagger: function (k, t) { return Number(t.dataset.d) * 0.06 + (k % 3) * 0.008; }
    }, 0.3)
    .to(caps[0], { opacity: 0.35, duration: 0.2 }, 0.45)
    .fromTo(caps[1], { opacity: 0, y: 6 }, { opacity: 1, y: 0, duration: 0.25 }, 0.45)
    .from(plates, { y: -90, opacity: 0, duration: 0.38, ease: 'power2.in', stagger: 0.055 }, 0.95)
    .to(caps[1], { opacity: 0.35, duration: 0.2 }, 1.05)
    .fromTo(caps[2], { opacity: 0, y: 6 }, { opacity: 1, y: 0, duration: 0.25 }, 1.05)
    // assentamento: o piso inteiro "senta" 2 px quando a última placa encaixa
    .to(plateLayer, { y: 2, duration: 0.08, ease: 'power1.in' }, '>-0.02')
    .to(plateLayer, { y: 0, duration: 0.25, ease: 'power2.out' })
    .to(box.querySelector('.fpi-last .fpi-top'), { attr: { class: 'fpi-top fpi-top-on' }, duration: 0.01 }, '<')
    .from(box.querySelector('.fp-intro-brand'), { opacity: 0, y: 14, duration: 0.45 }, '<')
    .to(box.querySelector('.fp-intro-cap'), { opacity: 0, duration: 0.3 }, '<')
    .to({}, { duration: 0.35 })
    .add(reveal);

  var revealed = false;
  function reveal() {
    if (revealed) return;
    revealed = true;
    html.classList.remove('fp-intro-lock');
    window.dispatchEvent(new Event('fp:reveal'));
    gsap.to(box, { yPercent: -100, duration: 0.7, ease: 'power3.inOut', onComplete: finish });
  }
  function finish() {
    if (!revealed) { reveal(); return; }
    if (box.parentNode) box.parentNode.removeChild(box);
    document.removeEventListener('keydown', onKey);
  }
  function skip() { tl.kill(); reveal(); }
  function onKey(e) { if (e.key === 'Escape' || e.key === 'Enter' || e.key === ' ') { e.preventDefault(); skip(); } }
  box.addEventListener('click', skip);
  document.addEventListener('keydown', onKey);
  box.querySelector('.fp-intro-skip').focus({ preventScroll: true });
})();

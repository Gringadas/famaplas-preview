/* Calculadora de pedestais (estimativa).
   Grade de placas 600 x 600 mm: pedestais = (colunas + 1) x (linhas + 1), placas = colunas x linhas.
   Só com a área: 1 pedestal por placa + 15% para as bordas.
   Composição por altura, conforme os textos de produto:
   - vão mínimo: apoio + porca base
   - até 15 cm: apoio + porca niveladora + base 02 (estrela)
   - 15 a 40 cm: + prolongador (quantidade depende da altura)
   - a partir de 40 cm: apoio + porca niveladora + base 03 (para tubo) + tubo de acoplamento */
(function () {
  'use strict';
  var form = document.getElementById('calc-form');
  if (!form) return;
  var WA = '5511989833238';
  var PLACA = 0.6;
  var $ = function (id) { return document.getElementById(id); };
  var out = { ped: $('c-ped'), sub: $('c-sub'), list: $('c-list'), err: $('c-err'), send: $('c-send') };
  var altOut = form.querySelector('output strong');
  var used = false;
  var fmt = new Intl.NumberFormat('pt-BR');

  function num(v) {
    var n = parseFloat(String(v || '').replace(/\./g, '').replace(',', '.'));
    return isFinite(n) && n > 0 ? n : 0;
  }

  function compute() {
    var f = form.elements;
    var modo = f.modo.value;
    form.querySelectorAll('[data-modo]').forEach(function (el) { el.hidden = el.dataset.modo !== modo; });
    var h = parseInt(f.altura.value, 10);
    altOut.textContent = h;
    var ped = 0, placas = 0, desc = '';

    if (modo === 'dim') {
      var c = num(f.comp.value), l = num(f.larg.value);
      if (!c || !l) return fail('Informe comprimento e largura em metros.');
      var nc = Math.ceil(c / PLACA), nl = Math.ceil(l / PLACA);
      ped = (nc + 1) * (nl + 1);
      placas = nc * nl;
      desc = fmt.format(c) + ' × ' + fmt.format(l) + ' m (' + fmt.format(Math.round(c * l * 10) / 10) + ' m²), grade de ' + nc + ' × ' + nl + ' placas';
    } else {
      var a = num(f.area.value);
      if (!a) return fail('Informe a área em metros quadrados.');
      placas = Math.ceil(a / (PLACA * PLACA));
      ped = Math.ceil(placas * 1.15);
      desc = fmt.format(a) + ' m², cerca de ' + fmt.format(placas) + ' placas';
    }
    out.err.hidden = true;

    var minimo = f.minimo.checked;
    var rows;
    if (minimo) {
      rows = [['Apoio da placa', ped], ['Porca base', ped]];
    } else if (h < 40) {
      rows = [['Apoio da placa', ped], ['Porca niveladora', ped], ['Base 02 (estrela)', ped]];
      if (h > 15) rows.push(['Prolongador', null]);
    } else {
      rows = [['Apoio da placa', ped], ['Porca niveladora', ped], ['Base 03 (para tubo)', ped], ['Tubo de acoplamento', ped]];
    }
    if (f.placas.checked) rows.push(['Placas 600 × 600 mm', placas]);

    out.ped.textContent = fmt.format(ped);
    out.sub.textContent = desc + ', piso a ' + h + ' cm.';
    out.list.innerHTML = rows.map(function (r) {
      var q = r[1] === null ? 'conforme a altura' : fmt.format(r[1]);
      return '<li><span>' + r[0] + '</span><strong>' + q + '</strong></li>';
    }).join('');

    var msg = ['Olá! Vim pelo site da Famaplás e fiz uma estimativa na calculadora.', '',
      '*Ambiente:* ' + desc, '*Altura acabada:* ' + h + ' cm' + (minimo ? ' (vão mínimo)' : ''),
      '*Pedestais estimados:* ' + fmt.format(ped)];
    rows.forEach(function (r) { msg.push('- ' + r[0] + ': ' + (r[1] === null ? 'conforme a altura' : fmt.format(r[1]))); });
    msg.push('', 'Podem confirmar a composição e me passar um orçamento?');
    out.send.href = 'https://wa.me/' + WA + '?text=' + encodeURIComponent(msg.join('\n'));
    out.send.dataset.pedestais = ped;
    out.send.removeAttribute('aria-disabled');
  }

  function fail(text) {
    out.err.textContent = text;
    out.err.hidden = false;
    out.ped.textContent = '0';
    out.list.innerHTML = '';
    out.sub.textContent = '';
    out.send.setAttribute('aria-disabled', 'true');
  }

  form.addEventListener('input', function () {
    compute();
    if (!used) {
      used = true;
      window.dataLayer.push({ event: 'calculator_use', page_path: location.pathname });
    }
  });
  form.addEventListener('submit', function (e) { e.preventDefault(); });
  out.send.addEventListener('click', function (e) {
    if (out.send.getAttribute('aria-disabled') === 'true') { e.preventDefault(); return; }
    window.dataLayer.push({ event: 'generate_lead', form_id: 'calculadora', pedestais: Number(out.send.dataset.pedestais) || undefined });
  });
  compute();
})();

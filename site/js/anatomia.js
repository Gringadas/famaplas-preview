/* Anatomia do pedestal (home).
   Motivo do movimento: mostrar como as peças se empilham para formar o pedestal,
   na ordem real de montagem (base -> prolongador -> porca -> apoio -> placa).
   Sem JS ou com reduced motion: o pedestal aparece montado e a lista fica toda visível. */
(function () {
  'use strict';
  if (!window.gsap || !window.ScrollTrigger) return;
  gsap.registerPlugin(ScrollTrigger);

  var section = document.querySelector('.anat');
  if (!section) return;
  var order = ['base', 'prolongador', 'porca', 'apoio', 'placa'];
  var parts = order.map(function (k) { return section.querySelector('.part[data-part="' + k + '"]'); });
  var items = order.map(function (k) { return section.querySelector('.anat-item[data-step="' + k + '"]'); });
  if (parts.some(function (p) { return !p; })) return;

  function mark(active) {
    parts.forEach(function (p, i) { p.classList.toggle('on', i === active); });
    items.forEach(function (it, i) { if (it) it.classList.toggle('on', i <= active); });
  }

  function build(opts) {
    var tl = gsap.timeline({
      defaults: { ease: 'power2.out', duration: 1 },
      scrollTrigger: Object.assign({
        trigger: opts.pin ? section : section.querySelector('.anat-stage'),
        scrub: 0.6,
        invalidateOnRefresh: true,
        onUpdate: function (self) {
          var step = Math.min(order.length - 1, Math.floor(self.progress * order.length * 0.999));
          mark(self.progress >= 0.995 ? -1 : step);
          if (self.progress >= 0.995) items.forEach(function (it) { if (it) it.classList.add('on'); });
        },
        onLeaveBack: function () { mark(0); }
      }, opts.st)
    });
    parts.forEach(function (p, i) {
      tl.from(p, { y: -140 - i * 12, opacity: 0 }, i);
    });
    return tl;
  }

  var mm = gsap.matchMedia();

  mm.add('(min-width: 1001px) and (prefers-reduced-motion: no-preference)', function () {
    section.classList.add('is-scrub');
    mark(0);
    build({ pin: true, st: { start: 'top 77px', end: '+=1400', pin: true, anticipatePin: 1 } });
    return function () { section.classList.remove('is-scrub'); mark(-1); };
  });

  mm.add('(max-width: 1000px) and (prefers-reduced-motion: no-preference)', function () {
    build({ pin: false, st: { start: 'top 85%', end: 'bottom 55%' } });
    return function () { mark(-1); };
  });

  // Imagens e fontes mudam a altura da página: recalcula o pin depois que tudo carregou.
  window.addEventListener('load', function () { ScrollTrigger.refresh(); });
  if (document.fonts && document.fonts.ready) document.fonts.ready.then(function () { ScrollTrigger.refresh(); });
})();

/* Entrada da home.
   Motivo: conduzir o olhar na ordem da mensagem (título -> prova -> imagem do vão técnico com as etiquetas).
   Regras: só transform/opacity; nada fica escondido por CSS (o estado inicial é aplicado aqui, pelo GSAP);
   a imagem do hero (LCP) nunca sai de opacity 0, só assenta de uma escala levemente maior;
   duração total ~1,1 s, sem loop. Reduced motion: nada anima. */
(function () {
  'use strict';
  if (!window.gsap) return;
  var hero = document.querySelector('.hero');
  if (!hero) return;
  if (window.SplitText) gsap.registerPlugin(SplitText);

  var mm = gsap.matchMedia();
  mm.add('(prefers-reduced-motion: no-preference)', function () {
    var h1 = hero.querySelector('.h1');
    var eyebrow = hero.querySelector('.eyebrow');
    var side = hero.querySelectorAll('.hero-side .lead, .hero-side .btn');
    var img = hero.querySelector('.hero-visual img');
    var tags = hero.querySelectorAll('.hv-tag');
    var dots = hero.querySelectorAll('.hv-tag i');
    var nums = hero.querySelectorAll('.numbers li');
    var split = null;

    var tl = gsap.timeline({ defaults: { ease: 'power3.out' } });

    // título: linhas sobem de dentro de uma máscara (o texto não muda de opacidade)
    if (window.SplitText && h1) {
      split = SplitText.create(h1, { type: 'lines', mask: 'lines', linesClass: 'h1-line' });
      tl.from(split.lines, { yPercent: 105, duration: 0.6, stagger: 0.07 }, 0);
    }
    if (eyebrow) tl.from(eyebrow, { opacity: 0, x: -12, duration: 0.45 }, 0);
    if (side.length) tl.from(side, { opacity: 0, y: 14, duration: 0.5, stagger: 0.06 }, 0.2);
    // imagem do hero: já visível, só assenta (sem opacity)
    if (img) tl.from(img, { scale: 1.06, duration: 1.1, ease: 'power2.out' }, 0);
    if (tags.length) tl.from(tags, { opacity: 0, y: 8, duration: 0.4, stagger: 0.12 }, 0.55);
    if (dots.length) tl.fromTo(dots, { scale: 0 }, { scale: 1, duration: 0.35, ease: 'back.out(3)', stagger: 0.12 }, 0.55);
    if (nums.length) tl.from(nums, { opacity: 0, y: 10, duration: 0.45, stagger: 0.06 }, 0.45);

    return function () { if (split) split.revert(); };
  });
})();

(function () {
  'use strict';

  var reduce = window.matchMedia('(prefers-reduced-motion: reduce)');
  var native = !!(window.CSS && CSS.supports &&
    CSS.supports('animation-timeline: view()') && CSS.supports('animation-range: entry'));
  var CLASSES = ['reveal-pending', 'reveal-native', 'reveal-in'];
  var observer = null;
  var seen = new WeakSet();

  // <html data-reveal-mode="once"> força o modo de uma vez só (IntersectionObserver).
  function useNative() {
    return native && document.documentElement.dataset.revealMode !== 'once';
  }

  function onEntries(entries) {
    entries.forEach(function (entry) {
      var el = entry.target;
      if (!seen.has(el)) {
        // Primeira leitura: o que já está na tela ou acima dela nunca é escondido.
        seen.add(el);
        var below = !entry.isIntersecting && entry.boundingClientRect.top > 0;
        if (!below) {
          observer.unobserve(el);
        } else if (useNative()) {
          el.classList.add('reveal-native');
          observer.unobserve(el);
        } else {
          el.classList.add('reveal-pending');
        }
      } else if (entry.isIntersecting || entry.boundingClientRect.top <= 0) {
        // Pulou por cima (âncora, End): também revela.
        el.classList.add('reveal-in');
        el.classList.remove('reveal-pending');
        observer.unobserve(el);
      }
    });
  }

  function observe(root) {
    if (!('IntersectionObserver' in window) || reduce.matches) return;
    observer = observer || new IntersectionObserver(onEntries);
    (root || document).querySelectorAll('[data-reveal]').forEach(function (el) {
      if (!seen.has(el)) observer.observe(el);
    });
  }

  function reset() {
    if (observer) observer.disconnect();
    observer = null;
    seen = new WeakSet();
    document.querySelectorAll('[data-reveal]').forEach(function (el) {
      el.classList.remove.apply(el.classList, CLASSES);
    });
  }

  reduce.addEventListener('change', function () {
    reset();
    observe();
  });

  window.RevealOnScroll = { observe: observe, reset: reset };
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', function () { observe(); });
  } else {
    observe();
  }
})();

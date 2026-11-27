(function () {
  'use strict';

  var allowed = window.matchMedia(
    '(hover: hover) and (pointer: fine) and (prefers-reduced-motion: no-preference)'
  );
  var active = null;
  var frame = 0;
  var x = 0;
  var y = 0;

  function apply() {
    frame = 0;
    if (!active) return;
    var r = active.getBoundingClientRect();
    if (!r.width || !r.height) return;
    var max = parseFloat(active.dataset.tilt) || 6; // graus
    var px = Math.min(Math.max((x - r.left) / r.width, 0), 1) - 0.5;
    var py = Math.min(Math.max((y - r.top) / r.height, 0), 1) - 0.5;
    active.style.setProperty('--tilt-x', (-py * 2 * max).toFixed(2) + 'deg');
    active.style.setProperty('--tilt-y', (px * 2 * max).toFixed(2) + 'deg');
  }

  function release() {
    if (frame) cancelAnimationFrame(frame);
    frame = 0;
    if (!active) return;
    active.removeAttribute('data-tilt-active');
    active.style.removeProperty('--tilt-x');
    active.style.removeProperty('--tilt-y');
    active = null;
  }

  document.addEventListener('pointermove', function (event) {
    if (!allowed.matches || event.pointerType !== 'mouse' || !(event.target instanceof Element)) return release();
    var host = event.target.closest('[data-tilt]');
    if (host !== active) {
      release();
      active = host;
      if (host) host.setAttribute('data-tilt-active', '');
    }
    if (!active) return;
    x = event.clientX;
    y = event.clientY;
    if (!frame) frame = requestAnimationFrame(apply);
  }, { passive: true });

  document.addEventListener('pointerout', function (event) {
    if (!event.relatedTarget) release(); // saiu da janela
  }, { passive: true });

  window.addEventListener('scroll', release, { passive: true });
  window.addEventListener('blur', release);
  allowed.addEventListener('change', release);
})();

// Opcional. Carregue sem defer no <head>: pagereveal dispara antes do primeiro frame.
// Não intercepta links nem histórico. A navegação continua sendo a do navegador.
(function () {
  'use strict';

  var reduce = window.matchMedia('(prefers-reduced-motion: reduce)');
  function noop() {}

  // Entre páginas: só informa a direção ao CSS.
  window.addEventListener('pagereveal', function (event) {
    var transition = event.viewTransition;
    if (!transition) return;
    transition.ready.catch(noop);
    transition.finished.catch(noop);
    if (reduce.matches) {
      transition.skipTransition();
      return;
    }
    if (!transition.types) return;
    var activation = window.navigation && window.navigation.activation;
    var back = activation && activation.from && activation.entry &&
      activation.navigationType === 'traverse' &&
      activation.entry.index < activation.from.index;
    transition.types.add(back ? 'back' : 'forward');
  });

  // Na mesma página: pageTransition(function () { ...muda o DOM... })
  // A mudança sempre acontece, com ou sem animação.
  window.pageTransition = function (update) {
    if (!document.startViewTransition || reduce.matches) {
      return new Promise(function (resolve) { resolve(update()); });
    }
    var transition = document.startViewTransition(update);
    transition.ready.catch(noop); // transição pulada não é erro
    transition.finished.catch(noop);
    return transition.updateCallbackDone;
  };
})();

(function () {
  var each = function (list, fn) { Array.prototype.forEach.call(list, fn); };
  var headers = document.querySelectorAll('.hdr');

  /* header: solid once the hero starts scrolling away */
  function onScroll() {
    var stuck = window.scrollY > 12;
    each(headers, function (h) { h.classList.toggle('is-stuck', stuck); });
  }
  onScroll();
  window.addEventListener('scroll', onScroll, { passive: true });

  /* mobile menu */
  each(document.querySelectorAll('.menu-btn'), function (mb) {
    var hdr = mb.closest('.hdr');
    if (!hdr) return;
    mb.addEventListener('click', function () {
      var open = hdr.classList.toggle('is-open');
      mb.setAttribute('aria-expanded', open ? 'true' : 'false');
    });
    each(hdr.querySelectorAll('.nav a'), function (a) {
      a.addEventListener('click', function () {
        hdr.classList.remove('is-open');
        mb.setAttribute('aria-expanded', 'false');
      });
    });
  });

  /* seal: give every ring its own circumference so it can ink itself in */
  each(document.querySelectorAll('.seal .ring'), function (c) {
    var r = parseFloat(c.getAttribute('r')) || 0;
    c.style.setProperty('--len', (2 * Math.PI * r).toFixed(1));
  });

  /* scroll reveal */
  var els = document.querySelectorAll('.reveal');
  if (!('IntersectionObserver' in window)) {
    each(els, function (e) { e.classList.add('in'); });
    return;
  }
  var io = new IntersectionObserver(function (entries) {
    entries.forEach(function (en) {
      if (en.isIntersecting) {
        en.target.classList.add('in');
        io.unobserve(en.target);
      }
    });
  }, { rootMargin: '0px 0px -8% 0px', threshold: 0.08 });
  each(els, function (e) { io.observe(e); });
})();

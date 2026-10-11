/* OwlMind — language switcher (RU / EN). Inline data attributes, no build step. */
(function () {
  var KEY = 'owlmind-lang';

  function stored() {
    try {
      var v = localStorage.getItem(KEY);
      if (v === 'en' || v === 'ru') return v;
    } catch (e) {}
    return null;
  }

  function initLang() {
    var s = stored();
    if (s) return s;
    try {
      if ((navigator.language || '').toLowerCase().indexOf('en') === 0) return 'en';
    } catch (e) {}
    return 'ru';
  }

  function text(el, lang) {
    var en = el.getAttribute('data-en');
    var ru = el.getAttribute('data-ru');
    el.textContent = (lang === 'ru' && ru) ? ru : en;
  }

  function apply(lang) {
    document.documentElement.setAttribute('lang', lang);

    var i, el;

    // Text content
    var nodes = document.querySelectorAll('[data-en]');
    for (i = 0; i < nodes.length; i++) text(nodes[i], lang);

    // Input / textarea placeholders
    var ph = document.querySelectorAll('[data-en-ph]');
    for (i = 0; i < ph.length; i++) {
      el = ph[i];
      var enPh = el.getAttribute('data-en-ph');
      var ruPh = el.getAttribute('data-ru-ph');
      el.setAttribute('placeholder', (lang === 'ru' && ruPh) ? ruPh : enPh);
    }

    // Document title
    var t = document.querySelector('title[data-en]');
    if (t) document.title = (lang === 'ru' && t.getAttribute('data-ru')) ? t.getAttribute('data-ru') : t.getAttribute('data-en');

    // Meta description
    var md = document.querySelector('meta[name="description"][data-en]');
    if (md) md.setAttribute('content', (lang === 'ru' && md.getAttribute('data-ru')) ? md.getAttribute('data-ru') : md.getAttribute('data-en'));

    // Toggle buttons state
    var btns = document.querySelectorAll('[data-lang-toggle]');
    for (i = 0; i < btns.length; i++) {
      var b = btns[i];
      if (b.getAttribute('data-lang') === lang) { b.classList.add('active'); b.setAttribute('aria-pressed', 'true'); }
      else { b.classList.remove('active'); b.setAttribute('aria-pressed', 'false'); }
    }

    try { localStorage.setItem(KEY, lang); } catch (e) {}
  }

  function ready(fn) {
    if (document.readyState !== 'loading') fn();
    else document.addEventListener('DOMContentLoaded', fn);
  }

  ready(function () {
    var lang = initLang();
    apply(lang);
    var btns = document.querySelectorAll('[data-lang-toggle]');
    for (var i = 0; i < btns.length; i++) {
      (function (b) {
        b.addEventListener('click', function () { apply(b.getAttribute('data-lang')); });
      })(btns[i]);
    }
  });
})();

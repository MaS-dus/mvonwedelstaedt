// Cookie-Consent + Google-Tags (GA4, Google Ads Conversion-Tracking).
// Unser eigenes Reichweiten-Tracking (tracking.js) ist cookielos und
// braucht keine Einwilligung (Art. 6 Abs. 1 lit. f DSGVO). GA4 und
// Google Ads setzen dagegen einwilligungspflichtige Cookies -- die
// laden deshalb NUR nach ausdrücklicher Zustimmung über dieses Banner.
//
// IDs eintragen, sobald vorhanden (sonst bleibt das Banner unsichtbar,
// es gibt ja noch nichts zuzustimmen):
window.GA4_ID = '';           // z.B. 'G-XXXXXXXXXX'
window.ADS_CONVERSION_ID = ''; // z.B. 'AW-XXXXXXXXX'
window.ADS_CONVERSION_LABEL = ''; // z.B. 'AbCdEfGhIjK'

(function () {
  if (!window.GA4_ID && !window.ADS_CONVERSION_ID) return; // noch nichts zu konfigurieren

  var STORAGE_KEY = 'cookie-consent-mvw';
  var vorhanden = null;
  try { vorhanden = localStorage.getItem(STORAGE_KEY); } catch (e) {}

  function ladeGoogleTags() {
    var s = document.createElement('script');
    s.async = true;
    s.src = 'https://www.googletagmanager.com/gtag/js?id=' + (window.GA4_ID || window.ADS_CONVERSION_ID);
    document.head.appendChild(s);
    window.dataLayer = window.dataLayer || [];
    function gtag() { window.dataLayer.push(arguments); }
    window.gtag = gtag;
    gtag('js', new Date());
    if (window.GA4_ID) gtag('config', window.GA4_ID);
    if (window.ADS_CONVERSION_ID) gtag('config', window.ADS_CONVERSION_ID);
    window.gtagReportConversion = function () {
      if (window.ADS_CONVERSION_ID && window.ADS_CONVERSION_LABEL) {
        gtag('event', 'conversion', { send_to: window.ADS_CONVERSION_ID + '/' + window.ADS_CONVERSION_LABEL });
      }
    };
  }

  if (vorhanden === 'akzeptiert') { ladeGoogleTags(); return; }
  if (vorhanden === 'abgelehnt') return;

  function banner() {
    var sprache = (new URLSearchParams(location.search).get('lang') === 'en') ? 'en' : 'de';
    var TXT = {
      de: {
        text: 'Diese Seite nutzt optional Google Analytics, um zu verstehen, wie Besucher:innen die Seite finden. Du kannst zustimmen oder ablehnen — die Seite funktioniert in beiden Fällen gleich.',
        accept: 'Zustimmen', decline: 'Ablehnen', privacy: 'Datenschutz',
      },
      en: {
        text: 'This site optionally uses Google Analytics to understand how visitors find the site. You can accept or decline — the site works the same either way.',
        accept: 'Accept', decline: 'Decline', privacy: 'Privacy',
      },
    }[sprache];

    var wrap = document.createElement('div');
    wrap.setAttribute('role', 'dialog');
    wrap.setAttribute('aria-label', 'Cookie-Einwilligung');
    wrap.style.cssText = 'position:fixed;left:0;right:0;bottom:0;z-index:9999;' +
      'background:var(--surface,#fff);border-top:1px solid var(--rule,rgba(0,0,0,.12));' +
      'box-shadow:0 -12px 30px -18px rgba(0,0,0,.35);padding:16px 20px;' +
      'font-family:"Source Serif 4",Georgia,serif;color:var(--ink,#22333B);';
    wrap.innerHTML =
      '<div style="max-width:900px;margin:0 auto;display:flex;flex-wrap:wrap;gap:14px;align-items:center;justify-content:space-between;">' +
      '<p style="margin:0;flex:1 1 380px;font-size:0.9rem;line-height:1.55;color:var(--ink-soft,#5B6B72);">' +
        TXT.text + ' <a href="/datenschutz" style="color:var(--gold,#A97C3F);">' + TXT.privacy + '</a>' +
      '</p>' +
      '<div style="display:flex;gap:10px;flex:0 0 auto;">' +
        '<button id="consent-decline" style="padding:10px 16px;border-radius:9px;border:1.5px solid var(--rule,rgba(0,0,0,.16));background:transparent;color:var(--ink,#22333B);font-family:inherit;font-size:0.875rem;cursor:pointer;">' + TXT.decline + '</button>' +
        '<button id="consent-accept" style="padding:10px 16px;border-radius:9px;border:none;background:var(--ink,#22333B);color:var(--bg,#FAF6EE);font-family:inherit;font-weight:700;font-size:0.875rem;cursor:pointer;">' + TXT.accept + '</button>' +
      '</div></div>';
    document.body.appendChild(wrap);

    document.getElementById('consent-accept').addEventListener('click', function () {
      try { localStorage.setItem(STORAGE_KEY, 'akzeptiert'); } catch (e) {}
      wrap.remove();
      ladeGoogleTags();
    });
    document.getElementById('consent-decline').addEventListener('click', function () {
      try { localStorage.setItem(STORAGE_KEY, 'abgelehnt'); } catch (e) {}
      wrap.remove();
    });
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', banner);
  } else {
    banner();
  }
})();

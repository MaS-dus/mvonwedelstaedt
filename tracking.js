// Server-Side Event Tracking (cookieless, kein Fingerprint, n8n Loop 24)
// Gleiches System wie operator.builders, ueber das Feld "site" getrennt
// ausgewertet. Erfasst: Ereignistyp, Seitenpfad, Referrer-Domaene,
// Zeitstempel, nicht umkehrbarer Hash des User-Agent-Strings. Keine
// Cookies, keine IP-Speicherung, kein Geraete-Fingerprint.
(function () {
  var TRACK_URL = 'https://n8n.srv1082810.hstgr.cloud/webhook/track-event';
  var SITE = 'mvonwedelstaedt.com';
  if (location.hostname === 'localhost' || location.hostname === '127.0.0.1') return;

  function uaHash() {
    var ua = navigator.userAgent, h = 0;
    for (var i = 0; i < ua.length; i++) h = ((h << 5) - h) + ua.charCodeAt(i) | 0;
    return Math.abs(h).toString(36);
  }
  function qp(name) {
    try { return new URLSearchParams(location.search).get(name) || ''; } catch (e) { return ''; }
  }
  function send(event, extra) {
    try {
      var payload = Object.assign({
        event: event,
        site: SITE,
        path: location.pathname,
        ref: document.referrer || 'direct',
        utm_source: qp('utm_source'),
        utm_medium: qp('utm_medium'),
        utm_campaign: qp('utm_campaign'),
        ua_hash: uaHash(),
        ts: Date.now()
      }, extra || {});
      fetch(TRACK_URL, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(payload),
        keepalive: true,
        mode: 'cors'
      });
    } catch (e) {}
  }
  window.osTrack = send;
  send('page_view');
  document.addEventListener('click', function (e) {
    var el = e.target.closest && e.target.closest('[data-track]');
    if (el) send('cta_click', { cta_id: el.dataset.track });
    var a = e.target.closest && e.target.closest('a[href^="http"]');
    if (a && a.href.indexOf('mvonwedelstaedt.com') === -1) {
      try {
        var u = new URL(a.href);
        send('external_link_click', { dest_domain: u.hostname });
      } catch (e) {}
    }
  });
  var depth75 = false;
  window.addEventListener('scroll', function () {
    if (depth75) return;
    var sc = (window.scrollY + window.innerHeight) / document.body.scrollHeight;
    if (sc >= 0.75) { depth75 = true; send('scroll_depth', { depth: 75 }); }
  }, { passive: true });
})();

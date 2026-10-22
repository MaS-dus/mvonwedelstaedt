// Gemeinsames Skript fuer alle indexierbaren Seiten. Alles hier ist Zusatz:
// ohne JavaScript funktionieren Links, Texte und Bilder trotzdem.
(function () {
  var sprache = document.documentElement.lang === "en" ? "en" : "de";

  // Amazon-Shop des Besuchers. Die ASIN ist in allen Shops gleich (auf amazon.co.uk geprueft).
  // Deutsche Buecher: immer amazon.de (liefert auch nach AT und CH). Englische: nach Browser-Region,
  // sonst nach Zeitzone, Standard amazon.com. Alles passiert im Browser, es wird nichts uebertragen.
  function amazonShop() {
    if (sprache === "de") return "de";
    var nachRegion = { GB: "co.uk", IE: "ie", AU: "com.au", CA: "ca", US: "com" };
    var region = (((navigator.languages && navigator.languages[0]) || navigator.language || "").split("-")[1] || "").toUpperCase();
    if (nachRegion[region]) return nachRegion[region];
    var zone = "";
    try { zone = Intl.DateTimeFormat().resolvedOptions().timeZone || ""; } catch (e) { /* egal */ }
    if (zone === "Europe/London") return "co.uk";
    if (zone === "Europe/Dublin") return "ie";
    if (zone.indexOf("Australia/") === 0) return "com.au";
    if (/^America\/(Toronto|Vancouver|Edmonton|Winnipeg|Halifax|St_Johns|Regina|Montreal|Moncton)/.test(zone)) return "ca";
    return "com";
  }
  window.mvwAmazonShop = amazonShop;

  // Englische Seiten liefern amazon.com aus; hier wird der Link auf den Shop des Besuchers umgestellt.
  if (sprache === "en") {
    var shop = amazonShop();
    if (shop !== "com") {
      var links = document.querySelectorAll("a[data-asin]");
      for (var i = 0; i < links.length; i++) {
        links[i].href = "https://www.amazon." + shop + "/dp/" + links[i].getAttribute("data-asin");
      }
    }
  }

  // Weihnachts-Video: nur abspielen, wenn sichtbar und keine reduzierte Bewegung gewuenscht ist;
  // Bedienelemente bleiben immer da.
  var video = document.getElementById("xmas-video");
  if (video && "IntersectionObserver" in window && !window.matchMedia("(prefers-reduced-motion: reduce)").matches) {
    new IntersectionObserver(function (eintraege) {
      for (var j = 0; j < eintraege.length; j++) {
        if (eintraege[j].isIntersecting) { var p = video.play(); if (p && p.catch) p.catch(function () {}); }
        else video.pause();
      }
    }, { threshold: 0.25 }).observe(video);
  }
})();

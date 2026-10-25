# -*- coding: utf-8 -*-
"""Erzeugt alle indexierbaren Seiten der Kinderbuch-Website als statisches HTML.

Aufruf (im Webordner oder von ueberall):
    python tools/build_seo.py

Erzeugt/ueberschreibt:
    index.html, en/index.html                      Startseiten DE und EN
    <slug>/index.html, en/<slug>/index.html         Themenseiten, Pakete, FAQ
    sitemap.xml                                     mit hreflang-Paaren und lastmod

Datenquellen:
    tools/data/buecher.json   alle Buchtitel, ASINs, Etsy-IDs (DE und EN)
    tools/data/pakete.json    die sechs Etsy-Pakete
    tools/content.py          alle Texte, Seitenstruktur, Slugs

Bilder, CSS und JS (covers/, pakete/, site.css, site.js, home.js) werden nur verlinkt.
Pro URL entsteht ein Ordner mit index.html, damit die Seiten lokal und unter Vercel
(cleanUrls) gleich funktionieren.
"""
import html
import json
import re
import struct
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from content import (SITE, SLUGS, PAGE_ORDER, UI, NAV_LABEL, TOPIC_BLURB, HOME, PAGES)  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent
DATA = Path(__file__).resolve().parent / "data"
TODAY = "2026-10-22"
LANGS = ("de", "en")

BUECHER = json.loads((DATA / "buecher.json").read_text(encoding="utf-8"))
PAKETE = json.loads((DATA / "pakete.json").read_text(encoding="utf-8"))
BUCH_NACH_ID = {b["id"]: b for b in BUECHER}
PAKET_NACH_ID = {p["id"]: p for p in PAKETE}

AUTHOR = "M. von Wedelstaedt"
CONTACT_MAIL = "hello@mvonwedelstaedt.com"


# ---------------------------------------------------------------------------
# Hilfsfunktionen
# ---------------------------------------------------------------------------
def esc(s):
    return html.escape(s, quote=True)


_size_cache = {}


def img_size(rel):
    """Breite und Hoehe einer JPEG/PNG-Datei unter ROOT (ohne Zusatzbibliothek)."""
    if rel in _size_cache:
        return _size_cache[rel]
    data = (ROOT / rel.lstrip("/")).read_bytes()
    if data[:8] == b"\x89PNG\r\n\x1a\n":
        w, h = struct.unpack(">II", data[16:24])
    else:
        i = 2
        w = h = None
        while i < len(data):
            if data[i] != 0xFF:
                i += 1
                continue
            marker = data[i + 1]
            if marker in (0xD8, 0x01) or 0xD0 <= marker <= 0xD7:
                i += 2
                continue
            seg = struct.unpack(">H", data[i + 2:i + 4])[0]
            if 0xC0 <= marker <= 0xCF and marker not in (0xC4, 0xC8, 0xCC):
                h, w = struct.unpack(">HH", data[i + 5:i + 9])
                break
            i += 2 + seg
        if w is None:
            raise ValueError("Bildgroesse nicht lesbar: " + rel)
    _size_cache[rel] = (w, h)
    return w, h


def img_attrs(rel):
    w, h = img_size(rel)
    return f'width="{w}" height="{h}"'


def path_of(key, lang):
    slug = SLUGS[key][lang]
    if key == "home":
        return "/" if lang == "de" else "/en/"
    return "/" + slug


def abs_url(key, lang):
    return SITE + path_of(key, lang)


def out_file(key, lang):
    if key == "home":
        return ROOT / "index.html" if lang == "de" else ROOT / "en" / "index.html"
    return ROOT / SLUGS[key][lang] / "index.html"


LINK_RE = re.compile(r"\[([^\]]+)\]\(([^)]+)\)")


def resolve_href(url, lang):
    if url.startswith("@"):
        key, _, frag = url[1:].partition("#")
        return path_of(key, lang) + ("#" + frag if frag else "")
    return url


def md(text, lang):
    """Text mit [Link](Ziel)-Markup nach HTML."""
    out = []
    pos = 0
    for m in LINK_RE.finditer(text):
        out.append(esc(text[pos:m.start()]))
        href = resolve_href(m.group(2), lang)
        extern = href.startswith("http")
        attrs = ' target="_blank" rel="noopener"' if extern else ""
        out.append(f'<a href="{esc(href)}"{attrs}>{esc(m.group(1))}</a>')
        pos = m.end()
    out.append(esc(text[pos:]))
    return "".join(out)


def plain(text):
    return LINK_RE.sub(r"\1", text)


def jsonld(obj):
    s = json.dumps(obj, ensure_ascii=False, indent=2)
    return '<script type="application/ld+json">\n' + s.replace("</", "<\\/") + "\n</script>"


def cover_path(book_id, lang):
    if lang == "en" and (ROOT / "covers" / f"{book_id}-en.jpg").exists():
        return f"/covers/{book_id}-en.jpg"
    return f"/covers/{book_id}.jpg"


def alter_von(book_id):
    return "6-10" if re.match(r"^(1[1-9]|20|4[0-4])-", book_id) else "3-6"


def amazon_url(asin, lang):
    return f"https://www.amazon.{'de' if lang == 'de' else 'com'}/dp/{asin}"


def etsy_url(listing_id):
    return f"https://www.etsy.com/listing/{listing_id}"


def fmt_preis(x, lang):
    s = f"{x:.2f}"
    return s.replace(".", ",") if lang == "de" else s


def verfuegbar(book, lang):
    e = book[lang]
    return bool(e.get("asin") or e.get("etsy"))


# ---------------------------------------------------------------------------
# Kopf, Kopfzeile, Fusszeile
# ---------------------------------------------------------------------------
def head_html(lang, key, title, desc, og_image=None, og_desc=None, extra_head="", ld_blocks=()):
    ui = UI[lang]
    canonical = abs_url(key, lang)
    de_url, en_url = abs_url(key, "de"), abs_url(key, "en")
    if og_image:
        img_abs = SITE + og_image
        w, h = img_size(og_image)
        card = "summary_large_image"
        og_img_tags = (f'<meta property="og:image" content="{img_abs}">\n'
                       f'<meta property="og:image:width" content="{w}">\n'
                       f'<meta property="og:image:height" content="{h}">\n')
    else:
        img_abs = SITE + "/mvw-logo.png"
        card = "summary"
        og_img_tags = f'<meta property="og:image" content="{img_abs}">\n'
    og_desc = og_desc or desc
    other = "en_US" if lang == "de" else "de_DE"
    parts = [
        "<!doctype html>",
        f'<html lang="{ui["lang"]}">',
        "<head>",
        '<meta charset="utf-8">',
        '<meta name="viewport" content="width=device-width,initial-scale=1">',
        extra_head,
        f"<title>{esc(title)}</title>",
        f'<meta name="description" content="{esc(desc)}">',
        '<meta name="robots" content="index,follow,max-image-preview:large">',
        f'<link rel="canonical" href="{canonical}">',
        f'<link rel="alternate" hreflang="de" href="{de_url}">',
        f'<link rel="alternate" hreflang="en" href="{en_url}">',
        f'<link rel="alternate" hreflang="x-default" href="{de_url}">',
        '<meta property="og:type" content="website">',
        f'<meta property="og:site_name" content="{esc(AUTHOR)}">',
        f'<meta property="og:title" content="{esc(title)}">',
        f'<meta property="og:description" content="{esc(og_desc)}">',
        og_img_tags.rstrip("\n"),
        f'<meta property="og:url" content="{canonical}">',
        f'<meta property="og:locale" content="{ui["locale"]}">',
        f'<meta property="og:locale:alternate" content="{other}">',
        f'<meta name="twitter:card" content="{card}">',
        f'<meta name="twitter:title" content="{esc(title)}">',
        f'<meta name="twitter:description" content="{esc(og_desc)}">',
        f'<meta name="twitter:image" content="{img_abs}">',
        '<link rel="icon" type="image/png" href="/favicon-32.png">',
        '<link rel="icon" href="/favicon.ico" sizes="any">',
        '<link rel="apple-touch-icon" href="/apple-touch-icon.png">',
        '<link rel="stylesheet" href="/site.css">',
        '<script src="/tracking.js"></script>',
        '<script src="/consent.js"></script>',
    ]
    parts = [p for p in parts if p]
    parts.extend(jsonld(b) for b in ld_blocks)
    parts.append("</head>")
    return "\n".join(parts)


def header_html(lang, key):
    ui = UI[lang]
    home = path_of("home", lang)
    nav = [
        (home + "#buecher", ui["nav_books"], None),
        (path_of("ausdrucken", lang), ui["nav_print"], "ausdrucken"),
        (path_of("pakete", lang), ui["nav_bundles"], "pakete"),
        (path_of("faq", lang), ui["nav_faq"], "faq"),
    ]
    links = []
    for href, label, k in nav:
        cur = ' aria-current="page"' if k and k == key else ""
        links.append(f'<a href="{href}"{cur}>{esc(label)}</a>')
    sw = []
    for code in LANGS:
        cur = ' aria-current="true"' if code == lang else ""
        sw.append(f'<a href="{path_of(key, code)}" hreflang="{code}" lang="{code}"{cur}>{code.upper()}</a>')
    return (
        f'<a class="skip-link" href="#main">{esc(ui["skip"])}</a>\n'
        '<header class="site-header"><div class="site-header-inner">\n'
        f'  <a class="brand" href="{home}"><img src="/mvw-logo.png" alt="" {img_attrs("/mvw-logo.png")}><span>{esc(AUTHOR)}</span></a>\n'
        f'  <nav class="main-nav" aria-label="{esc(ui["nav_aria"])}">{"".join(links)}</nav>\n'
        f'  <nav class="langswitch" aria-label="{esc(ui["lang_aria"])}">{"".join(sw)}</nav>\n'
        "</div></header>"
    )


def footer_html(lang):
    ui = UI[lang]
    home = path_of("home", lang)

    def li(key):
        return f'<li><a href="{path_of(key, lang)}">{esc(NAV_LABEL[key][lang])}</a></li>'

    themes = "".join(li(k) for k in ("weihnachten", "nikolaus", "silvester", "dinosaurier"))
    printing = "".join(li(k) for k in ("ausdrucken", "woerter", "labyrinthe", "pakete"))
    info = (f'<li><a href="{home}">{esc(ui["home_label"])}</a></li>' + li("faq") +
            f'<li><a href="/impressum">{esc(ui["impressum"])}</a></li>'
            f'<li><a href="/datenschutz">{esc(ui["datenschutz"])}</a></li>')
    return (
        '<footer class="site-footer">\n'
        '  <img src="/mvw-logo.png" alt="" width="46" height="46" loading="lazy">\n'
        f'  <div class="name">{esc(AUTHOR)}</div>\n'
        f'  <nav class="footer-nav" aria-label="{esc(ui["footer_info"])}">\n'
        f'    <div><p class="footer-h">{esc(ui["footer_themes"])}</p><ul>{themes}</ul></div>\n'
        f'    <div><p class="footer-h">{esc(ui["footer_print"])}</p><ul>{printing}</ul></div>\n'
        f'    <div><p class="footer-h">{esc(ui["footer_info"])}</p><ul>{info}</ul></div>\n'
        "  </nav>\n"
        f'  <p class="ai-note">{esc(ui["footer_ai"])}</p>\n'
        f'  <div class="meta">&copy; 2026 &middot; <a href="/impressum">{esc(ui["impressum"])}</a> &middot; '
        f'<a href="/datenschutz">{esc(ui["datenschutz"])}</a></div>\n'
        "</footer>"
    )


def scripts_html(home=False):
    s = '<script src="/site.js" defer></script>'
    if home:
        s += '\n<script src="/home.js" defer></script>'
    return s


# ---------------------------------------------------------------------------
# Bausteine
# ---------------------------------------------------------------------------
def breadcrumb(lang, key):
    ui = UI[lang]
    label = NAV_LABEL[key][lang]
    h = (f'<nav class="breadcrumb" aria-label="{esc(ui["breadcrumb_aria"])}"><ol>'
         f'<li><a href="{path_of("home", lang)}">{esc(ui["home_label"])}</a></li>'
         f'<li><span aria-current="page">{esc(label)}</span></li></ol></nav>')
    ld = {"@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": 1, "name": ui["home_label"], "item": abs_url("home", lang)},
        {"@type": "ListItem", "position": 2, "name": label, "item": abs_url(key, lang)},
    ]}
    return h, ld


def book_tile(book, lang, home=False, eager=False):
    e = book[lang]
    ui = UI[lang]
    farbe = book["farbe"]
    cover = cover_path(book["id"], lang)
    href = f"#{book['id']}" if home else f"{path_of('home', lang)}#{book['id']}"
    data = ""
    ident = ""
    if home:
        ident = f' id="{book["id"]}"'
        data = (f' data-id="{book["id"]}" data-alter="{alter_von(book["id"])}" data-farbe="{farbe}"'
                f' data-asin="{e.get("asin") or ""}" data-etsy="{e.get("etsy") or ""}"'
                f'{" data-typ=" + chr(34) + book["typ"] + chr(34) if book.get("typ") else ""}')
    links = []
    if e.get("asin"):
        links.append(f'<a href="{amazon_url(e["asin"], lang)}" data-asin="{e["asin"]}" target="_blank" rel="noopener" '
                     f'aria-label="{esc(e["titel"])}: {esc(ui["amazon_link"])}">{esc(ui["amazon_link"])}</a>')
    if e.get("etsy"):
        links.append(f'<a href="{etsy_url(e["etsy"])}" target="_blank" rel="noopener" '
                     f'aria-label="{esc(e["titel"])}: {esc(ui["etsy_link"])}">{esc(ui["etsy_link"])}</a>')
    loading = "" if eager else ' loading="lazy"'
    return (
        f'<article class="tile"{ident}{data}>\n'
        f'  <span class="tile-top" style="background:{farbe}"></span>\n'
        f'  <a class="tile-open" href="{href}">\n'
        f'    <img class="tile-img" src="{cover}" alt="{esc(ui["alt_cover"].format(titel=e["titel"]))}" {img_attrs(cover)}{loading}>\n'
        f'    <h3 class="tile-title" style="color:{farbe}">{esc(e["titel"])}</h3>\n'
        "  </a>\n"
        f'  <p class="tile-sub">{esc(e["sub"])}</p>\n'
        f'  <div class="tile-links">{"".join(links)}</div>\n'
        "</article>"
    )


def book_grid(ids, lang, home=False):
    tiles = [book_tile(BUCH_NACH_ID[i], lang, home) for i in ids if verfuegbar(BUCH_NACH_ID[i], lang)]
    cls = "grid grid-zoom" if home else "grid grid-lg"
    gid = ' id="grid"' if home else ""
    return f'<div class="{cls}"{gid}>\n' + "\n".join(tiles) + "\n</div>"


ZAHLWORT = {
    "de": {1: "ein", 2: "zwei", 3: "drei", 4: "vier", 5: "fünf", 6: "sechs", 7: "sieben", 8: "acht",
           9: "neun", 10: "zehn", 11: "elf"},
    "en": {1: "one", 2: "two", 3: "three", 4: "four", 5: "five", 6: "six", 7: "seven", 8: "eight",
           9: "nine", 10: "ten", 11: "eleven"},
}


def zahl(n, lang):
    """Zahlen unter zwoelf ausgeschrieben, danach Ziffern."""
    return ZAHLWORT[lang].get(n, str(n))


def bundle_card(p, lang):
    ui = UI[lang]
    img = f"/pakete/{p['id']}_{lang}.jpg"
    buttons = []
    for fmt, lid in p["etsy"][lang]:
        label = ui["bundle_etsy_fmt"].format(f=fmt) if fmt else ui["bundle_etsy"]
        buttons.append(f'<a class="bundle-btn" href="{etsy_url(lid)}" target="_blank" rel="noopener">{esc(label)}</a>')
    preis = ui["bundle_price"].format(preis=fmt_preis(p["preis"], lang))
    summe = ui["bundle_sum"].format(summe=fmt_preis(p["summe"], lang))
    return (
        f'<article class="bundle" id="paket-{p["id"]}">\n'
        f'  <span class="bundle-top" style="background:{p["farbe"]}"></span>\n'
        f'  <img src="{img}" alt="{esc(p[lang])}" {img_attrs(img)} loading="lazy">\n'
        '  <div class="bundle-body">\n'
        f'    <h3 style="color:{p["farbe"]}">{esc(p[lang])}</h3>\n'
        f'    <p class="bundle-meta">{esc(ui["bundle_books"].format(n=zahl(p["anzahl"], lang), s=p["seiten"]))}</p>\n'
        f'    <p class="bundle-price"><strong>{esc(preis)}</strong><s>{esc(summe)}</s>'
        f'<span class="bundle-badge">{esc(ui["bundle_save"].format(p=p["spar"]))}</span></p>\n'
        f'    <div class="bundle-buttons">{"".join(buttons)}</div>\n'
        "  </div>\n"
        "</article>"
    )


def bundle_grid(ids, lang):
    return '<div class="bundle-grid">\n' + "\n".join(bundle_card(PAKET_NACH_ID[i], lang) for i in ids) + "\n</div>"


def xmas_block(lang):
    ui = UI[lang]
    p = PAKET_NACH_ID["jahreszeiten"]
    poster = f"/pakete/weihnachten_{lang}_poster.jpg"
    return (
        '<div class="xmas" id="xmas">\n'
        f'  <video id="xmas-video" muted loop playsinline controls preload="none" width="250" height="375" '
        f'poster="{poster}" src="/pakete/weihnachten_{lang}.mp4" aria-label="{esc(ui["xmas_video_label"])}"></video>\n'
        "  <div>\n"
        f'    <p class="eyebrow">{esc(ui["xmas_eyebrow"])}</p>\n'
        f'    <h3>{esc(ui["xmas_h3"])}</h3>\n'
        f'    <p>{esc(ui["xmas_p"])}</p>\n'
        f'    <a class="bundle-btn" href="{etsy_url(p["etsy"][lang][0][1])}" target="_blank" rel="noopener">{esc(ui["xmas_btn"])}</a>\n'
        "  </div>\n"
        "</div>"
    )


def topic_cards(keys, lang):
    items = []
    for k in keys:
        items.append(
            f'<li><a class="topic" href="{path_of(k, lang)}"><strong>{esc(NAV_LABEL[k][lang])}</strong>'
            f'<span>{esc(TOPIC_BLURB[k][lang])}</span></a></li>')
    return '<ul class="topic-grid">\n' + "\n".join(items) + "\n</ul>"


def faq_ld(pairs):
    return {"@type": "FAQPage", "mainEntity": [
        {"@type": "Question", "name": plain(q),
         "acceptedAnswer": {"@type": "Answer", "text": plain(a)}} for q, a in pairs]}


def books_ld(ids, lang, name=None):
    items = []
    for i in ids:
        b = BUCH_NACH_ID[i]
        e = b[lang]
        if not e.get("asin"):
            continue
        items.append({"@type": "ListItem", "position": len(items) + 1, "item": {
            "@type": "Book", "name": e["titel"],
            "author": {"@type": "Person", "name": AUTHOR},
            "bookFormat": "https://schema.org/Paperback",
            "inLanguage": lang,
            "url": amazon_url(e["asin"], lang),
            "image": SITE + cover_path(i, lang)}})
    if not items:
        return None
    ld = {"@type": "ItemList", "itemListElement": items}
    if name:
        ld["name"] = name
    return ld


def products_ld(ids, lang):
    out = []
    for i in ids:
        p = PAKET_NACH_ID[i]
        lid = p["etsy"][lang][0][1]
        if lang == "de":
            desc = f"{p['anzahl']} Bücher, {p['seiten']} Seiten als PDF zum Ausdrucken in A4 und US Letter. Sofort-Download bei Etsy."
        else:
            desc = f"{p['anzahl']} books, {p['seiten']} pages as a printable PDF in A4 and US Letter. Instant download on Etsy."
        out.append({
            "@type": "Product", "name": p[lang], "description": desc,
            "image": SITE + f"/pakete/{i}_{lang}.jpg",
            "brand": {"@type": "Brand", "name": AUTHOR},
            "offers": {"@type": "Offer", "url": etsy_url(lid), "priceCurrency": "EUR",
                       "price": f"{p['preis']:.2f}", "availability": "https://schema.org/InStock",
                       # Digitale Ware bei Etsy: Sofort-Download, keine Rückgabe (Etsy-AGB "Digitale Artikel", 84 aktive Angebote)
                       "shippingDetails": {
                           "@type": "OfferShippingDetails",
                           "shippingRate": {"@type": "MonetaryAmount", "value": "0", "currency": "EUR"},
                           "shippingDestination": [{"@type": "DefinedRegion", "addressCountry": c} for c in DIGITAL_LAENDER],
                           "deliveryTime": {"@type": "ShippingDeliveryTime",
                                            "handlingTime": {"@type": "QuantitativeValue", "minValue": 0, "maxValue": 0, "unitCode": "DAY"},
                                            "transitTime": {"@type": "QuantitativeValue", "minValue": 0, "maxValue": 0, "unitCode": "DAY"}}},
                       "hasMerchantReturnPolicy": {
                           "@type": "MerchantReturnPolicy", "applicableCountry": DIGITAL_LAENDER,
                           "returnPolicyCategory": "https://schema.org/MerchantReturnNotPermitted"}}})
    return out


DIGITAL_LAENDER = ["DE", "AT", "CH", "GB", "US"]


def site_entities(lang):
    org_id = SITE + "/#organization"
    job = ("Autor von Ausmalbüchern und Rätselbüchern für Kinder" if lang == "de"
           else "Author of coloring books and puzzle books for kids")
    return [
        {"@type": "Organization", "@id": org_id, "name": AUTHOR, "legalName": "Just Good Things Retail GmbH",
         "url": SITE + "/", "logo": SITE + "/mvw-logo.png", "email": CONTACT_MAIL,
         "address": {"@type": "PostalAddress", "streetAddress": "Kaiserswerther Str. 215",
                     "postalCode": "40474", "addressLocality": "Düsseldorf", "addressCountry": "DE"}},
        {"@type": "Person", "@id": SITE + "/#author", "name": AUTHOR, "url": SITE + "/",
         "jobTitle": job, "image": SITE + "/mvw-logo.png"},
        {"@type": "WebSite", "@id": SITE + "/#website", "url": SITE + "/", "name": AUTHOR,
         "inLanguage": ["de", "en"], "publisher": {"@id": org_id}},
    ]


def graph(items):
    return {"@context": "https://schema.org", "@graph": [i for i in items if i]}


# ---------------------------------------------------------------------------
# Startseite
# ---------------------------------------------------------------------------
def build_home(lang):
    ui = UI[lang]
    t = HOME[lang]
    key = "home"
    all_ids = [b["id"] for b in BUECHER]
    ld = graph(site_entities(lang) + [books_ld(all_ids, lang, "Malbücher von M. von Wedelstaedt" if lang == "de" else "Coloring books by M. von Wedelstaedt")]
               + products_ld([p["id"] for p in PAKETE], lang))
    extra = '<meta name="p:domain_verify" content="ef978efb78d8b2c78567ef743ccc1d6d"/>'
    head = head_html(lang, key, t["title"], t["desc"], None, t["og_desc"], extra, [ld])

    bonus_radios = []
    for i, tid in enumerate(("07-dinosaurier", "05-unterwasser", "03-bauernhof")):
        c = cover_path(tid, lang)
        bonus_radios.append(
            '<label class="pick">'
            f'<input type="radio" name="thema" value="{tid}"{" checked" if i == 0 else ""}>'
            f'<span class="pick-body"><img src="{c}" alt="" {img_attrs(c)} loading="lazy">'
            f'<span class="pick-name">{esc(t["bonus_themes"][tid])}</span></span></label>')

    privacy = "\n".join(f"    <p>{md(p, lang)}</p>" for p in t["privacy_p"])
    other_lang = "en" if lang == "de" else "de"
    body = f"""<body>
{header_html(lang, key)}
<main id="main">

<section class="hero">
  <p class="eyebrow">{esc(t["eyebrow_hero"])}</p>
  <img class="avatar" src="/mvw-logo.png" alt="{esc(t["avatar_alt"])}" width="132" height="132">
  <h1>{esc(AUTHOR)}<span class="h1-sub">{esc(t["h1_sub"])}</span></h1>
  <div class="rule"></div>
  <p class="bio">{t["bio"]}</p>
</section>

<section class="books" id="buecher">
  <div class="books-head">
    <p class="eyebrow">{esc(t["books_eyebrow"])}</p>
    <h2>{esc(t["books_h2"])}</h2>
    <p>{esc(t["books_p"])}</p>
  </div>
  <div class="filter" id="filter" role="group" aria-label="{esc(t["filter_aria"])}">
    <span class="filter-count" id="filter-count" aria-live="polite"></span>
  </div>
{book_grid(all_ids, lang, home=True)}
</section>

<section class="topics" id="themen">
  <div class="section-head">
    <h2>{esc(t["topics_h2"])}</h2>
    <p>{esc(t["topics_p"])}</p>
  </div>
{topic_cards(PAGE_ORDER, lang)}
</section>

<section class="bundles" id="pakete">
  <div class="bundles-head">
    <p class="eyebrow">{esc(t["bundles_eyebrow"])}</p>
    <h2>{esc(t["bundles_h2"])}</h2>
    <p>{md(t["bundles_p"], lang)}</p>
  </div>
{bundle_grid([p["id"] for p in PAKETE], lang)}
{xmas_block(lang)}
</section>

<dialog id="detail" aria-labelledby="detail-title">
  <div class="detail-inner">
    <button type="button" class="detail-close" id="detail-close" aria-label="{esc(t["detail_close"])}">&times;</button>
    <img class="detail-img" id="detail-img" alt="" width="320" height="414">
    <div class="detail-info">
      <h3 class="detail-title" id="detail-title"></h3>
      <p class="detail-sub" id="detail-sub"></p>
      <div class="detail-buttons">
        <a class="detail-amazon" id="detail-amazon" target="_blank" rel="noopener"></a>
        <a class="detail-etsy" id="detail-etsy" target="_blank" rel="noopener" hidden></a>
      </div>
      <p class="detail-shops" id="detail-shops" hidden></p>
      <a class="detail-bonus" id="detail-bonus" href="#bonus"></a>
    </div>
  </div>
</dialog>

<section class="bonus" id="bonus">
  <div class="bonus-card">
    <p class="eyebrow">{esc(t["bonus_eyebrow"])}</p>
    <h2>{esc(t["bonus_h2"])}</h2>
    <p class="bonus-p">{esc(t["bonus_p"])}</p>
    <form id="bonus-form">
      <fieldset>
        <legend>{esc(t["bonus_legend"])}</legend>
        <div class="bonus-options" id="bonus-options">{"".join(bonus_radios)}</div>
      </fieldset>
      <div class="field">
        <label for="bonus-email">{esc(t["bonus_label"])}</label>
        <input id="bonus-email" type="email" name="email" placeholder="{esc(t["bonus_placeholder"])}" required autocomplete="email">
      </div>
      <input type="text" name="website" value="" style="position:absolute;left:-9999px" tabindex="-1" autocomplete="off">
      <button type="submit" class="bonus-btn" id="bonus-btn">{esc(t["bonus_btn"])}</button>
      <p class="bonus-legal">{md(t["bonus_legal"], lang)}</p>
    </form>
    <p id="bonus-message" class="bonus-message" hidden></p>
  </div>
</section>

<section class="privacy" id="datenschutz">
  <div class="privacy-card">
    <h2>{esc(t["privacy_h2"])}</h2>
{privacy}
  </div>
</section>

</main>
{footer_html(lang)}
{scripts_html(home=True)}
</body>
</html>
"""
    return head + "\n" + body


# ---------------------------------------------------------------------------
# Themenseiten
# ---------------------------------------------------------------------------
def build_page(key, lang):
    ui = UI[lang]
    cfg = PAGES[key]
    t = cfg[lang]
    og = cfg.get("og")
    og_image = f"/pakete/{og}_{lang}.jpg" if og else None

    bc_html, bc_ld = breadcrumb(lang, key)
    ld_items = [bc_ld]

    faq_pairs = []
    if "faq_groups" in t:
        for _, qa in t["faq_groups"]:
            faq_pairs.extend(qa)
    else:
        faq_pairs = t["faq"]
    ld_items.append(faq_ld(faq_pairs))

    all_book_ids = list(cfg.get("books", []))
    for _, ids in cfg.get("book_groups", []):
        all_book_ids.extend(ids)
    bl = books_ld(all_book_ids, lang, t["h1"]) if all_book_ids else None
    ld_items.append(bl)
    if cfg.get("bundles"):
        ld_items.extend(products_ld(cfg["bundles"], lang))

    head = head_html(lang, key, t["title"], t["desc"], og_image, None, "", [graph(ld_items)])

    prose = []
    for h2, paras in t["sections"]:
        prose.append(f"<h2>{esc(h2)}</h2>")
        prose.extend(f"<p>{md(p, lang)}</p>" for p in paras)
    prose_html = ('<div class="prose">\n' + "\n".join(prose) + "\n</div>") if prose else ""

    blocks = []
    if cfg.get("video"):
        blocks.append(f'<section class="section" id="video">\n{xmas_block(lang)}\n</section>')
    if cfg.get("books"):
        blocks.append('<section class="section" id="buecher">\n'
                      f'  <div class="section-head"><h2>{esc(t["books_h2"])}</h2></div>\n'
                      f'{book_grid(cfg["books"], lang)}\n</section>')
    for gkey, ids in cfg.get("book_groups", []):
        blocks.append(f'<section class="section" id="{gkey}">\n'
                      f'  <div class="section-head"><h2>{esc(t["group_h2"][gkey])}</h2></div>\n'
                      f'{book_grid(ids, lang)}\n</section>')
    if cfg.get("bundles"):
        blocks.append('<section class="section" id="pakete">\n'
                      f'  <div class="section-head"><h2>{esc(t["bundles_h2"])}</h2></div>\n'
                      f'{bundle_grid(cfg["bundles"], lang)}\n</section>')

    if "faq_groups" in t:
        faq = ['<section class="faq" id="fragen">']
        for gname, qa in t["faq_groups"]:
            faq.append(f"<h2>{esc(gname)}</h2>")
            for q, a in qa:
                faq.append(f"<h3>{esc(q)}</h3>\n<p>{md(a, lang)}</p>")
        faq.append("</section>")
    else:
        faq = ['<section class="faq" id="fragen">', f'<h2>{esc(t["faq_h2"])}</h2>']
        for q, a in t["faq"]:
            faq.append(f"<h3>{esc(q)}</h3>\n<p>{md(a, lang)}</p>")
        faq.append("</section>")

    related = ('<section class="related">\n'
               f'  <h2>{esc(ui["related_h2"])}</h2>\n'
               f'{topic_cards(cfg["related"], lang)}\n</section>')
    bonus_hint = f'<p class="bonus-hint">{md(ui["bonus_hint"], lang)}</p>'

    # FAQ-Seite: Fragen zuerst, Themenkarten danach
    body = f"""<body>
{header_html(lang, key)}
<main id="main">
{bc_html}
<section class="page-hero">
  <p class="eyebrow">{esc(t["eyebrow"])}</p>
  <h1>{esc(t["h1"])}</h1>
  <p class="lead">{md(t["lead"], lang)}</p>
</section>
{prose_html}
{chr(10).join(blocks)}
{chr(10).join(faq)}
{related}
{bonus_hint}
</main>
{footer_html(lang)}
{scripts_html()}
</body>
</html>
"""
    return head + "\n" + body


# ---------------------------------------------------------------------------
# Sitemap
# ---------------------------------------------------------------------------
def build_sitemap():
    lines = ['<?xml version="1.0" encoding="UTF-8"?>',
             '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" '
             'xmlns:xhtml="http://www.w3.org/1999/xhtml">']
    keys = ["home"] + PAGE_ORDER
    for key in keys:
        for lang in LANGS:
            lines.append("  <url>")
            lines.append(f"    <loc>{abs_url(key, lang)}</loc>")
            lines.append(f"    <lastmod>{TODAY}</lastmod>")
            for code in LANGS:
                lines.append(f'    <xhtml:link rel="alternate" hreflang="{code}" href="{abs_url(key, code)}"/>')
            lines.append(f'    <xhtml:link rel="alternate" hreflang="x-default" href="{abs_url(key, "de")}"/>')
            lines.append("  </url>")
    for legal in ("impressum", "datenschutz"):
        lines.append("  <url>")
        lines.append(f"    <loc>{SITE}/{legal}</loc>")
        lines.append(f"    <lastmod>{TODAY}</lastmod>")
        lines.append("  </url>")
    lines.append("</urlset>")
    return "\n".join(lines) + "\n"


# ---------------------------------------------------------------------------
# Pruefungen und Ausgabe
# ---------------------------------------------------------------------------
def main_text_words(page_html):
    m = re.search(r"<main[^>]*>(.*?)</main>", page_html, re.S)
    body = m.group(1)
    body = re.sub(r"<script.*?</script>", " ", body, flags=re.S)
    body = re.sub(r"<[^>]+>", " ", body)
    body = html.unescape(body)
    return len(body.split())


def prose_words(key, lang):
    t = PAGES[key][lang]
    texts = [t["lead"]]
    for h2, paras in t["sections"]:
        texts.append(h2)
        texts.extend(paras)
    if "faq_groups" in t:
        for g, qa in t["faq_groups"]:
            texts.append(g)
            for q, a in qa:
                texts.extend([q, a])
    else:
        texts.append(t["faq_h2"])
        for q, a in t["faq"]:
            texts.extend([q, a])
    return len(plain(" ".join(texts)).split())


def main():
    problems = []
    report = []
    for lang in LANGS:
        pages = [("home", build_home(lang))] + [(k, build_page(k, lang)) for k in PAGE_ORDER]
        for key, content in pages:
            f = out_file(key, lang)
            f.parent.mkdir(parents=True, exist_ok=True)
            f.write_text(content, encoding="utf-8", newline="\n")
            title = (HOME[lang]["title"] if key == "home" else PAGES[key][lang]["title"])
            desc = (HOME[lang]["desc"] if key == "home" else PAGES[key][lang]["desc"])
            if len(title) > 60:
                problems.append(f"{lang}/{key}: Title {len(title)} Zeichen")
            if len(desc) > 155:
                problems.append(f"{lang}/{key}: Description {len(desc)} Zeichen")
            if len(re.findall(r"<h1[ >]", content)) != 1:
                problems.append(f"{lang}/{key}: H1-Anzahl")
            if key != "home":
                pw = prose_words(key, lang)
                report.append((lang, key, len(title), len(desc), pw, main_text_words(content)))
            else:
                report.append((lang, key, len(title), len(desc), 0, main_text_words(content)))
    (ROOT / "sitemap.xml").write_text(build_sitemap(), encoding="utf-8", newline="\n")
    print("lang page          title desc prose-words main-words")
    for r in report:
        print(f"{r[0]:4} {r[1]:13} {r[2]:5} {r[3]:4} {r[4]:11} {r[5]:10}")
    if problems:
        print("PROBLEME:")
        for p in problems:
            print(" -", p)
        sys.exit(1)
    print("OK")


if __name__ == "__main__":
    main()

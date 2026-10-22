# -*- coding: utf-8 -*-
"""Prueft die erzeugten Seiten: Links, Bilder, hreflang, Canonical, JSON-LD, Sitemap, Textregeln.

Aufruf:  python tools/check_site.py
Exit-Code 1, wenn ein Fehler gefunden wird. Hinweise (nur zur Durchsicht) stehen unter "HINWEIS".
"""
import json
import re
import sys
import xml.etree.ElementTree as ET
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlsplit

sys.path.insert(0, str(Path(__file__).resolve().parent))
from content import SITE, SLUGS, PAGE_ORDER, PAGES  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent
errors = []
notes = []


def err(msg):
    errors.append(msg)


def note(msg):
    notes.append(msg)


class Page(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.links = []
        self.imgs = []
        self.h = []          # (tag, text)
        self.metas = []
        self.linkrels = []
        self.jsonld = []
        self.tags = []
        self._cur = None
        self._buf = []
        self._ld = None
        self.in_main = False
        self.paras = []      # Absaetze innerhalb main
        self._p = None
        self.lang = None
        self.ids = []

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        self.tags.append(tag)
        if a.get("id"):
            self.ids.append(a["id"])
        if tag == "html":
            self.lang = a.get("lang")
        if tag == "main":
            self.in_main = True
        if tag == "a" and "href" in a:
            self.links.append(a["href"])
        if tag == "img":
            self.imgs.append(a)
        if tag in ("h1", "h2", "h3", "title"):
            self._cur = tag
            self._buf = []
        if tag == "meta":
            self.metas.append(a)
        if tag == "link":
            self.linkrels.append(a)
        if tag == "script" and a.get("type") == "application/ld+json":
            self._ld = []
        if tag == "p" and self.in_main:
            self._p = []

    def handle_endtag(self, tag):
        if tag == self._cur:
            self.h.append((tag, "".join(self._buf).strip()))
            self._cur = None
        if tag == "script" and self._ld is not None:
            self.jsonld.append("".join(self._ld))
            self._ld = None
        if tag == "p" and self._p is not None:
            self.paras.append("".join(self._p).strip())
            self._p = None
        if tag == "main":
            self.in_main = False

    def handle_data(self, data):
        if self._cur:
            self._buf.append(data)
        if self._ld is not None:
            self._ld.append(data)
        if self._p is not None:
            self._p.append(data)


def parse(path):
    p = Page()
    p.feed(path.read_text(encoding="utf-8"))
    return p


def page_file(key, lang):
    if key == "home":
        return ROOT / "index.html" if lang == "de" else ROOT / "en" / "index.html"
    return ROOT / SLUGS[key][lang] / "index.html"


def url_path(key, lang):
    if key == "home":
        return "/" if lang == "de" else "/en/"
    return "/" + SLUGS[key][lang]


def target_exists(path):
    """Bildet Vercel cleanUrls + Verzeichnis-index nach."""
    path = path.split("#")[0].split("?")[0]
    if path in ("", "/"):
        return (ROOT / "index.html").exists()
    rel = path.lstrip("/")
    f = ROOT / rel
    if f.is_file():
        return True
    if f.is_dir() and (f / "index.html").exists():
        return True
    if (ROOT / (rel.rstrip("/") + ".html")).is_file():
        return True
    return False


keys = ["home"] + PAGE_ORDER
pages = {}
for lang in ("de", "en"):
    for key in keys:
        f = page_file(key, lang)
        if not f.exists():
            err(f"fehlt: {f}")
            continue
        pages[(key, lang)] = parse(f)

# ---------------------------------------------------------------- Seitenebene
EMOJI = re.compile("[\U0001F300-\U0001FAFF☀-➿⭐✅✨❤]")
VERBOTEN = ["nutzen", "Mehrwert", "ganzheitlich", "beleuchten", "vertiefen", "revolution", "bahnbrechend",
            "In einer Welt, in der", "mehr als nur", "kostenlos", "beste ", "Testsieger", "bestes ",
            "leverage", "delve", "tapestry", "more than just", "free of charge"]
for (key, lang), p in pages.items():
    tag = f"{lang}/{key}"
    u = SITE + url_path(key, lang)
    canon = [l for l in p.linkrels if l.get("rel") == "canonical"]
    if len(canon) != 1 or canon[0]["href"] != u:
        err(f"{tag}: Canonical {canon}")
    alts = {l["hreflang"]: l["href"] for l in p.linkrels if l.get("rel") == "alternate"}
    exp = {"de": SITE + url_path(key, "de"), "en": SITE + url_path(key, "en"), "x-default": SITE + url_path(key, "de")}
    if alts != exp:
        err(f"{tag}: hreflang {alts}")
    if p.lang != lang:
        err(f"{tag}: html lang {p.lang}")
    if p.tags.count("main") != 1:
        err(f"{tag}: main-Anzahl")
    if [t for t, _ in p.h].count("h1") != 1:
        err(f"{tag}: h1-Anzahl")
    last = 0
    for t, _ in p.h:
        if t == "title":
            continue
        n = int(t[1])
        if n > last + 1:
            err(f"{tag}: Heading-Sprung {t}")
        last = n
    title = [x for t, x in p.h if t == "title"]
    if not title or len(title[0]) > 60:
        err(f"{tag}: Title-Laenge")
    desc = [m.get("content", "") for m in p.metas if m.get("name") == "description"]
    if not desc or not (50 <= len(desc[0]) <= 155):
        err(f"{tag}: Description-Laenge {len(desc[0]) if desc else None}")
    for name in ("og:title", "og:description", "og:image", "og:url", "og:locale"):
        if not any(m.get("property") == name for m in p.metas):
            err(f"{tag}: {name} fehlt")
    for name in ("twitter:card", "twitter:title", "twitter:image"):
        if not any(m.get("name") == name for m in p.metas):
            err(f"{tag}: {name} fehlt")
    for im in p.imgs:
        if "alt" not in im:
            err(f"{tag}: img ohne alt {im.get('src')}")
        if im.get("src") and (not im.get("width") or not im.get("height")):
            err(f"{tag}: img ohne Groesse {im.get('src')}")
        src = im.get("src")
        if src and src.startswith("/") and not target_exists(src):
            err(f"{tag}: Bild fehlt {src}")
    for href in p.links:
        if href.startswith(("http://", "https://", "mailto:")):
            continue
        if href.startswith("#"):
            if href[1:] and href[1:] not in p.ids:
                err(f"{tag}: Anker {href} nicht in Seite")
            continue
        if not target_exists(href):
            err(f"{tag}: Link kaputt {href}")
        if "#" in href and href.startswith("/"):
            base, frag = href.split("#", 1)
            if base in ("/", "/en/"):
                lg = "de" if base == "/" else "en"
                tp = pages.get(("home", lg))
                if tp and frag and frag not in tp.ids:
                    err(f"{tag}: Anker {href} fehlt auf Zielseite")
    ld_items = []
    for raw in p.jsonld:
        try:
            ld = json.loads(raw)
        except Exception as e:  # noqa: BLE001
            err(f"{tag}: JSON-LD ungueltig {e}")
            continue
        ld_items.extend(ld.get("@graph", [ld]))
    types = [i.get("@type") for i in ld_items]
    if "BreadcrumbList" not in types and key != "home":
        err(f"{tag}: BreadcrumbList fehlt")
    if "aggregateRating" in json.dumps(ld_items):
        err(f"{tag}: aggregateRating vorhanden")
    faq = [i for i in ld_items if i.get("@type") == "FAQPage"]
    if key != "home":
        if len(faq) != 1:
            err(f"{tag}: FAQPage-Anzahl {len(faq)}")
        else:
            qs = [(q["name"], q["acceptedAnswer"]["text"]) for q in faq[0]["mainEntity"]]
            h3s = [x for t, x in p.h if t == "h3"]
            for q, a in qs:
                if q not in h3s:
                    err(f"{tag}: FAQ-Frage nicht sichtbar: {q}")
                if a not in p.paras:
                    err(f"{tag}: FAQ-Antwort nicht identisch sichtbar: {a[:50]}")
            if key == "faq":
                if len(qs) < 10:
                    err(f"{tag}: FAQ-Anzahl {len(qs)}")
            elif not 3 <= len(qs) <= 4:
                err(f"{tag}: FAQ-Anzahl {len(qs)}")
    for para in p.paras:
        if "–" in para or "—" in para:
            err(f"{tag}: Gedankenstrich in: {para[:60]}")
        if EMOJI.search(para):
            err(f"{tag}: Emoji in: {para[:60]}")
        if "!" in para:
            err(f"{tag}: Ausrufezeichen in: {para[:60]}")
        for v in VERBOTEN:
            if v.lower() in para.lower():
                err(f"{tag}: verbotenes Wort '{v}' in: {para[:60]}")
        txt = re.sub(r"\b(St|M|Nr|ca)\.\s", "X ", para)
        txt = re.sub(r"\b\d{1,2}\.\s(?=[A-ZÄÖÜ])", "N ", txt)
        txt = re.sub(r"\b(December|January)\s\d{1,2}\.", "D.", txt)
        sentences = [s for s in re.split(r"(?<=[.?!…])\s+(?=[A-ZÄÖÜ„“\"])", txt.strip()) if s]
        if len(sentences) > 3 and key != "home":
            note(f"{tag}: {len(sentences)} Saetze: {para[:70]}")
    if key != "home":
        for para in p.paras:
            t2 = re.sub(r"\b\d{1,2}\.\s(?=[A-ZÄÖÜ])", "", para)
            t2 = re.sub(r"(December|Dezember)\s\d+", "", t2)
            t2 = re.sub(r"€\s?\d+[.,]\d+|\d+[.,]\d+\s?€", "", t2)
            for m in re.finditer(r"(?<![\w.,])([1-9]|1[01])(?![\w.,%]|\s?%)", t2):
                note(f"{tag}: Ziffer {m.group(1)} in: {para[:80]}")
                break

# ---------------------------------------------------------------- hreflang gegenseitig
for key in keys:
    if (key, "de") in pages and (key, "en") in pages:
        de, en = pages[(key, "de")], pages[(key, "en")]
        de_alt = {l["hreflang"]: l["href"] for l in de.linkrels if l.get("rel") == "alternate"}
        en_alt = {l["hreflang"]: l["href"] for l in en.linkrels if l.get("rel") == "alternate"}
        if de_alt["en"] != SITE + url_path(key, "en") or en_alt["de"] != SITE + url_path(key, "de"):
            err(f"{key}: hreflang nicht gegenseitig")

# ---------------------------------------------------------------- Sitemap
ns = {"s": "http://www.sitemaps.org/schemas/sitemap/0.9", "x": "http://www.w3.org/1999/xhtml"}
tree = ET.parse(ROOT / "sitemap.xml")
urls = tree.getroot().findall("s:url", ns)
locs = [u.find("s:loc", ns).text for u in urls]
if len(locs) != len(set(locs)):
    err("Sitemap: doppelte URLs")
for u in urls:
    loc = u.find("s:loc", ns).text
    if u.find("s:lastmod", ns).text != "2026-10-22":
        err(f"Sitemap lastmod {loc}")
    if not target_exists(urlsplit(loc).path):
        err(f"Sitemap-URL ohne Datei {loc}")
    for a in u.findall("x:link", ns):
        if a.get("href") not in locs:
            err(f"Sitemap: hreflang-Ziel fehlt {a.get('href')}")
for bad in ("bonus", "bestaetigen", "malbuch", "?lang"):
    if any(bad in l for l in locs):
        err(f"Sitemap enthaelt {bad}")
expected = len(keys) * 2 + 2
if len(locs) != expected:
    err(f"Sitemap: {len(locs)} URLs statt {expected}")

# ---------------------------------------------------------------- IndexNow
keyfiles = [f for f in ROOT.glob("*.txt") if re.fullmatch(r"[0-9a-f]{32}", f.stem)]
if len(keyfiles) != 1 or keyfiles[0].read_text().strip() != keyfiles[0].stem:
    err("IndexNow-Schluesseldatei")

# ---------------------------------------------------------------- Inhalte
for lang in ("de", "en"):
    for key in PAGE_ORDER:
        blob = json.dumps(PAGES[key][lang], ensure_ascii=False)
        if "–" in blob or "—" in blob:
            err(f"content {lang}/{key}: Gedankenstrich")

print(f"Seiten geprueft: {len(pages)}, Sitemap-URLs: {len(locs)}")
for n in notes:
    print("HINWEIS", n)
if errors:
    print("FEHLER:")
    for e in errors:
        print(" -", e)
    sys.exit(1)
print("ALLES OK")

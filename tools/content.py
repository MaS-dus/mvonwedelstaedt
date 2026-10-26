# -*- coding: utf-8 -*-
"""Texte und Seitenstruktur fuer build_seo.py.

Absatz-Markup: [Text](@seitenkey) verlinkt auf eine Seite in der Sprache der aktuellen Seite,
[Text](@seitenkey#anker) mit Anker, [Text](https://...) oder [Text](mailto:...) als normaler Link.
In JSON-LD (FAQPage) wird nur der Linktext uebernommen, damit der Text mit der sichtbaren Seite
uebereinstimmt.
"""

SITE = "https://mvonwedelstaedt.com"

# ---------------------------------------------------------------------------
# Seiten-Slugs (ohne fuehrenden Slash); "home" ist die Startseite
# ---------------------------------------------------------------------------
SLUGS = {
    "home": {"de": "", "en": "en"},
    "weihnachten": {"de": "ausmalbilder-weihnachten", "en": "en/christmas-coloring-pages"},
    "nikolaus": {"de": "ausmalbilder-nikolaus", "en": "en/st-nicholas-coloring-pages"},
    "silvester": {"de": "ausmalbilder-silvester", "en": "en/new-year-coloring-pages"},
    "dinosaurier": {"de": "ausmalbilder-dinosaurier", "en": "en/dinosaur-coloring-pages"},
    "ausdrucken": {"de": "ausmalbilder-zum-ausdrucken", "en": "en/printable-coloring-pages"},
    "woerter": {"de": "woerter-suchen-kinder", "en": "en/word-search-for-kids"},
    "labyrinthe": {"de": "labyrinthe-kinder", "en": "en/mazes-for-kids"},
    "pakete": {"de": "pakete", "en": "en/bundles"},
    "faq": {"de": "faq", "en": "en/faq"},
}

# Reihenfolge der Themenseiten (Footer, Themenkarten)
PAGE_ORDER = ["weihnachten", "nikolaus", "silvester", "dinosaurier", "ausdrucken",
              "woerter", "labyrinthe", "pakete", "faq"]

# ---------------------------------------------------------------------------
# Oberflaechentexte
# ---------------------------------------------------------------------------
UI = {
    "de": {
        "lang": "de",
        "locale": "de_DE",
        "site_name": "M. von Wedelstaedt",
        "skip": "Zum Inhalt springen",
        "home_label": "Startseite",
        "nav_aria": "Hauptmenü",
        "lang_aria": "Sprache / Language",
        "nav_books": "Bücher",
        "nav_print": "Zum Ausdrucken",
        "nav_bundles": "Pakete",
        "nav_faq": "Häufige Fragen",
        "breadcrumb_aria": "Brotkrumen",
        "amazon_link": "Bei Amazon",
        "etsy_link": "PDF bei Etsy",
        "alt_cover": "Cover: {titel}",
        "bundle_books": "{n} Bücher · {s} Seiten",
        "bundle_save": "Spare {p} %",
        "bundle_price": "Paket {preis} €",
        "bundle_sum": "statt {summe} €",
        "bundle_etsy": "Auf Etsy ansehen",
        "bundle_etsy_fmt": "Auf Etsy ansehen ({f})",
        "footer_themes": "Themen",
        "footer_print": "Zum Ausdrucken",
        "footer_info": "Informationen",
        "footer_ai": "Gestaltet und entwickelt von M. von Wedelstaedt, mit Unterstützung von KI.",
        "impressum": "Impressum",
        "datenschutz": "Datenschutz",
        "related_h2": "Weitere Themen",
        "bonus_hint": "Fünf Bonus-Ausmalbilder bekommst du gegen deine E-Mail-Adresse. [Hier anmelden](@home#bonus)",
        "xmas_eyebrow": "Weihnachten",
        "xmas_h3": "Weihnachtsmalbücher zum Sofort-Ausdrucken",
        "xmas_p": "Fünf Bücher von Halloween über Nikolaus und Weihnachten bis Silvester, als PDF in A4 und US Letter. Passend für den Advent und für Regentage.",
        "xmas_btn": "Jahreszeiten-Paket auf Etsy",
        "xmas_video_label": "Video zum Jahreszeiten-Paket",
    },
    "en": {
        "lang": "en",
        "locale": "en_US",
        "site_name": "M. von Wedelstaedt",
        "skip": "Skip to content",
        "home_label": "Home",
        "nav_aria": "Main menu",
        "lang_aria": "Sprache / Language",
        "nav_books": "Books",
        "nav_print": "Printables",
        "nav_bundles": "Bundles",
        "nav_faq": "FAQ",
        "breadcrumb_aria": "Breadcrumb",
        "amazon_link": "On Amazon",
        "etsy_link": "PDF on Etsy",
        "alt_cover": "Cover: {titel}",
        "bundle_books": "{n} books · {s} pages",
        "bundle_save": "Save {p}%",
        "bundle_price": "Bundle €{preis}",
        "bundle_sum": "instead of €{summe}",
        "bundle_etsy": "View on Etsy",
        "bundle_etsy_fmt": "View on Etsy ({f})",
        "footer_themes": "Topics",
        "footer_print": "Printables",
        "footer_info": "Information",
        "footer_ai": "Designed and developed by M. von Wedelstaedt, with the help of AI.",
        "impressum": "Impressum",
        "datenschutz": "Privacy (German)",
        "related_h2": "More topics",
        "bonus_hint": "You get five bonus coloring pages in exchange for your email address. [Sign up here](@home#bonus)",
        "xmas_eyebrow": "Christmas",
        "xmas_h3": "Christmas coloring books to print right away",
        "xmas_p": "Five books from Halloween through St. Nicholas and Christmas to New Year, as PDF in A4 and US Letter. Made for advent and rainy days.",
        "xmas_btn": "Seasonal bundle on Etsy",
        "xmas_video_label": "Video about the seasonal bundle",
    },
}

NAV_LABEL = {
    "weihnachten": {"de": "Ausmalbilder Weihnachten", "en": "Christmas coloring pages"},
    "nikolaus": {"de": "Ausmalbilder Nikolaus", "en": "St. Nicholas coloring pages"},
    "silvester": {"de": "Ausmalbilder Silvester", "en": "New Year coloring pages"},
    "dinosaurier": {"de": "Ausmalbilder Dinosaurier", "en": "Dinosaur coloring pages"},
    "ausdrucken": {"de": "Ausmalbilder zum Ausdrucken", "en": "Printable coloring pages"},
    "woerter": {"de": "Wortsuche für Kinder", "en": "Word search for kids"},
    "labyrinthe": {"de": "Labyrinthe für Kinder", "en": "Mazes for kids"},
    "pakete": {"de": "Pakete", "en": "Bundles"},
    "faq": {"de": "Häufige Fragen", "en": "FAQ"},
}

TOPIC_BLURB = {
    "weihnachten": {"de": "Malbuch mit Tieren, Nikolaus und Wortsuche zu Weihnachten",
                    "en": "A coloring book with animals, St. Nicholas and a Christmas word search"},
    "nikolaus": {"de": "50 Ausmalbilder rund um den Nikolaustag",
                 "en": "50 coloring pages around St. Nicholas Day"},
    "silvester": {"de": "50 Ausmalbilder zum Jahreswechsel",
                  "en": "50 coloring pages for New Year's Eve"},
    "dinosaurier": {"de": "Malbücher, Labyrinthe und Wortsuche mit Dinosauriern",
                    "en": "Coloring books, mazes and word search with dinosaurs"},
    "ausdrucken": {"de": "Alle PDFs der Reihe im Überblick",
                   "en": "All PDFs of the series at a glance"},
    "woerter": {"de": "80 Rätsel in drei Stufen, mit Lösungen",
                "en": "80 puzzles in three levels, with solutions"},
    "labyrinthe": {"de": "60 Labyrinthe pro Buch, ab vier Jahren",
                   "en": "60 mazes per book, ages four and up"},
    "pakete": {"de": "Mehrere Bücher als PDF auf einmal",
               "en": "Several books as a PDF at once"},
    "faq": {"de": "Alter, Druck, Etsy-Download und Rechte",
            "en": "Age, printing, Etsy download and usage rights"},
}

# ---------------------------------------------------------------------------
# Startseite
# ---------------------------------------------------------------------------
HOME = {
    "de": {
        "title": "Ausmalbücher & Rätselbücher für Kinder | M. von Wedelstaedt",
        "desc": "Ausmalbücher, Labyrinthe und Wortsuche für Kinder von drei bis zehn Jahren. Dicke Linien, große Motive. Taschenbuch bei Amazon, PDF bei Etsy.",
        "og_desc": "Dicke Linien, große Motive, ein Bild pro Seite. Ausmalbücher für Kinder von drei bis zehn Jahren, als Taschenbuch bei Amazon oder als PDF bei Etsy.",
        "eyebrow_hero": "Autor · Kinderbücher",
        "h1_sub": "Ausmalbücher und Rätselbücher für Kinder",
        "bio": "Ich habe drei Kinder und suchte am Nachmittag nach fünf ruhigen Minuten. Ausmalbücher sollten dabei helfen, aber die meisten waren entweder zu kindisch oder zu kompliziert, viele gefielen mir einfach nicht…<br><br>Also habe ich angefangen, eigene zu machen. Erst für die Kleineren mit dicken Linien, großen Bildern, ein Motiv pro Seite. Dann noch etwas für die Ältere, die schon sauer war, weil sie ihre eigenen wollte…<br>Wenn meine drei dann über ihren Bildern hängen, hat sich das gelohnt. Aus dem ersten Buch für zuhause ist schnell eine ganze Reihe geworden, und es kommen noch mehr. Gleichzeitig entstanden die ersten Bücher für die Ältere. So wie es aussieht, kommen da immer weitere dazu…",
        "books_eyebrow": "Die Reihe",
        "books_h2": "Mal- und Rätselbücher für kleine Hände",
        "books_p": "Ausmalbücher mit großen Motiven, dicken Linien und einem Bild pro Seite, dazu Labyrinthe und Wortsuchrätsel in drei Stufen. Für Kinder von drei bis zehn Jahren. Viele Titel gibt es als Taschenbuch bei Amazon, alle auch als PDF zum sofort Ausdrucken bei Etsy.",
        "topics_h2": "Themen im Überblick",
        "topics_p": "Von Weihnachten bis Dinosaurier: Hier findest du die Bücher und PDFs nach Thema geordnet.",
        "bundles_eyebrow": "Pakete zum Ausdrucken",
        "bundles_h2": "Mehrere Bücher auf einmal, bis zu 69 % günstiger",
        "bundles_p": "Die Pakete gibt es als PDF-Download bei Etsy. Sofort nach dem Kauf bereit, ausdrucken so oft du willst, für den privaten Gebrauch und die Schule. Der Preisvorteil gilt gegenüber dem Einzelkauf der Bücher im Shop. Alle sechs Pakete im Überblick: [Pakete](@pakete)",
        "bonus_eyebrow": "Gratis",
        "bonus_h2": "Fünf Bonus-Ausmalbilder zum Mitnehmen",
        "bonus_p": "Such dir eins von drei Themen aus. Du bekommst fünf Bilder als PDF und hörst von mir, wenn ein neues Buch erscheint.",
        "bonus_legend": "Thema wählen",
        "bonus_label": "E-Mail-Adresse",
        "bonus_placeholder": "deine@email.de",
        "bonus_btn": "Bonus-Bilder holen",
        "bonus_legal": "Du bekommst die Bonus-Bilder und gelegentlich Neuigkeiten per E-Mail. Jederzeit abbestellbar. [Datenschutz](/datenschutz)",
        "bonus_themes": {"07-dinosaurier": "Dinosaurier", "05-unterwasser": "Unter Wasser", "03-bauernhof": "Bauernhof"},
        "privacy_h2": "Datenschutz",
        "privacy_p": [
            "Diese Seite setzt keine Cookies oder Tracking-Skripte ein. Die vollständige [Datenschutzerklärung](/datenschutz) findest du hier.",
            "Die zu dieser Marke gehörende Pinterest-App veröffentlicht ausschließlich Inhalte auf dem eigenen Pinterest-Konto von M. von Wedelstaedt. Sie greift auf keine Pins, Pinnwände oder Daten anderer Pinterest-Nutzer:innen zu und wird nicht für andere Personen oder Unternehmen betrieben.",
            "Links zu Buchtiteln führen zu amazon.de bzw. amazon.com und zu etsy.com. Dort gilt jeweils die Datenschutzerklärung von Amazon bzw. Etsy.",
        ],
        "detail_close": "Schließen",
        "avatar_alt": "Monogramm M. von Wedelstaedt",
        "filter_aria": "Nach Alter filtern",
        "email_hint_alt": "",
    },
    "en": {
        "title": "Coloring Books & Puzzle Books for Kids | M. von Wedelstaedt",
        "desc": "Coloring books, mazes and word search for kids ages three to ten. Thick lines, big pictures. Paperback on Amazon, printable PDF on Etsy.",
        "og_desc": "Thick lines, big pictures, one picture per page. Coloring books for kids ages three to ten, as paperback on Amazon or as a PDF on Etsy.",
        "eyebrow_hero": "Author · Children's Books",
        "h1_sub": "Coloring books and puzzle books for kids",
        "bio": "I have three kids, and in the afternoon I was looking for five quiet minutes. Coloring books were supposed to help, but most were either too babyish or too complicated, and plenty of them I just didn't like…<br><br>So I started making my own. First for the little ones, with thick lines, big pictures, one picture per page. Then something for my oldest, who was already annoyed because she wanted her own…<br>When my three are bent over their pictures, it's all worth it. What began as a first book for home quickly turned into a whole series, and more are coming. At the same time the first books for my oldest came along. The way it looks, more will keep joining…",
        "books_eyebrow": "The Series",
        "books_h2": "Coloring and Puzzle Books for Little Hands",
        "books_p": "Coloring books with big pictures, thick lines and one picture per page, plus mazes and word search puzzles in three levels. For kids ages three to ten. Many titles are available as paperback on Amazon, and all of them as a printable PDF on Etsy.",
        "topics_h2": "Topics at a glance",
        "topics_p": "From Christmas to dinosaurs: find the books and PDFs sorted by topic.",
        "bundles_eyebrow": "Printable bundles",
        "bundles_h2": "Several books at once, up to 69% cheaper",
        "bundles_p": "The bundles are PDF downloads on Etsy. Ready right after purchase, print as often as you like, for private use and school. The saving compares with buying the books one by one in the shop. See all six bundles: [Bundles](@pakete)",
        "bonus_eyebrow": "Free",
        "bonus_h2": "Five free bonus coloring pages",
        "bonus_p": "Pick one of three themes. You get five pictures as a PDF, and I'll let you know when a new book comes out.",
        "bonus_legend": "Choose a theme",
        "bonus_label": "Email address",
        "bonus_placeholder": "your@email.com",
        "bonus_btn": "Get my bonus pages",
        "bonus_legal": "You will get the bonus pages and occasional news by email. Unsubscribe anytime. [Privacy (German)](/datenschutz)",
        "bonus_themes": {"07-dinosaurier": "Dinosaurs", "05-unterwasser": "Under the Sea", "03-bauernhof": "On the Farm"},
        "privacy_h2": "Privacy",
        "privacy_p": [
            "This site does not use cookies or tracking scripts. You can find the full [privacy policy](/datenschutz) (German) here.",
            "The Pinterest app associated with this brand only publishes content on M. von Wedelstaedt's own Pinterest account. It does not access any pins, boards or data of other Pinterest users, and is not operated on behalf of other people or companies.",
            "Links to book titles lead to amazon.de or amazon.com and to etsy.com. The privacy policy of Amazon or Etsy applies there.",
        ],
        "detail_close": "Close",
        "avatar_alt": "Monogram M. von Wedelstaedt",
        "filter_aria": "Filter by age",
        "email_hint_alt": "",
    },
}

# ---------------------------------------------------------------------------
# Themenseiten
# ---------------------------------------------------------------------------
# Felder: title, desc, h1, eyebrow, lead, sections [(h2, [absaetze])], books_h2, books | book_groups,
#         bundles_h2, bundles, faq_h2, faq [(frage, antwort)], related [keys], og (Paketbild), video
PAGES = {}

# ---- Weihnachten ----------------------------------------------------------
PAGES["weihnachten"] = {
    "og": "jahreszeiten",
    "video": True,
    "books": ["10-weihnachten", "23-nikolaus", "44-wortsuche-weihnachten"],
    "bundles": ["jahreszeiten", "alles"],
    "related": ["nikolaus", "silvester", "ausdrucken", "pakete"],
    "de": {
        "title": "Ausmalbilder Weihnachten zum Ausdrucken | M. von Wedelstaedt",
        "desc": "Ausmalbilder zu Weihnachten für Kinder: Malbuch mit Tieren, Nikolaus und Wortsuche. Als Taschenbuch bei Amazon oder als PDF zum Ausdrucken bei Etsy.",
        "h1": "Ausmalbilder zu Weihnachten für Kinder",
        "eyebrow": "Weihnachten",
        "lead": "Für den Advent gibt es drei Bücher mit Weihnachtsmotiven: ein Malbuch mit Tieren, ein Malbuch zum Nikolaus und eine Wortsuche. Du bekommst sie als Taschenbuch bei Amazon oder als PDF, das du sofort bei Etsy herunterladen und selbst ausdrucken kannst.",
        "sections": [
            ("Malbuch und Wortsuche zu Weihnachten", [
                "„Weihnachten mit Tieren“ enthält 50 Ausmalbilder mit festlichen Motiven. Jedes Bild hat eine eigene Seite, die Linien sind dick und die Motive groß. Das Buch ist für Kinder ab drei Jahren gedacht.",
                "Die „Weihnachtsrätsel Wortsuche“ ist für Kinder ab sechs Jahren. Sie enthält 80 Rätsel in drei Stufen, und zu den Rätseln gibt es Lösungen.",
                "Wer lieber Nikolausbilder ausmalt, findet auf der Seite [Ausmalbilder Nikolaus](@nikolaus) das passende Buch.",
            ]),
            ("Taschenbuch oder PDF zum Ausdrucken", [
                "Das Taschenbuch bestellst du bei Amazon. Das PDF kaufst du bei Etsy und lädst es direkt nach dem Kauf herunter. Es gibt die Seiten in A4 und US Letter, und du kannst jede Seite einzeln ausdrucken.",
                "Mit dem Jahreszeiten-Paket bekommst du fünf Malbücher auf einmal: Halloween, Erntedank, Nikolaus, Weihnachten und Silvester. Es umfasst 250 Seiten und kostet 12,99 €. Weitere Pakete findest du auf der Seite [Pakete](@pakete).",
            ]),
            ("Ideen für die Adventszeit", [
                "Du kannst im Advent jeden Tag ein Bild ausdrucken und gemeinsam ausmalen. Fertige Seiten lassen sich ans Fenster hängen oder als kleines Geschenk verschenken.",
                "Für Filzstifte ist dickeres Papier eine gute Wahl, weil die Farbe dann nicht durchscheint. Buntstifte funktionieren auf jedem Papier.",
                "Wenn mehrere Kinder mitmachen, druckst du dasselbe Bild mehrmals aus. Das geht bei den PDF-Seiten so oft, wie du möchtest, für den privaten Gebrauch und die Schule.",
            ]),
        ],
        "books_h2": "Weihnachtsbücher im Überblick",
        "bundles_h2": "Pakete mit Weihnachtsbüchern",
        "faq_h2": "Fragen zu den Weihnachtsbüchern",
        "faq": [
            ("Ab welchem Alter sind die Weihnachtsbücher geeignet?",
             "Die Ausmalbücher sind für Kinder ab drei Jahren gedacht, die Wortsuche für Kinder ab sechs Jahren."),
            ("Kann ich einzelne Weihnachtsbilder ausdrucken?",
             "Ja, jede Seite des PDFs lässt sich einzeln ausdrucken, in A4 oder US Letter. Das geht für den privaten Gebrauch und die Schule so oft, wie du möchtest."),
            ("Wie bekomme ich das PDF?",
             "Du kaufst es bei Etsy und lädst die Datei direkt nach dem Kauf herunter. Wie der Download im Detail funktioniert, steht in den [häufigen Fragen](@faq)."),
            ("Gibt es die Bücher auch gedruckt?",
             "Ja, „Weihnachten mit Tieren“, „Nikolaus kommt“ und die „Weihnachtsrätsel Wortsuche“ gibt es als Taschenbuch bei Amazon."),
        ],
    },
    "en": {
        "title": "Christmas Coloring Pages to Print | M. von Wedelstaedt",
        "desc": "Christmas coloring pages for kids: a coloring book with animals, St. Nicholas and a word search. Paperback on Amazon or printable PDF on Etsy.",
        "h1": "Christmas coloring pages for kids",
        "eyebrow": "Christmas",
        "lead": "For advent there are three books with Christmas pictures: a coloring book with animals, a coloring book for St. Nicholas Day and a word search. You can get them as paperbacks on Amazon, or as a PDF that you download from Etsy right away and print yourself.",
        "sections": [
            ("A coloring book and a word search for Christmas", [
                "“Christmas with Animals” has 50 festive coloring pages. Each picture gets its own page, with thick lines and big motifs. The book is made for kids ages three and up.",
                "“Christmas Word Search” is for kids ages six and up. It has 80 puzzles in three levels, and solutions are included.",
                "If your child prefers St. Nicholas pictures, the page on [St. Nicholas coloring pages](@nikolaus) has the matching book.",
            ]),
            ("Paperback or printable PDF", [
                "You order the paperback on Amazon. You buy the PDF on Etsy and download it right after the purchase. The pages come in A4 and US Letter, and you can print each page on its own.",
                "The seasonal bundle gives you five coloring books at once: Halloween, Thanksgiving, St. Nicholas, Christmas and New Year. It has 250 pages and costs €12.99. You can find more bundles on the [Bundles](@pakete) page.",
            ]),
            ("Ideas for advent", [
                "In advent you can print one picture a day and color it together. Finished pages can go in the window or become a small gift.",
                "Thicker paper is a good choice for felt-tip pens because the color does not show through. Colored pencils work on any paper.",
                "If several kids join in, print the same picture a few times. With the PDF pages you can do that as often as you like, for private use and school.",
            ]),
        ],
        "books_h2": "The Christmas books at a glance",
        "bundles_h2": "Bundles with Christmas books",
        "faq_h2": "Questions about the Christmas books",
        "faq": [
            ("What age are the Christmas books for?",
             "The coloring books are made for kids ages three and up, the word search for kids ages six and up."),
            ("Can I print single Christmas pages?",
             "Yes, you can print each page of the PDF on its own, in A4 or US Letter. For private use and school, you can print as often as you like."),
            ("How do I get the PDF?",
             "You buy it on Etsy and download the file right after the purchase. The [FAQ](@faq) explains the download in more detail."),
            ("Are the books available in print?",
             "Yes, “Christmas with Animals”, “Here Comes St. Nicholas” and “Christmas Word Search” are available as paperbacks on Amazon."),
        ],
    },
}

# ---- Nikolaus -------------------------------------------------------------
PAGES["nikolaus"] = {
    "og": "jahreszeiten",
    "books": ["23-nikolaus", "10-weihnachten", "44-wortsuche-weihnachten", "25-silvester"],
    "bundles": ["jahreszeiten"],
    "related": ["weihnachten", "silvester", "ausdrucken", "faq"],
    "de": {
        "title": "Ausmalbilder Nikolaus zum Ausdrucken | M. von Wedelstaedt",
        "desc": "Ausmalbilder zum Nikolaustag für Kinder ab drei Jahren: Malbuch mit 50 Bildern als Taschenbuch bei Amazon oder als PDF zum Ausdrucken bei Etsy.",
        "h1": "Ausmalbilder zum Nikolaus für Kinder",
        "eyebrow": "Nikolaus",
        "lead": "Das Malbuch „Nikolaus kommt“ hat 50 Ausmalbilder rund um den Nikolaustag. Du kannst es als Taschenbuch bei Amazon bestellen oder als PDF bei Etsy kaufen und zu Hause ausdrucken.",
        "sections": [
            ("Ausmalen zum Nikolaustag", [
                "Der Nikolaustag ist am 6. Dezember. In vielen Familien stellen die Kinder am Abend davor einen Stiefel vor die Tür und finden am Morgen kleine Geschenke darin.",
                "Passend dazu enthält „Nikolaus kommt“ 50 Ausmalbilder. Jedes Bild steht allein auf einer Seite, mit dicken Linien und großen Motiven, damit schon Kinder ab drei Jahren es ausmalen können.",
            ]),
            ("So kommt das Buch zu dir", [
                "Als Taschenbuch bestellst du „Nikolaus kommt“ bei Amazon. Als PDF kaufst du es bei Etsy und lädst es sofort herunter. Die Seiten gibt es in A4 und US Letter, jede Seite lässt sich einzeln ausdrucken.",
                "Wer die Bilder vor dem 6. Dezember braucht, kommt mit dem PDF am schnellsten ans Ziel, weil es keinen Versand gibt.",
                "Das Jahreszeiten-Paket enthält das Nikolaus-Buch zusammen mit Halloween, Erntedank, Weihnachten und Silvester. Es kostet 12,99 € für fünf Bücher mit 250 Seiten.",
            ]),
            ("Ideen zum Ausmalen und Verschenken", [
                "Du kannst ausgemalte Seiten als Tischdeko für den Nikolausabend auslegen oder in eine Mappe heften. Schreibe den Namen des Kindes oben auf die Seite, dann wird daraus ein persönliches Geschenk für den Stiefel.",
                "Wer mehrere Kinder beschäftigen möchte, druckt dasselbe Motiv mehrfach aus. Die PDF-Seiten dürfen privat und in der Schule so oft ausgedruckt werden, wie du möchtest.",
                "Auch in der Schule dürfen die Seiten für die Klasse ausgedruckt werden. Weitergeben oder verkaufen darfst du die Dateien nicht.",
                "Mehr Winterthemen findest du auf den Seiten [Ausmalbilder Weihnachten](@weihnachten) und [Ausmalbilder Silvester](@silvester).",
            ]),
        ],
        "books_h2": "Das Nikolaus-Buch und weitere Winterbücher",
        "bundles_h2": "Paket mit dem Nikolaus-Buch",
        "faq_h2": "Fragen zum Nikolaus-Malbuch",
        "faq": [
            ("Wann ist der Nikolaustag?",
             "Am 6. Dezember. Mit dem PDF druckst du die Bilder rechtzeitig vorher aus."),
            ("Für welches Alter ist „Nikolaus kommt“ gedacht?",
             "Für Kinder ab drei Jahren. Die Linien sind dick und die Motive groß."),
            ("Gibt es das Nikolaus-Malbuch gedruckt?",
             "Ja, als Taschenbuch bei Amazon."),
            ("Was kostet das PDF?",
             "Ein einzelnes Malbuch kostet als PDF bei Etsy 4,99 €. Das Jahreszeiten-Paket mit fünf Büchern kostet 12,99 €."),
        ],
    },
    "en": {
        "title": "St. Nicholas Coloring Pages to Print | M. von Wedelstaedt",
        "desc": "St. Nicholas Day coloring pages for kids ages three and up: a book with 50 pictures, as paperback on Amazon or printable PDF on Etsy.",
        "h1": "St. Nicholas coloring pages for kids",
        "eyebrow": "St. Nicholas",
        "lead": "The coloring book “Here Comes St. Nicholas” has 50 coloring pages around St. Nicholas Day. You can order it as a paperback on Amazon, or buy the PDF on Etsy and print it at home.",
        "sections": [
            ("Coloring for St. Nicholas Day", [
                "St. Nicholas Day is on December 6. In many German families, children put a boot outside the door the evening before and find small gifts in it the next morning.",
                "To go with it, “Here Comes St. Nicholas” has 50 coloring pages. Each picture sits alone on its page, with thick lines and big motifs, so kids ages three and up can color them.",
            ]),
            ("How the book gets to you", [
                "You order “Here Comes St. Nicholas” as a paperback on Amazon. You buy the PDF on Etsy and download it right away. The pages come in A4 and US Letter, and you can print each page on its own.",
                "If you need the pictures before December 6, the PDF is the fastest way, because nothing has to be shipped.",
                "The seasonal bundle holds the St. Nicholas book together with Halloween, Thanksgiving, Christmas and New Year. It costs €12.99 for five books with 250 pages.",
            ]),
            ("Ideas for coloring and giving", [
                "You can lay finished pages out as table decoration for the evening or put them in a folder. Write the child's name at the top of the page, and it becomes a personal gift for the boot.",
                "If you want to keep several kids busy, print the same motif a few times. You may print the PDF pages for private use and school as often as you like.",
                "You may also print the pages for your class at school. You may not pass the files on or sell them.",
                "You can find more winter topics on the pages [Christmas coloring pages](@weihnachten) and [New Year coloring pages](@silvester).",
            ]),
        ],
        "books_h2": "The St. Nicholas book and more winter books",
        "bundles_h2": "Bundle with the St. Nicholas book",
        "faq_h2": "Questions about the St. Nicholas coloring book",
        "faq": [
            ("When is St. Nicholas Day?",
             "On December 6. With the PDF you can print the pictures in good time before."),
            ("What age is “Here Comes St. Nicholas” for?",
             "For kids ages three and up. The lines are thick and the motifs are big."),
            ("Is the St. Nicholas coloring book available in print?",
             "Yes, as a paperback on Amazon."),
            ("How much does the PDF cost?",
             "A single coloring book costs €4.99 as a PDF on Etsy. The seasonal bundle with five books costs €12.99."),
        ],
    },
}

# ---- Silvester ------------------------------------------------------------
PAGES["silvester"] = {
    "og": "jahreszeiten",
    "books": ["25-silvester", "10-weihnachten", "23-nikolaus"],
    "bundles": ["jahreszeiten"],
    "related": ["weihnachten", "nikolaus", "ausdrucken", "faq"],
    "de": {
        "title": "Ausmalbilder Silvester zum Ausdrucken | M. von Wedelstaedt",
        "desc": "Ausmalbilder zu Silvester für Kinder: Malbuch Silvester Feuerwerk mit 50 Bildern als Taschenbuch bei Amazon oder als PDF zum Ausdrucken bei Etsy.",
        "h1": "Ausmalbilder zu Silvester für Kinder",
        "eyebrow": "Silvester",
        "lead": "„Silvester Feuerwerk“ ist ein Malbuch mit 50 Ausmalbildern zum Jahreswechsel. Du bekommst es als Taschenbuch bei Amazon oder als PDF bei Etsy, das du sofort ausdrucken kannst.",
        "sections": [
            ("Ein Malbuch zum Jahreswechsel", [
                "„Silvester Feuerwerk“ hat 50 Ausmalbilder rund um den Jahreswechsel, für Kinder ab drei Jahren. Jedes Bild steht allein auf einer Seite, mit dicken Linien und großen Motiven.",
                "Das Buch gibt es als Taschenbuch bei Amazon. Das PDF kaufst du bei Etsy und lädst es direkt nach dem Kauf herunter, in A4 oder US Letter.",
            ]),
            ("Silvester mit Kindern", [
                "Am Silvesterabend ist die Zeit bis Mitternacht für Kinder oft lang. Ein Ausmalbild kann die Wartezeit verkürzen, ob am Tisch oder auf dem Sofa.",
                "Du kannst vorab ein paar Seiten ausdrucken und mit Stiften in einer Schachtel bereitlegen. Wer mit anderen Familien feiert, druckt ein Motiv mehrfach aus. Das geht privat so oft, wie du möchtest.",
                "Fertige Bilder eignen sich als Dekoration für die Neujahrsfeier. Hänge sie an eine Schnur oder klebe sie an die Wand.",
            ]),
            ("Eine Neujahrskarte aus dem Ausmalbild", [
                "Aus einem ausgemalten Bild wird schnell eine Neujahrskarte. Druck die Seite auf Karton, falte sie in der Mitte und schreibe die Wünsche innen hinein.",
                "So können Kinder Großeltern, Freunden oder Nachbarn zum Jahreswechsel etwas Selbstgemachtes schenken.",
            ]),
            ("Das passende Paket", [
                "Im Jahreszeiten-Paket steckt „Silvester Feuerwerk“ zusammen mit Halloween, Erntedank, Nikolaus und Weihnachten. Fünf Malbücher mit 250 Seiten kosten 12,99 €.",
                "Die anderen Winterthemen findest du auf den Seiten [Ausmalbilder Weihnachten](@weihnachten) und [Ausmalbilder Nikolaus](@nikolaus). Eine Übersicht über alle PDFs gibt es unter [Ausmalbilder zum Ausdrucken](@ausdrucken).",
            ]),
        ],
        "books_h2": "Das Silvester-Buch und weitere Winterbücher",
        "bundles_h2": "Paket mit dem Silvester-Buch",
        "faq_h2": "Fragen zum Silvester-Malbuch",
        "faq": [
            ("Für welches Alter ist das Silvester-Malbuch?",
             "Für Kinder ab drei Jahren. Die Motive sind groß und die Linien dick."),
            ("Gibt es die Bilder auch als PDF?",
             "Ja, bei Etsy. Du lädst die Datei nach dem Kauf sofort herunter und druckst jede Seite einzeln aus."),
            ("Was kostet das PDF?",
             "Ein einzelnes Malbuch kostet als PDF 4,99 €. Im Jahreszeiten-Paket mit fünf Büchern kostet es zusammen 12,99 €."),
            ("Darf ich die Seiten in der Schule ausdrucken?",
             "Ja, für den privaten Gebrauch und in der Schule. Weitergeben oder verkaufen darfst du die Dateien nicht."),
        ],
    },
    "en": {
        "title": "New Year Coloring Pages to Print | M. von Wedelstaedt",
        "desc": "New Year's Eve coloring pages for kids: the book with 50 pictures, as paperback on Amazon or printable PDF on Etsy.",
        "h1": "New Year coloring pages for kids",
        "eyebrow": "New Year's Eve",
        "lead": "“New Year's Eve Sparkle” is a coloring book with 50 coloring pages for the turn of the year. You can get it as a paperback on Amazon, or as a PDF on Etsy that you can print right away.",
        "sections": [
            ("A coloring book for the turn of the year", [
                "“New Year's Eve Sparkle” has 50 coloring pages around New Year, for kids ages three and up. Each picture sits alone on its page, with thick lines and big motifs.",
                "The book is available as a paperback on Amazon. You buy the PDF on Etsy and download it right after the purchase, in A4 or US Letter.",
            ]),
            ("New Year's Eve with kids", [
                "On New Year's Eve, the time until midnight can feel long to kids. A coloring page can shorten the wait, at the table or on the sofa.",
                "You can print a few pages beforehand and put them in a box with pens. If you celebrate with other families, print one motif several times. For private use, you can do that as often as you like.",
                "Finished pictures make good decoration for the party. Hang them on a string or stick them on the wall.",
            ]),
            ("A New Year card from a coloring page", [
                "A colored picture quickly becomes a New Year card. Print the page on card stock, fold it in the middle and write the wishes inside.",
                "That way kids can give grandparents, friends or neighbors something handmade for the new year.",
            ]),
            ("The matching bundle", [
                "The seasonal bundle holds “New Year's Eve Sparkle” together with Halloween, Thanksgiving, St. Nicholas and Christmas. Five coloring books with 250 pages cost €12.99.",
                "You can find the other winter topics on the pages [Christmas coloring pages](@weihnachten) and [St. Nicholas coloring pages](@nikolaus). An overview of all PDFs is on [Printable coloring pages](@ausdrucken).",
            ]),
        ],
        "books_h2": "The New Year book and more winter books",
        "bundles_h2": "Bundle with the New Year book",
        "faq_h2": "Questions about the New Year coloring book",
        "faq": [
            ("What age is the New Year coloring book for?",
             "For kids ages three and up. The motifs are big and the lines are thick."),
            ("Are the pictures available as a PDF?",
             "Yes, on Etsy. You download the file right after the purchase and print each page on its own."),
            ("How much does the PDF cost?",
             "A single coloring book costs €4.99 as a PDF. In the seasonal bundle with five books, it costs €12.99 together."),
            ("May I print the pages at school?",
             "Yes, for private use and at school. You may not pass the files on or sell them."),
        ],
    },
}

# ---- Dinosaurier ----------------------------------------------------------
PAGES["dinosaurier"] = {
    "og": "staffel1",
    "books": ["07-dinosaurier", "15-dinosaurier", "31-labyrinth-dino", "41-wortsuche-dino"],
    "bundles": ["staffel1", "alles"],
    "related": ["labyrinthe", "woerter", "ausdrucken", "pakete"],
    "de": {
        "title": "Ausmalbilder Dinosaurier zum Ausdrucken | M. von Wedelstaedt",
        "desc": "Ausmalbilder Dinosaurier für Kinder: Malbücher ab drei und ab sechs Jahren, Labyrinthe und Wortsuche. Taschenbuch bei Amazon oder PDF bei Etsy.",
        "h1": "Ausmalbilder Dinosaurier für Kinder",
        "eyebrow": "Dinosaurier",
        "lead": "Dinosaurier gibt es in der Reihe gleich viermal: als Malbuch für kleine Kinder, als Malbuch für Kinder ab sechs, als Labyrinthbuch und als Wortsuche. Alle vier gibt es als PDF bei Etsy und als Taschenbuch bei Amazon.",
        "sections": [
            ("Dinosaurier für zwei Altersstufen", [
                "Das Malbuch „Dinosaurier“ für Kinder ab drei Jahren hat 50 Ausmalbilder mit dicken Linien und großen Motiven. Jedes Bild steht allein auf einer Seite.",
                "Die zweite Ausgabe ist für Kinder von sechs bis zehn Jahren. Sie hat ebenfalls 50 Ausmalbilder.",
            ]),
            ("Freie Farbwahl bei Dinosauriern", [
                "Welche Farben viele Dinosaurier hatten, ist nicht bekannt. Deshalb sind bei den Ausmalbildern alle Farben erlaubt, vom klassischen Grün bis zum Regenbogen.",
                "Die großen Motive lassen Platz für Muster, Punkte und Streifen. Das macht die Bilder auch für Kinder spannend, die schon länger ausmalen.",
            ]),
            ("Dinosaurier als Rätsel", [
                "„Dinosaurier Labyrinthe“ ist für Kinder ab vier Jahren und enthält 60 Labyrinthe zum Ausdrucken. Mehr dazu auf der Seite [Labyrinthe für Kinder](@labyrinthe).",
                "„Dinosaurier Wortsuche“ ist für Kinder ab sechs Jahren. Das Buch enthält 80 Wortsuchrätsel in drei Stufen, mit Lösungen. Mehr dazu auf der Seite [Wortsuche für Kinder](@woerter).",
            ]),
            ("Zum Ausdrucken oder als Taschenbuch", [
                "Die PDF-Dateien kaufst du bei Etsy und lädst sie direkt nach dem Kauf herunter. Sie gibt es in A4 und US Letter, und jede Seite lässt sich einzeln ausdrucken. Verwenden darfst du sie privat und in der Schule.",
                "Das Malbuch-Paket für drei bis sechs Jahre enthält zehn Bände, darunter die Dinosaurier. Es kostet 19,99 €.",
                "Eine Übersicht über alle PDFs findest du unter [Ausmalbilder zum Ausdrucken](@ausdrucken).",
            ]),
        ],
        "books_h2": "Die Dinosaurier-Bücher",
        "bundles_h2": "Pakete mit Dinosaurier-Büchern",
        "faq_h2": "Fragen zu den Dinosaurier-Büchern",
        "faq": [
            ("Welches Dinosaurier-Buch passt zu meinem Kind?",
             "Für Kinder ab drei Jahren passt das Malbuch „Dinosaurier“ mit 50 Bildern. Für Kinder von sechs bis zehn Jahren gibt es die zweite Ausgabe, ebenfalls mit 50 Bildern."),
            ("Gibt es Dinosaurier-Ausmalbilder als PDF?",
             "Ja. Beide Malbücher gibt es als PDF bei Etsy, zum sofortigen Download."),
            ("Wie oft darf ich die Seiten ausdrucken?",
             "So oft du möchtest, für den privaten Gebrauch und die Schule. Die Dateien weiterzugeben oder zu verkaufen ist nicht erlaubt."),
        ],
    },
    "en": {
        "title": "Dinosaur Coloring Pages to Print | M. von Wedelstaedt",
        "desc": "Dinosaur coloring pages for kids: coloring books for ages three and six, mazes and word search. Paperback on Amazon or printable PDF on Etsy.",
        "h1": "Dinosaur coloring pages for kids",
        "eyebrow": "Dinosaurs",
        "lead": "The series has dinosaurs four times: as a coloring book for little kids, as a coloring book for kids ages six and up, as a maze book and as a word search. All four are available as PDFs on Etsy and as paperbacks on Amazon.",
        "sections": [
            ("Dinosaurs for two age groups", [
                "The coloring book “Dinosaurs” for kids ages three and up has 50 coloring pages with thick lines and big motifs. Each picture sits alone on its page.",
                "The second edition is for kids ages six to ten. It also has 50 coloring pages.",
            ]),
            ("Free choice of colors", [
                "For many dinosaurs, nobody knows what color they were. So all colors are allowed on the coloring pages, from classic green to rainbow.",
                "The big motifs leave room for patterns, dots and stripes. That keeps the pictures interesting for kids who have been coloring for a while.",
            ]),
            ("Dinosaurs as puzzles", [
                "“Dinosaur Mazes” is for kids ages four and up and has 60 mazes to print. Read more on the page [Mazes for kids](@labyrinthe).",
                "“Dinosaur Word Search” is for kids ages six and up. The book has 80 word search puzzles in three levels, with solutions. Read more on the page [Word search for kids](@woerter).",
            ]),
            ("To print or as a paperback", [
                "You buy the PDF files on Etsy and download them right after the purchase. They come in A4 and US Letter, and you can print each page on its own. You may use them privately and at school.",
                "The coloring bundle for ages three to six has ten books, including the dinosaurs. It costs €19.99.",
                "You can find an overview of all PDFs under [Printable coloring pages](@ausdrucken).",
            ]),
        ],
        "books_h2": "The dinosaur books",
        "bundles_h2": "Bundles with dinosaur books",
        "faq_h2": "Questions about the dinosaur books",
        "faq": [
            ("Which dinosaur book fits my child?",
             "For kids ages three and up, the coloring book “Dinosaurs” with 50 pictures fits. For kids ages six to ten there is the second edition, also with 50 pictures."),
            ("Are dinosaur coloring pages available as a PDF?",
             "Yes. Both coloring books are available as a PDF on Etsy, for instant download."),
            ("How often may I print the pages?",
             "As often as you like, for private use and school. You may not pass the files on or sell them."),
        ],
    },
}

# ---- Ausmalbilder zum Ausdrucken (Hub) ------------------------------------
PAGES["ausdrucken"] = {
    "og": "alles",
    "book_groups": [
        ("ausmal3", ["01-tierbabys", "02-tierfamilien", "03-bauernhof", "04-safari", "05-unterwasser",
                     "06-einhoerner", "07-dinosaurier", "08-fahrzeuge", "09-haustiere", "10-weihnachten",
                     "21-halloween", "22-thanksgiving", "23-nikolaus", "25-silvester", "05-unterwasser-deluxe"]),
        ("ausmal6", ["11-pferde", "12-mandalas", "13-wildtiere", "14-meer", "15-dinosaurier",
                     "16-weltraum", "17-drachen", "18-maschinen", "19-voegel", "20-ritter"]),
        ("labyrinth", ["30-labyrinth-dschungel", "31-labyrinth-dino", "32-labyrinth-weltraum",
                       "33-labyrinth-meer", "34-labyrinth-einhorn"]),
        ("wortsuche", ["40-wortsuche-dschungel", "41-wortsuche-dino", "42-wortsuche-weltraum",
                       "43-wortsuche-meer", "44-wortsuche-weihnachten"]),
    ],
    "bundles": ["staffel1", "staffel2", "jahreszeiten", "labyrinth", "wortsuche", "alles"],
    "related": ["weihnachten", "dinosaurier", "woerter", "labyrinthe", "pakete", "faq"],
    "de": {
        "title": "Ausmalbilder zum Ausdrucken für Kinder | M. von Wedelstaedt",
        "desc": "Ausmalbilder zum Ausdrucken für Kinder als PDF: Malbücher, Labyrinthe und Wortsuche in A4 und US Letter, Sofort-Download bei Etsy.",
        "h1": "Ausmalbilder zum Ausdrucken",
        "eyebrow": "PDF zum Ausdrucken",
        "lead": "Alle Bücher der Reihe gibt es als PDF zum Ausdrucken bei Etsy. Du lädst die Datei direkt nach dem Kauf herunter und druckst die Seiten zu Hause aus.",
        "sections": [
            ("So funktioniert der Download", [
                "Du suchst dir ein Buch oder ein Paket aus und kaufst es bei Etsy. Danach lädst du das PDF herunter und druckst die Seiten aus, die du brauchst. Jede Seite lässt sich einzeln drucken.",
                "Die Dateien gibt es in A4 und US Letter. Stelle im Druckdialog die tatsächliche Größe oder 100 Prozent ein, damit nichts verkleinert wird.",
            ]),
            ("Welches Buch passt zu welchem Alter", [
                "Die Malbücher für Kinder ab drei Jahren haben dicke Linien, große Motive und ein Bild pro Seite. Jedes Buch enthält 50 Ausmalbilder zu einem Thema, zum Beispiel Tierbabys, Bauernhof oder Fahrzeuge.",
                "Für Kinder von sechs bis zehn Jahren gibt es die zweite Reihe, etwa mit Pferden, Drachen, Weltraum oder Rittern.",
                "Die Labyrinthbücher mit je 60 Labyrinthen sind für Kinder ab vier Jahren. Die Wortsuche mit 80 Rätseln in drei Stufen ist für Kinder ab sechs Jahren.",
            ]),
            ("Tipps für den Druck", [
                "Für Buntstifte reicht normales Druckerpapier. Für Filzstifte oder Wasserfarben ist dickeres Papier besser, weil die Farbe sonst durchscheinen kann.",
                "Druck nur die Seiten aus, die ihr gerade ausmalen wollt. Das spart Papier und Tinte, und das Buch bleibt als Datei für später erhalten.",
            ]),
            ("Einzelne Bücher oder ein Paket", [
                "Ein einzelnes Malbuch kostet als PDF 4,99 €, ein Labyrinthbuch 5,99 € und ein Wortsuchbuch 6,99 €. Das Buch „Unterwasserwelt Deluxe“ mit 100 Ausmalbildern kostet 7,98 €.",
                "Wer mehrere Bücher möchte, spart mit einem Paket. Alle sechs Pakete findest du auf der Seite [Pakete](@pakete).",
                "Fünf Bonus-Ausmalbilder bekommst du gegen deine E-Mail-Adresse, siehe [Startseite](@home#bonus).",
            ]),
        ],
        "group_h2": {
            "ausmal3": "Ausmalbücher für Kinder ab drei Jahren",
            "ausmal6": "Ausmalbücher für Kinder von sechs bis zehn Jahren",
            "labyrinth": "Labyrinthe für Kinder ab vier Jahren",
            "wortsuche": "Wortsuche für Kinder ab sechs Jahren",
        },
        "bundles_h2": "Pakete zum Ausdrucken",
        "faq_h2": "Fragen zum Ausdrucken",
        "faq": [
            ("Welche Formate haben die PDFs?",
             "Die Seiten gibt es in A4 und in US Letter."),
            ("Kann ich ein PDF mehrmals ausdrucken?",
             "Ja, für den privaten Gebrauch und die Schule so oft, wie du möchtest."),
            ("Gibt es die Bücher auch gedruckt?",
             "Viele Titel gibt es als Taschenbuch bei Amazon. Welche, siehst du an den Links bei den einzelnen Büchern."),
            ("Welche Ausmalbilder passen zu Weihnachten?",
             "Weihnachtsmotive findest du auf der Seite [Ausmalbilder Weihnachten](@weihnachten)."),
        ],
    },
    "en": {
        "title": "Printable Coloring Pages for Kids | M. von Wedelstaedt",
        "desc": "Printable coloring pages for kids as PDF: coloring books, mazes and word search in A4 and US Letter, instant download on Etsy.",
        "h1": "Printable coloring pages",
        "eyebrow": "PDF to print",
        "lead": "Every book in the series is available as a printable PDF on Etsy. You download the file right after the purchase and print the pages at home.",
        "sections": [
            ("How the download works", [
                "You pick a book or a bundle and buy it on Etsy. Then you download the PDF and print the pages you need. You can print each page on its own.",
                "The files come in A4 and US Letter. In the print dialog, choose actual size or 100 percent so that nothing gets shrunk.",
            ]),
            ("Which book fits which age", [
                "The coloring books for kids ages three and up have thick lines, big motifs and one picture per page. Each book has 50 coloring pages on one topic, for example baby animals, farm or vehicles.",
                "For kids ages six to ten there is the second series, with horses, dragons, space or knights, among others.",
                "The maze books, with 60 mazes each, are for kids ages four and up. The word search, with 80 puzzles in three levels, is for kids ages six and up.",
            ]),
            ("Tips for printing", [
                "Regular printer paper is fine for colored pencils. For felt-tip pens or watercolors, thicker paper is better because the color can show through otherwise.",
                "Print only the pages you want to color right now. That saves paper and ink, and the book stays on your computer as a file for later.",
            ]),
            ("Single books or a bundle", [
                "A single coloring book costs €4.99 as a PDF, a maze book €5.99 and a word search book €6.99. The book “Under the Sea Deluxe” with 100 coloring pages costs €7.98.",
                "If you want several books, a bundle saves money. You can find all six bundles on the [Bundles](@pakete) page.",
                "You get five bonus coloring pages in exchange for your email address, see the [home page](@home#bonus).",
            ]),
        ],
        "group_h2": {
            "ausmal3": "Coloring books for kids ages three and up",
            "ausmal6": "Coloring books for kids ages six to ten",
            "labyrinth": "Mazes for kids ages four and up",
            "wortsuche": "Word search for kids ages six and up",
        },
        "bundles_h2": "Bundles to print",
        "faq_h2": "Questions about printing",
        "faq": [
            ("Which formats do the PDFs have?",
             "The pages come in A4 and in US Letter."),
            ("Can I print a PDF more than once?",
             "Yes, for private use and school, as often as you like."),
            ("Are the books also available in print?",
             "Many titles are available as paperbacks on Amazon. You can see which ones from the links on each book."),
            ("Which coloring pages fit Christmas?",
             "You can find Christmas motifs on the page [Christmas coloring pages](@weihnachten)."),
        ],
    },
}

# ---- Wortsuche ------------------------------------------------------------
PAGES["woerter"] = {
    "og": "wortsuche",
    "books": ["40-wortsuche-dschungel", "41-wortsuche-dino", "42-wortsuche-weltraum",
              "43-wortsuche-meer", "44-wortsuche-weihnachten"],
    "bundles": ["wortsuche", "alles"],
    "related": ["labyrinthe", "dinosaurier", "ausdrucken", "faq"],
    "de": {
        "title": "Wortsuche für Kinder zum Ausdrucken | M. von Wedelstaedt",
        "desc": "Wortsuche für Kinder ab sechs Jahren: 80 Rätsel in drei Stufen mit Lösungen, als PDF zum Ausdrucken bei Etsy, zwei Titel auch als Taschenbuch.",
        "h1": "Wortsuche für Kinder",
        "eyebrow": "Rätselbücher",
        "lead": "Die Wortsuchbücher der Reihe haben je 80 Rätsel in drei Stufen, mit Lösungen. Sie sind für Kinder ab sechs Jahren gedacht und kommen als PDF zum Ausdrucken bei Etsy, zwei Titel auch als Taschenbuch bei Amazon.",
        "sections": [
            ("Fünf Themen, je 80 Rätsel", [
                "Es gibt fünf Wortsuchbücher: Dschungel, Dinosaurier, Weltraum, Meer und Weihnachten. Jedes Buch hat ein eigenes Thema.",
                "Jedes Buch enthält 80 Rätsel in drei Stufen. Zu allen Rätseln gibt es Lösungen, sodass du nachsehen kannst, wenn sich ein Wort gut versteckt.",
            ]),
            ("Für Kinder ab sechs Jahren", [
                "Wortsuche braucht Lesen und genaues Hinsehen, deshalb sind die Bücher für Kinder ab sechs Jahren gedacht. Die drei Stufen helfen dir bei der Wahl des passenden Rätsels.",
                "Du entscheidest je nach Kind, mit welcher Stufe ihr beginnt. Ein Rätsel lässt sich auch gemeinsam lösen, wenn ein Kind Hilfe beim Suchen möchte.",
            ]),
            ("Wortsuche zu Hause und in der Schule", [
                "Mit einem Marker oder Buntstift lässt sich jedes gefundene Wort markieren. Wer ein Rätsel noch einmal lösen möchte, druckt die Seite einfach neu aus.",
                "Lehrkräfte dürfen einzelne Seiten für die Klasse ausdrucken. Die Dateien weiterzugeben oder zu verkaufen ist nicht erlaubt.",
                "Das passt gut für Wartezeiten, Regentage oder die Reise, weil du nur Papier und einen Stift brauchst.",
            ]),
            ("Als PDF oder Taschenbuch", [
                "Alle fünf Bücher gibt es als PDF bei Etsy, einzeln für 6,99 €. Das PDF lädst du direkt nach dem Kauf herunter, in A4 oder US Letter, und druckst jede Seite einzeln aus.",
                "„Dinosaurier Wortsuche“ und „Weihnachtsrätsel Wortsuche“ gibt es auch als Taschenbuch bei Amazon.",
                "Das Wortsuche-Paket enthält alle fünf Themen mit 400 Rätseln und kostet 24,99 €. Im Alles-Paket stecken zusätzlich Malbücher und Labyrinthe.",
            ]),
        ],
        "books_h2": "Die Wortsuchbücher",
        "bundles_h2": "Pakete mit Wortsuche",
        "faq_h2": "Fragen zur Wortsuche",
        "faq": [
            ("Ab welchem Alter ist die Wortsuche geeignet?",
             "Ab sechs Jahren. Die Kinder sollten schon lesen können."),
            ("Gibt es Lösungen?",
             "Ja, zu den Rätseln gibt es Lösungen."),
            ("Wie viele Rätsel hat ein Buch?",
             "Jedes Wortsuchbuch hat 80 Rätsel in drei Stufen."),
            ("Darf ich die Rätsel in der Klasse ausdrucken?",
             "Ja, die Verwendung in der Schule ist erlaubt. Weitergeben oder verkaufen darfst du die Dateien nicht."),
        ],
    },
    "en": {
        "title": "Word Search for Kids to Print | M. von Wedelstaedt",
        "desc": "Word search for kids ages six and up: 80 puzzles in three levels with solutions, as printable PDF on Etsy, two titles also as paperback.",
        "h1": "Word search for kids",
        "eyebrow": "Puzzle books",
        "lead": "The word search books in the series have 80 puzzles each, in three levels, with solutions. They are made for kids ages six and up and come as printable PDFs on Etsy, two titles also as paperbacks on Amazon.",
        "sections": [
            ("Five topics, 80 puzzles each", [
                "There are five word search books: Jungle, Dinosaur, Space, Ocean and Christmas. Each book has its own topic.",
                "Each book has 80 puzzles in three levels. Solutions are included for all puzzles, so you can look up a word that hides well.",
            ]),
            ("For kids ages six and up", [
                "Word search takes reading and a close look, which is why the books are made for kids ages six and up. The three levels help you choose a fitting puzzle.",
                "You decide, depending on your child, which level to start with. You can also solve a puzzle together if a child wants help searching.",
            ]),
            ("Word search at home and at school", [
                "You can mark each word you find with a marker or colored pencil. If you want to solve a puzzle again, just print the page anew.",
                "Teachers may print single pages for their class. You may not pass the files on or sell them.",
                "It works well for waiting rooms, rainy days or travel, because all you need is paper and a pen.",
            ]),
            ("As a PDF or a paperback", [
                "All five books are available as a PDF on Etsy, €6.99 each. You download the PDF right after the purchase, in A4 or US Letter, and print each page on its own.",
                "“Dinosaur Word Search” and “Christmas Word Search” are also available as paperbacks on Amazon.",
                "The word search bundle holds all five topics with 400 puzzles and costs €24.99. The complete bundle adds coloring books and mazes.",
            ]),
        ],
        "books_h2": "The word search books",
        "bundles_h2": "Bundles with word search",
        "faq_h2": "Questions about word search",
        "faq": [
            ("What age is word search suitable for?",
             "Ages six and up. Kids should already be able to read."),
            ("Are solutions included?",
             "Yes, solutions are included for the puzzles."),
            ("How many puzzles does a book have?",
             "Each word search book has 80 puzzles in three levels."),
            ("May I print the puzzles for my class?",
             "Yes, use at school is allowed. You may not pass the files on or sell them."),
        ],
    },
}

# ---- Labyrinthe -----------------------------------------------------------
PAGES["labyrinthe"] = {
    "og": "labyrinth",
    "books": ["30-labyrinth-dschungel", "31-labyrinth-dino", "32-labyrinth-weltraum",
              "33-labyrinth-meer", "34-labyrinth-einhorn"],
    "bundles": ["labyrinth", "alles"],
    "related": ["woerter", "dinosaurier", "ausdrucken", "faq"],
    "de": {
        "title": "Labyrinthe für Kinder zum Ausdrucken | M. von Wedelstaedt",
        "desc": "Labyrinthe für Kinder ab vier Jahren: 60 Labyrinthe pro Buch, fünf Themen, als PDF bei Etsy, das Dinosaurier-Buch auch bei Amazon.",
        "h1": "Labyrinthe für Kinder",
        "eyebrow": "Rätselbücher",
        "lead": "Jedes Labyrinthbuch der Reihe enthält 60 Labyrinthe und ist für Kinder ab vier Jahren gedacht. Du bekommst die Bücher als PDF zum Ausdrucken bei Etsy, das Dinosaurier-Labyrinthbuch auch als Taschenbuch bei Amazon.",
        "sections": [
            ("Fünf Themen, je 60 Labyrinthe", [
                "Es gibt Labyrinthbücher zu fünf Themen: Dschungel, Dinosaurier, Weltraum, Meer und Einhorn. Jedes Buch hat 60 Labyrinthe.",
                "Zusammen sind das 300 Labyrinthe, die du im Labyrinth-Paket für 19,99 € bekommst.",
            ]),
            ("Labyrinthe ausdrucken", [
                "Das PDF kaufst du bei Etsy und lädst es direkt nach dem Kauf herunter. Es gibt die Seiten in A4 und US Letter, und jede Seite lässt sich einzeln ausdrucken. Ein einzelnes Labyrinthbuch kostet 5,99 €.",
                "Wenn ein Kind ein Labyrinth falsch begonnen hat, druckst du die Seite einfach noch einmal aus.",
                "Auch in der Schule dürfen Lehrkräfte einzelne Seiten für die Klasse ausdrucken. Die Dateien weiterzugeben oder zu verkaufen ist nicht erlaubt.",
            ]),
            ("Tipps zum Lösen", [
                "Viele Kinder fahren zuerst mit dem Finger über den Weg. Danach hilft ein Bleistift, den man radieren kann, oder ein dicker Stift für Kinder, die sich sicher fühlen.",
                "Bei einer Sackgasse lohnt es sich, vom Ziel aus rückwärts zu suchen. Das Kind merkt dabei oft schneller, welcher Abzweig nicht weiterführt.",
                "Mehrere Labyrinthe hintereinander ergeben eine kleine Rätselrunde für Autofahrten oder Wartezeiten. Dafür druckst du einfach ein paar Seiten aus und steckst sie in eine Mappe.",
            ]),
            ("Labyrinthe und Ausmalbilder verbinden", [
                "Bei den Ausmalbüchern findest du dieselben Themen, zum Beispiel [Dinosaurier](@dinosaurier). Das Alles-Paket enthält 35 Bücher: 25 Malbücher und zehn Rätselbücher.",
                "Die Labyrinthe sind für Kinder ab vier Jahren, die Wortsuche für Kinder ab sechs. Mehr dazu auf der Seite [Wortsuche für Kinder](@woerter).",
            ]),
        ],
        "books_h2": "Die Labyrinthbücher",
        "bundles_h2": "Pakete mit Labyrinthen",
        "faq_h2": "Fragen zu den Labyrinthen",
        "faq": [
            ("Ab welchem Alter eignen sich die Labyrinthe?",
             "Ab vier Jahren."),
            ("Wie viele Labyrinthe sind in einem Buch?",
             "Jedes Labyrinthbuch hat 60 Labyrinthe zu einem Thema."),
            ("Gibt es die Labyrinthe auch als Taschenbuch?",
             "Das Dinosaurier-Labyrinthbuch gibt es als Taschenbuch bei Amazon. Die anderen vier Labyrinthbücher gibt es bisher als PDF bei Etsy."),
            ("Darf ich die Labyrinthe in der Schule ausdrucken?",
             "Ja, für den privaten Gebrauch und in der Schule. Weitergeben oder verkaufen darfst du die Dateien nicht."),
        ],
    },
    "en": {
        "title": "Mazes for Kids to Print | M. von Wedelstaedt",
        "desc": "Mazes for kids ages four and up: 60 mazes per book, five topics, as printable PDF on Etsy, the dinosaur book also on Amazon.",
        "h1": "Mazes for kids",
        "eyebrow": "Puzzle books",
        "lead": "Each maze book in the series has 60 mazes and is made for kids ages four and up. You get the books as printable PDFs on Etsy, and the dinosaur maze book also as a paperback on Amazon.",
        "sections": [
            ("Five topics, 60 mazes each", [
                "There are maze books on five topics: Jungle, Dinosaur, Space, Ocean and Unicorn. Each book has 60 mazes.",
                "Together that makes 300 mazes, which you get in the maze bundle for €19.99.",
            ]),
            ("Printing the mazes", [
                "You buy the PDF on Etsy and download it right after the purchase. The pages come in A4 and US Letter, and you can print each page on its own. A single maze book costs €5.99.",
                "If a child started a maze the wrong way, just print the page again.",
                "Teachers may also print single pages for their class at school. You may not pass the files on or sell them.",
            ]),
            ("Tips for solving", [
                "Many kids first trace the path with a finger. After that, a pencil that can be erased helps, or a thick pen for kids who feel sure.",
                "At a dead end, it pays to search backwards from the goal. The child often notices faster which turn does not lead anywhere.",
                "Several mazes in a row make a small puzzle round for car rides or waiting rooms. Just print a few pages and put them in a folder.",
            ]),
            ("Combining mazes and coloring pages", [
                "The coloring books have the same topics, for example [dinosaurs](@dinosaurier). The complete bundle has 35 books: 25 coloring books and ten puzzle books.",
                "The mazes are for kids ages four and up, the word search for kids ages six and up. Read more on the page [Word search for kids](@woerter).",
            ]),
        ],
        "books_h2": "The maze books",
        "bundles_h2": "Bundles with mazes",
        "faq_h2": "Questions about the mazes",
        "faq": [
            ("What age are the mazes suitable for?",
             "Ages four and up."),
            ("How many mazes are in a book?",
             "Each maze book has 60 mazes on one topic."),
            ("Are the mazes also available as a paperback?",
             "The dinosaur maze book is available as a paperback on Amazon. The other four maze books are available as PDFs on Etsy for now."),
            ("May I print the mazes at school?",
             "Yes, for private use and at school. You may not pass the files on or sell them."),
        ],
    },
}

# ---- Pakete ---------------------------------------------------------------
PAGES["pakete"] = {
    "og": "alles",
    "bundles": ["staffel1", "staffel2", "jahreszeiten", "labyrinth", "wortsuche", "alles"],
    "related": ["ausdrucken", "weihnachten", "labyrinthe", "woerter"],
    "de": {
        "title": "Malbuch-Pakete und Rätsel-Pakete | M. von Wedelstaedt",
        "desc": "Sechs Pakete zum Ausdrucken bei Etsy: Malbücher für drei bis zehn Jahre, Labyrinthe, Wortsuche und das Alles-Paket mit 35 Büchern als PDF.",
        "h1": "Pakete zum Ausdrucken",
        "eyebrow": "PDF-Pakete",
        "lead": "Sechs Pakete bündeln mehrere Bücher der Reihe als PDF. Du kaufst sie bei Etsy, lädst sie direkt herunter und druckst die Seiten in A4 oder US Letter aus.",
        "sections": [
            ("Welches Paket passt zu wem", [
                "Das Malbuch-Paket für drei bis sechs Jahre enthält zehn Bände mit Tieren, Meer, Dinosauriern und Fahrzeugen. Für Kinder von sechs bis zehn Jahren gibt es das zweite Malbuch-Paket mit zehn Bänden zu Pferden, Mandalas, Drachen, Weltraum und Rittern.",
                "Das Jahreszeiten-Paket hat fünf Malbücher zu Halloween, Erntedank, Nikolaus, Weihnachten und Silvester. Das Labyrinth-Paket enthält 300 Labyrinthe zu fünf Themen, das Wortsuche-Paket 400 Wortsuchrätsel zu fünf Themen.",
            ]),
            ("Das Alles-Paket", [
                "Das Alles-Paket enthält 25 Malbücher und zehn Rätselbücher, zusammen 35 Bücher. Bei Etsy gibt es dafür zwei Angebote, eines in A4 und eines in US Letter.",
                "Die Pakete sind günstiger als der Einzelkauf der Bücher im Shop. Wie viel du sparst, steht bei jedem Paket.",
            ]),
            ("Eine Frage der Altersstufe", [
                "Die Pakete für Ausmalbücher sind nach Alter getrennt: drei bis sechs Jahre und sechs bis zehn Jahre. So passen die Bücher zu dem, was dein Kind schon ausmalen mag.",
                "Wenn Geschwister verschiedenen Alters mitmachen, ist das Alles-Paket die einfachste Wahl. Es enthält Bücher für beide Altersgruppen sowie Labyrinthe und Wortsuche.",
            ]),
            ("Wie der Download funktioniert", [
                "Nach dem Kauf bei Etsy lädst du die Datei herunter. Du druckst die Seiten so oft aus, wie du möchtest, für den privaten Gebrauch und die Schule. Die Dateien weiterzugeben oder zu verkaufen ist nicht erlaubt.",
                "Fünf Bonus-Ausmalbilder zum Ausprobieren bekommst du gegen deine E-Mail-Adresse, siehe [Startseite](@home#bonus).",
            ]),
        ],
        "bundles_h2": "Alle sechs Pakete",
        "faq_h2": "Fragen zu den Paketen",
        "faq": [
            ("Was ist in einem Paket enthalten?",
             "Die Bücher des Pakets als PDF in A4 und US Letter. Beim Alles-Paket wählst du bei Etsy zwischen zwei Angeboten, A4 oder US Letter."),
            ("Gibt es die Pakete gedruckt?",
             "Nein, die Pakete gibt es nur als PDF bei Etsy. Viele Einzelbücher gibt es als Taschenbuch bei Amazon."),
            ("Wie hoch ist die Ersparnis?",
             "Sie hängt vom Paket ab und steht bei jedem Paket auf dieser Seite. Verglichen wird mit dem Einzelkauf der Bücher im Shop."),
            ("Kann ich ein Paket in der Schule verwenden?",
             "Ja, für den privaten Gebrauch und in der Schule. Weitergeben oder verkaufen darfst du die Dateien nicht."),
        ],
    },
    "en": {
        "title": "Printable Coloring and Puzzle Bundles | M. von Wedelstaedt",
        "desc": "Six printable bundles on Etsy: coloring books for ages three to ten, mazes, word search and the complete bundle with 35 books as PDF.",
        "h1": "Printable bundles",
        "eyebrow": "PDF bundles",
        "lead": "Six bundles combine several books of the series as a PDF. You buy them on Etsy, download them right away and print the pages in A4 or US Letter.",
        "sections": [
            ("Which bundle fits whom", [
                "The coloring bundle for ages three to six has ten books with animals, ocean, dinosaurs and vehicles. For kids ages six to ten there is the second coloring bundle with ten books on horses, mandalas, dragons, space and knights.",
                "The seasonal bundle has five coloring books on Halloween, Thanksgiving, St. Nicholas, Christmas and New Year. The maze bundle holds 300 mazes on five topics, the word search bundle 400 puzzles on five topics.",
            ]),
            ("The complete bundle", [
                "The complete bundle holds 25 coloring books and ten puzzle books, 35 books in total. On Etsy there are two listings for it, one in A4 and one in US Letter.",
                "The bundles cost less than buying the books one by one in the shop. How much you save is shown on each bundle.",
            ]),
            ("A question of age", [
                "The coloring bundles are split by age: three to six years and six to ten years. That way the books fit what your child already likes to color.",
                "If siblings of different ages join in, the complete bundle is the simplest choice. It holds books for both age groups plus mazes and word search.",
            ]),
            ("How the download works", [
                "After the purchase on Etsy you download the file. You print the pages as often as you like, for private use and school. You may not pass the files on or sell them.",
                "You get five bonus coloring pages in exchange for your email address, see the [home page](@home#bonus).",
            ]),
        ],
        "bundles_h2": "All six bundles",
        "faq_h2": "Questions about the bundles",
        "faq": [
            ("What is in a bundle?",
             "The books of the bundle as a PDF in A4 and US Letter. For the complete bundle, you choose between two listings on Etsy, A4 or US Letter."),
            ("Are the bundles available in print?",
             "No, the bundles are only available as PDFs on Etsy. Many single books are available as paperbacks on Amazon."),
            ("How much do I save?",
             "It depends on the bundle and is shown on each bundle on this page. The comparison is with buying the books one by one in the shop."),
            ("Can I use a bundle at school?",
             "Yes, for private use and at school. You may not pass the files on or sell them."),
        ],
    },
}

# ---- FAQ ------------------------------------------------------------------
PAGES["faq"] = {
    "og": None,
    "related": ["ausdrucken", "pakete", "woerter", "labyrinthe"],
    "de": {
        "title": "Häufige Fragen zu Büchern und PDFs | M. von Wedelstaedt",
        "desc": "Antworten zu Altersempfehlung, Druck in A4 und US Letter, Etsy-Download, Taschenbuch und PDF, Rechten, Wortsuche und Labyrinthen.",
        "h1": "Häufige Fragen",
        "eyebrow": "Fragen und Antworten",
        "lead": "Hier stehen Antworten auf Fragen zu den Büchern und PDFs der Reihe.",
        "sections": [],
        "faq_groups": [
            ("Alter und Inhalt", [
                ("Für welches Alter sind die Bücher gedacht?",
                 "Die Ausmalbücher gibt es für Kinder ab drei Jahren und für Kinder von sechs bis zehn Jahren. Die Labyrinthbücher sind für Kinder ab vier Jahren, die Wortsuche für Kinder ab sechs Jahren."),
                ("Wie sind die Ausmalbilder gestaltet?",
                 "Die Bücher haben dicke Linien, große Motive und ein Bild pro Seite. Jedes Ausmalbuch enthält 50 Motive, das Buch „Unterwasserwelt Deluxe“ enthält 100."),
                ("Wie funktionieren die Wortsuche-Rätsel?",
                 "Jedes Wortsuchbuch enthält 80 Rätsel in drei Stufen, mit Lösungen. Die Bücher sind für Kinder ab sechs Jahren gedacht."),
                ("Was enthalten die Labyrinthbücher?",
                 "Jedes Buch hat 60 Labyrinthe zu einem Thema, für Kinder ab vier Jahren. Es gibt fünf Themen: Dschungel, Dinosaurier, Weltraum, Meer und Einhorn."),
            ]),
            ("PDF und Druck", [
                ("Wie funktioniert der Download bei Etsy?",
                 "Du kaufst das PDF bei Etsy und lädst die Datei direkt nach dem Kauf herunter. Es wird nichts verschickt, du musst also nicht warten."),
                ("Gibt es die PDFs in A4 und US Letter?",
                 "Ja, die Seiten gibt es in beiden Formaten. Wähle im Druckdialog die tatsächliche Größe oder 100 Prozent, damit nichts verkleinert wird."),
                ("Wie oft darf ich ein PDF ausdrucken?",
                 "So oft du möchtest, solange du die Seiten privat oder in der Schule verwendest. Jede Seite lässt sich einzeln ausdrucken."),
                ("Was kostet ein PDF?",
                 "Ein Malbuch kostet als PDF 4,99 €, ein Labyrinthbuch 5,99 € und ein Wortsuchbuch 6,99 €. „Unterwasserwelt Deluxe“ kostet 7,98 €, die Pakete findest du auf der Seite [Pakete](@pakete)."),
            ]),
            ("Taschenbuch und PDF", [
                ("Was ist der Unterschied zwischen Taschenbuch und PDF?",
                 "Das Taschenbuch ist ein gedrucktes Buch, das du bei Amazon bestellst. Das PDF ist eine Datei, die du bei Etsy kaufst und selbst ausdruckst. Einige Titel gibt es nur als PDF."),
            ]),
            ("Rechte und Verwendung", [
                ("Darf ich die Bilder privat und in der Schule verwenden?",
                 "Ja, du darfst die Seiten für den privaten Gebrauch und in der Schule ausdrucken und verwenden. Weitergeben oder verkaufen darfst du die Dateien nicht."),
                ("Wer hat die Bücher gestaltet, und wurde KI eingesetzt?",
                 "Die Bücher werden von M. von Wedelstaedt gestaltet und entwickelt, mit Unterstützung von KI."),
            ]),
            ("Bonus-Bilder und Kontakt", [
                ("Was sind die Bonus-Bilder?",
                 "Du bekommst fünf Bonus-Ausmalbilder als PDF, wenn du dich auf der [Startseite](@home#bonus) mit deiner E-Mail-Adresse anmeldest. Dazu wählst du eines von drei Themen und bestätigst die Anmeldung per E-Mail. Danach bekommst du gelegentlich Neuigkeiten, und du kannst dich jederzeit abmelden."),
                ("Was gilt bei Rückgabe oder Problemen mit einer Datei?",
                 "Für Käufe bei Amazon und Etsy gelten die Regeln der jeweiligen Plattform. Wenn eine Datei nicht funktioniert, schreib an [hello@mvonwedelstaedt.com](mailto:hello@mvonwedelstaedt.com)."),
            ]),
        ],
    },
    "en": {
        "title": "FAQ: Books and Printable PDFs | M. von Wedelstaedt",
        "desc": "Answers on age recommendations, printing in A4 and US Letter, the Etsy download, paperback and PDF, usage rights, word search and mazes.",
        "h1": "Frequently asked questions",
        "eyebrow": "Questions and answers",
        "lead": "Here are answers to questions about the books and PDFs of the series.",
        "sections": [],
        "faq_groups": [
            ("Age and content", [
                ("What age are the books made for?",
                 "The coloring books are available for kids ages three and up and for kids ages six to ten. The maze books are for kids ages four and up, the word search for kids ages six and up."),
                ("How are the coloring pages designed?",
                 "The books have thick lines, big motifs and one picture per page. Each coloring book has 50 motifs, and the book “Under the Sea Deluxe” has 100."),
                ("How do the word search puzzles work?",
                 "Each word search book has 80 puzzles in three levels, with solutions. The books are made for kids ages six and up."),
                ("What is in the maze books?",
                 "Each book has 60 mazes on one topic, for kids ages four and up. There are five topics: Jungle, Dinosaur, Space, Ocean and Unicorn."),
            ]),
            ("PDF and printing", [
                ("How does the download on Etsy work?",
                 "You buy the PDF on Etsy and download the file right after the purchase. Nothing is shipped, so you do not have to wait."),
                ("Are the PDFs available in A4 and US Letter?",
                 "Yes, the pages come in both formats. In the print dialog, choose actual size or 100 percent so that nothing gets shrunk."),
                ("How often may I print a PDF?",
                 "As often as you like, as long as you use the pages privately or at school. You can print each page on its own."),
                ("How much does a PDF cost?",
                 "A coloring book costs €4.99 as a PDF, a maze book €5.99 and a word search book €6.99. “Under the Sea Deluxe” costs €7.98, and you can find the bundles on the [Bundles](@pakete) page."),
            ]),
            ("Paperback and PDF", [
                ("What is the difference between a paperback and a PDF?",
                 "The paperback is a printed book that you order on Amazon. The PDF is a file that you buy on Etsy and print yourself. Some titles are only available as a PDF."),
            ]),
            ("Rights and use", [
                ("May I use the pictures privately and at school?",
                 "Yes, you may print and use the pages for private use and at school. You may not pass the files on or sell them."),
                ("Who designed the books, and was AI used?",
                 "The books are designed and developed by M. von Wedelstaedt, with the help of AI."),
            ]),
            ("Bonus pages and contact", [
                ("What are the bonus pages?",
                 "You get five bonus coloring pages as a PDF when you sign up on the [home page](@home#bonus) with your email address. You choose one of three themes and confirm the sign-up by email. After that you get occasional news, and you can unsubscribe at any time."),
                ("What applies to returns or problems with a file?",
                 "Purchases on Amazon and Etsy follow the rules of the respective platform. If a file does not work, write to [hello@mvonwedelstaedt.com](mailto:hello@mvonwedelstaedt.com)."),
            ]),
        ],
    },
}

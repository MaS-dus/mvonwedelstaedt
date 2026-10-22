// Startseite (DE und EN): Altersfilter, Detaildialog und Bonus-Anmeldung.
// Das Buchraster steht als normales HTML in der Seite; dieses Skript ergaenzt nur Bedienung.
(function () {
  const sprache = document.documentElement.lang === "en" ? "en" : "de";
  const TEXTE = {
    de: {
      filterLabel: "Nach Alter filtern",
      filterAlle: "Alle",
      filter36: "3 bis 6 Jahre",
      filter610: "6 bis 10 Jahre",
      filterCount: (n) => (n === 1 ? "1 Buch" : n + " Bücher"),
      detailBonus: "Fünf Bonus-Bilder gratis holen",
      detailClose: "Schließen",
      shopButton: () => "Auf Amazon ansehen",
      etsyButton: "Als PDF zum Ausdrucken auf Etsy",
      otherShops: "",
      bonusSending: "Sende...",
      bonusOk: "Fast geschafft! Wir haben dir eine E-Mail geschickt. Klicke darin auf den Bestätigungslink (schau auch im Spam-Ordner nach), dann bekommst du sofort deine Bonus-Bilder.",
      bonusErr: "Da ist etwas schiefgelaufen. Bitte später nochmal versuchen.",
    },
    en: {
      filterLabel: "Filter by age",
      filterAlle: "All",
      filter36: "Ages 3 to 6",
      filter610: "Ages 6 to 10",
      filterCount: (n) => (n === 1 ? "1 book" : n + " books"),
      detailBonus: "Get five free bonus pages",
      detailClose: "Close",
      shopButton: (dom) => "View on amazon." + dom,
      etsyButton: "Printable PDF on Etsy",
      otherShops: "Other Amazon stores:",
      bonusSending: "Sending…",
      bonusOk: "Almost done! We just sent you an email. Click the confirmation link in it (check your spam folder too) and your bonus pages will follow right away.",
      bonusErr: "Something went wrong. Please try again later.",
    },
  };
  const t = TEXTE[sprache];
  const amazonShop = window.mvwAmazonShop || (() => (sprache === "de" ? "de" : "com"));

  const grid = document.getElementById("grid");
  const detail = document.getElementById("detail");
  const filterBar = document.getElementById("filter");
  const zaehler = document.getElementById("filter-count");

  // ---------- Altersfilter ----------
  filterBar.setAttribute("aria-label", t.filterLabel);
  for (const [wert, text] of [["alle", t.filterAlle], ["3-6", t.filter36], ["6-10", t.filter610]]) {
    const chip = document.createElement("button");
    chip.type = "button";
    chip.className = "chip";
    chip.dataset.alter = wert;
    chip.textContent = text;
    filterBar.insertBefore(chip, zaehler);
  }
  function filterAnwenden(wert) {
    let n = 0;
    for (const kachel of grid.children) {
      const zeigen = wert === "alle" || kachel.dataset.alter === wert;
      kachel.hidden = !zeigen;
      if (zeigen) n++;
    }
    for (const chip of filterBar.querySelectorAll(".chip")) {
      chip.setAttribute("aria-pressed", String(chip.dataset.alter === wert));
    }
    zaehler.textContent = t.filterCount(n);
  }
  filterBar.addEventListener("click", (e) => {
    const chip = e.target.closest(".chip");
    if (chip) filterAnwenden(chip.dataset.alter);
  });
  filterAnwenden("alle");

  // ---------- Detailansicht (Link auf ein einzelnes Buch: /#<buch-id>) ----------
  function kachelFuer(id) {
    return grid.querySelector('.tile[data-id="' + id.replace(/"/g, "") + '"]');
  }
  function detailOeffnen(id) {
    const kachel = kachelFuer(id);
    if (!kachel) return;
    const d = kachel.dataset;
    const coverImg = kachel.querySelector(".tile-img");
    const titelText = kachel.querySelector(".tile-title").textContent;
    const detailImg = document.getElementById("detail-img");
    detailImg.src = coverImg.getAttribute("src");
    detailImg.alt = `${titelText} — Cover`;
    const titel = document.getElementById("detail-title");
    titel.textContent = titelText;
    titel.style.color = d.farbe;
    document.getElementById("detail-sub").textContent = kachel.querySelector(".tile-sub").textContent;
    const shop = amazonShop();
    const amazon = document.getElementById("detail-amazon");
    amazon.hidden = !d.asin;
    if (d.asin) {
      amazon.href = `https://www.amazon.${shop}/dp/${d.asin}`;
      amazon.textContent = `${t.shopButton(shop)} →`;
    }
    const etsy = document.getElementById("detail-etsy");
    etsy.hidden = !d.etsy;
    if (d.etsy) {
      etsy.href = `https://www.etsy.com/listing/${d.etsy}`;
      etsy.textContent = `${t.etsyButton} →`;
    }
    const shops = document.getElementById("detail-shops");
    shops.replaceChildren();
    if (sprache === "en" && d.asin) {
      shops.append(t.otherShops + " ");
      for (const dom of ["com", "co.uk", "ca", "com.au", "ie"]) {
        if (dom === shop) continue;
        const a = document.createElement("a");
        a.href = `https://www.amazon.${dom}/dp/${d.asin}`;
        a.target = "_blank";
        a.rel = "noopener";
        a.textContent = `amazon.${dom}`;
        shops.append(a, " ");
      }
      shops.hidden = false;
    } else {
      shops.hidden = true;
    }
    const bonusLink = document.getElementById("detail-bonus");
    bonusLink.textContent = t.detailBonus;
    bonusLink.hidden = Boolean(d.typ); // der Gratis-Bonus der Startseite sind Ausmalbilder
    document.getElementById("detail-close").setAttribute("aria-label", t.detailClose);
    if (!detail.open) detail.showModal();
    history.replaceState(null, "", `${location.pathname}${location.search}#${d.id}`);
  }
  grid.addEventListener("click", (e) => {
    const link = e.target.closest(".tile-open");
    if (!link) return;
    e.preventDefault();
    detailOeffnen(link.closest(".tile").dataset.id);
  });
  detail.addEventListener("close", () => {
    history.replaceState(null, "", location.pathname + location.search);
  });
  detail.addEventListener("click", (e) => { if (e.target === detail) detail.close(); }); // Klick auf den Hintergrund
  document.getElementById("detail-close").addEventListener("click", () => detail.close());
  document.getElementById("detail-bonus").addEventListener("click", () => detail.close());
  if (location.hash.length > 1) detailOeffnen(decodeURIComponent(location.hash.slice(1)));

  // ---------- Bonus-Anmeldung (gleicher Webhook wie die QR-Seite /malbuch) ----------
  // buchId muss ein Schluessel aus der BONUS-MAP im n8n-Knoten "Vorbereiten" sein.
  const WEBHOOK_URL = "https://n8n.srv1082810.hstgr.cloud/webhook/kinderbuecher-bonus-subscribe";
  const BONUS_THEMEN = [
    { id: "07-dinosaurier", name: { de: "Dinosaurier", en: "Dinosaurs" },
      titel: { de: "Dinosaurier", en: "Dinosaurs" } },
    { id: "05-unterwasser", name: { de: "Unter Wasser", en: "Under the Sea" },
      titel: { de: "Unterwasserwelt", en: "Under the Sea" } },
    { id: "03-bauernhof", name: { de: "Bauernhof", en: "On the Farm" },
      titel: { de: "Mein Bauernhof-Malbuch", en: "My Farm Coloring Book" } },
  ];

  const bonusForm = document.getElementById("bonus-form");
  const bonusMsg = document.getElementById("bonus-message");
  bonusForm.addEventListener("submit", async (e) => {
    e.preventDefault();
    const data = new FormData(bonusForm);
    if (data.get("website")) return; // Honeypot
    const thema = BONUS_THEMEN.find((x) => x.id === data.get("thema")) || BONUS_THEMEN[0];
    const payload = {
      email: data.get("email"),
      buchId: thema.id,
      sprache: sprache,
      buchTitel: thema.titel[sprache],
      source: `Startseite - ${thema.id}-${sprache}`,
    };
    const btn = document.getElementById("bonus-btn");
    const orig = btn.textContent;
    btn.disabled = true;
    btn.textContent = t.bonusSending;
    bonusMsg.hidden = true;
    try {
      const res = await fetch(WEBHOOK_URL, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(payload),
      });
      if (!res.ok) throw new Error("Fehler");
      bonusMsg.textContent = t.bonusOk;
      bonusMsg.className = "bonus-message success";
      bonusMsg.hidden = false;
      bonusForm.reset();
      btn.textContent = orig;
      btn.disabled = false;
    } catch (err) {
      bonusMsg.textContent = t.bonusErr;
      bonusMsg.className = "bonus-message error";
      bonusMsg.hidden = false;
      btn.textContent = orig;
      btn.disabled = false;
    }
  });
})();

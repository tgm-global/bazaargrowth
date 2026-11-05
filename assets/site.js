/* Bazar Growth: site behaviour. Reads everything from window.SITE_CONFIG (config.js). */
(function () {
  "use strict";
  var C = window.SITE_CONFIG || {};
  var digits = function (v) { return String(v || "").replace(/\D/g, ""); };
  var phone = digits(C.phone), wa = digits(C.whatsapp), cc = digits(C.countryCode) || "91";
  var fmt = function (n) { return n.length === 10 ? "+" + cc + " " + n.slice(0, 5) + " " + n.slice(5) : n; };
  var q = function (s, r) { return Array.prototype.slice.call((r || document).querySelectorAll(s)); };

  var showPhone = C.showPhoneAndWhatsapp !== false && (phone || wa);
  var showForm = C.showEmailFormAndTestimonials !== false;

  /* brand, tagline, year */
  q('[data-cfg="brand"]').forEach(function (el) { el.textContent = C.brandName || "Bazar Growth"; });
  q('[data-cfg="tagline"]').forEach(function (el) { el.textContent = C.tagline || ""; });
  q('[data-cfg="year"]').forEach(function (el) { el.textContent = new Date().getFullYear(); });

  /* apply brand name everywhere: visible text, title, meta tags, structured data */
  var DEFAULT_BRAND = "Bazar Growth", brand = C.brandName || DEFAULT_BRAND;
  var swap = function (s) { return s.split(DEFAULT_BRAND).join(brand); };
  if (brand !== DEFAULT_BRAND) {
    document.title = swap(document.title);
    q('meta[name="description"],meta[name="keywords"],meta[property="og:title"],meta[property="og:description"],meta[property="og:site_name"]').forEach(function (m) { m.setAttribute("content", swap(m.getAttribute("content") || "")); });
    q("[aria-label]").forEach(function (el) { el.setAttribute("aria-label", swap(el.getAttribute("aria-label"))); });
    var tw = document.createTreeWalker(document.body, NodeFilter.SHOW_TEXT, null), tn = [];
    while (tw.nextNode()) { if (tw.currentNode.nodeValue.indexOf(DEFAULT_BRAND) > -1 && !/^(SCRIPT|STYLE)$/.test(tw.currentNode.parentNode.nodeName)) tn.push(tw.currentNode); }
    tn.forEach(function (n) { n.nodeValue = swap(n.nodeValue); });
  }
  var S = C.social || {};
  var sNames = { facebook: "Facebook", instagram: "Instagram", youtube: "YouTube", linkedin: "LinkedIn", twitter: "X (Twitter)", telegram: "Telegram" };
  var sKeys = Object.keys(sNames).filter(function (k) { return S[k]; });
  q('script[type="application/ld+json"]').forEach(function (s) {
    var t = s.textContent;
    if (brand !== DEFAULT_BRAND) t = swap(t);
    if (phone) t = t.split("+918510813357").join("+" + cc + phone);
    try {
      var j = JSON.parse(t);
      if (j["@type"] === "ProfessionalService" && sKeys.length) { j.sameAs = sKeys.map(function (k) { return S[k]; }); }
      t = JSON.stringify(j);
    } catch (err) { /* keep text as is */ }
    s.textContent = t;
  });

  /* phone, whatsapp, email values */
  q('[data-cfg="phone-text"]').forEach(function (el) { el.textContent = fmt(phone); });
  q('[data-cfg="whatsapp-text"]').forEach(function (el) { el.textContent = fmt(wa); });
  q('[data-cfg="email-text"]').forEach(function (el) { el.textContent = C.email || ""; });
  q('[data-cfg-href="tel"]').forEach(function (el) { el.href = "tel:+" + cc + phone; });
  q('[data-cfg-href="wa"]').forEach(function (el) {
    var msg = el.getAttribute("data-wa-msg") || "Hello, I would like to know more about your e-commerce seller services.";
    el.href = "https://wa.me/" + cc + wa + "?text=" + encodeURIComponent(msg);
    el.target = "_blank"; el.rel = "noopener";
  });
  q('[data-cfg-href="mail"]').forEach(function (el) { el.href = "mailto:" + (C.email || ""); });

  /* visibility toggles (elements start hidden in HTML when they depend on a value) */
  var setVis = function (el, ok) { el.hidden = !ok; el.style.display = ok ? "" : "none"; };
  q('[data-show="phone"]').forEach(function (el) { setVis(el, showPhone && !!phone); });
  q('[data-show="whatsapp"]').forEach(function (el) { setVis(el, showPhone && !!wa); });
  q('[data-show="email"]').forEach(function (el) { setVis(el, showForm && !!C.email); });
  q('[data-show="form"]').forEach(function (el) { setVis(el, showForm); });
  q('[data-show="affiliate"]').forEach(function (el) { setVis(el, !!C.affiliateLink); });
  q('[data-cfg-href="affiliate"]').forEach(function (el) { el.href = C.affiliateLink || "#"; el.target = "_blank"; el.rel = "noopener sponsored"; });
  q('[data-cfg="affiliate-label"]').forEach(function (el) { el.textContent = C.affiliateLabel || ""; });

  /* social media links */
  q("[data-social]").forEach(function (box) {
    box.innerHTML = "";
    sKeys.forEach(function (k) {
      var l = document.createElement("a");
      l.href = S[k]; l.target = "_blank"; l.rel = "noopener me"; l.className = "chip text-navy"; l.textContent = sNames[k];
      l.setAttribute("aria-label", (C.brandName || DEFAULT_BRAND) + " on " + sNames[k]);
      box.appendChild(l);
    });
    setVis(box, sKeys.length > 0);
  });
  q("[data-social-card]").forEach(function (c) { setVis(c, sKeys.length > 0); });

  /* mobile menu */
  var mb = document.getElementById("menuBtn"), mn = document.getElementById("mobileNav");
  if (mb && mn) {
    mb.addEventListener("click", function () {
      var open = mn.classList.toggle("hidden") === false;
      mb.setAttribute("aria-expanded", String(open));
      mb.textContent = open ? "Close" : "Menu";
    });
  }

  /* current page highlight */
  var here = (location.pathname.split("/").pop() || "index.html");
  q("[data-nav]").forEach(function (a) { if (a.getAttribute("href") === here) a.setAttribute("aria-current", "page"); });

  /* testimonials: from API or inline items, hidden when empty */
  var tSec = document.getElementById("testimonials");
  if (tSec) {
    var T = { api: C.testimonialsApi || (C.testimonials || {}).api || "", key: C.testimonialsKey || "", items: C.testimonialsItems || (C.testimonials || {}).items || [] };
    var render = function (items) {
      if (!showForm || !items || !items.length) { tSec.hidden = true; tSec.style.display = "none"; return; }
      var grid = document.getElementById("testimonialGrid");
      grid.innerHTML = "";
      items.slice(0, 6).forEach(function (t) {
        var d = document.createElement("figure");
        d.className = "card p-6 m-0";
        var bq = document.createElement("blockquote"); bq.className = "m-0 text-lg"; bq.textContent = "“" + (t.text || "") + "”";
        var cp = document.createElement("figcaption"); cp.className = "mt-4 font-display font-extrabold";
        cp.textContent = (t.name || "") + (t.role ? ", " + t.role : "");
        d.appendChild(bq); d.appendChild(cp); grid.appendChild(d);
      });
      tSec.hidden = false; tSec.style.display = "";
    };
    if (T.api) {
      fetch(T.api, T.key ? { headers: { "Authorization": "Bearer " + T.key } } : undefined).then(function (r) { return r.json(); }).then(function (j) { render(Array.isArray(j) ? j : (j.items || [])); }).catch(function () { render(T.items); });
    } else { render(T.items); }
  }

  /* enquiry form */
  var f = document.getElementById("enqForm");
  if (f) {
    var out = document.getElementById("formOut");
    var err = function (m, el) { out.innerHTML = '<div class="msg err" role="alert"></div>'; out.firstChild.textContent = m; if (el) el.focus(); };
    f.addEventListener("submit", function (e) {
      e.preventDefault();
      var name = f.elements.name.value.trim();
      var ph = digits(f.elements.phone.value);
      if (!name) { err("Please enter your name so we know who to call.", f.elements.name); return; }
      if (ph.length < 10 || ph.length > 12) { err("Please enter a valid 10-digit mobile number.", f.elements.phone); return; }
      var mps = q('input[name="marketplaces"]:checked', f).map(function (i) { return i.value; }).join(", ");
      var need = (q('input[name="need"]:checked', f)[0] || {}).value || "";
      var lines = ["New seller enquiry", "Name: " + name, "Phone: " + f.elements.phone.value.trim(),
        "City: " + (f.elements.city.value.trim() || "-"), "Need: " + need,
        "Marketplaces: " + (mps || "-"), "Products: " + (f.elements.message.value.trim() || "-")];
      var text = lines.join("\n");
      var btn = f.querySelector('button[type="submit"]');
      if (C.w3formsToken) {
        btn.disabled = true; btn.textContent = "Sending...";
        fetch("https://api.web3forms.com/submit", {
          method: "POST",
          headers: { "Content-Type": "application/json", "Accept": "application/json" },
          body: JSON.stringify({ access_key: C.w3formsToken, subject: "New seller enquiry for " + (C.brandName || "Bazar Growth"), from_name: name, name: name, phone: f.elements.phone.value.trim(), city: f.elements.city.value.trim(), need: need, marketplaces: mps, message: text })
        }).then(function (r) { return r.json(); }).then(function (j) {
          if (j && j.success) { location.href = "thank-you.html"; }
          else { btn.disabled = false; btn.textContent = "Request my free audit"; err("The form could not be sent. Please try again or message us on WhatsApp."); }
        }).catch(function () { btn.disabled = false; btn.textContent = "Request my free audit"; err("Network problem. Please try again or message us on WhatsApp."); });
      } else if (wa) {
        window.open("https://wa.me/" + cc + wa + "?text=" + encodeURIComponent(text), "_blank", "noopener");
        out.innerHTML = '<div class="msg" role="status"><strong>WhatsApp is opening with your enquiry.</strong> Press send there and we will reply soon.</div>';
      } else {
        err("This form is not connected yet. Please add a Web3Forms token or a WhatsApp number in config.js.");
      }
    });
  }

  /* ad budget planner (only on pages that include it) */
  var pf = document.getElementById("planForm");
  if (pf) {
    var inr = new Intl.NumberFormat("en-IN", { maximumFractionDigits: 0 });
    var $ = function (id) { return document.getElementById(id); };
    var num = function (v) { var n = parseFloat(v); return isFinite(n) ? n : 0; };
    var plan = function () {
      var price = Math.max(num($("pPrice").value), 1);
      var margin = Math.min(Math.max(num($("pMargin").value), 1), 90);
      var budget = Math.max(num($("pBudget").value), 0);
      var acos = Math.max(num($("pAcos").value), 1);
      $("pAcosOut").textContent = acos + "%";
      var sales = budget * 100 / acos, orders = sales / price, profit = sales * margin / 100 - budget, diff = margin - acos;
      $("oBeAcos").textContent = margin + "%";
      $("oBeRoas").textContent = (100 / margin).toFixed(1) + "x";
      $("oSales").textContent = "₹" + inr.format(sales);
      $("oOrders").textContent = inr.format(orders);
      $("oProfit").textContent = (profit < 0 ? "−" : "") + "₹" + inr.format(Math.abs(profit));
      var v = $("pVerdict");
      if (Math.abs(diff) < 0.5) { v.className = "verdict even"; v.textContent = "Break-even at this ACoS"; }
      else if (diff > 0) { v.className = "verdict good"; v.textContent = "Profitable at this ACoS"; }
      else { v.className = "verdict bad"; v.textContent = "Ads lose money at this ACoS"; }
      var costs = 100 - margin, prof = Math.max(diff, 0), total = costs + acos + prof;
      var w = function (x) { return (x / total * 100).toFixed(2) + "%"; };
      $("pBar").innerHTML = '<span class="seg c" style="width:' + w(costs) + '"></span><span class="seg a" style="width:' + w(acos) + '"></span>' + (prof > 0 ? '<span class="seg p" style="width:' + w(prof) + '"></span>' : "");
      $("pLegend").textContent = "Product, fees and shipping ₹" + costs.toFixed(0) + "  |  Ads ₹" + acos.toFixed(0) + (diff > 0 ? "  |  Profit ₹" + diff.toFixed(0) : diff < 0 ? "  |  Loss ₹" + Math.abs(diff).toFixed(0) : "  |  Profit ₹0");
    };
    ["pPrice", "pMargin", "pBudget", "pAcos"].forEach(function (id) { $(id).addEventListener("input", plan); });
    pf.addEventListener("submit", function (e) { e.preventDefault(); });
    plan();
  }
})();

/* Reads window.SITE_CONFIG and updates every page. Vanilla JS, no dependencies. */
(function () {
  var C = window.SITE_CONFIG || {};
  var digits = function (v) { return String(v || "").replace(/\D/g, ""); };
  var cc = digits(C.countryCode) || "91";
  var phone = digits(C.phone), wa = digits(C.whatsapp);
  var intl = function (n) { return n.length > 10 ? n : cc + n; };
  var pretty = phone ? "+" + cc + " " + phone.slice(-10, -5) + " " + phone.slice(-5) : "";
  var $$ = function (s) { return Array.prototype.slice.call(document.querySelectorAll(s)); };

  // Brand
  $$("[data-brand]").forEach(function (el) { el.textContent = C.brandName; });
  $$("[data-tagline]").forEach(function (el) { el.textContent = C.tagline; });
  $$("[data-year]").forEach(function (el) { el.textContent = new Date().getFullYear(); });
  var t = document.title; if (C.brandName) { document.title = t; }

  // Phone / WhatsApp
  var showPW = C.showPhoneWhatsapp !== false;
  $$("[data-only='phone']").forEach(function (el) { if (!showPW || !phone) el.classList.add("hidden"); });
  $$("[data-only='wa']").forEach(function (el) { if (!showPW || !wa) el.classList.add("hidden"); });
  $$("[data-phone]").forEach(function (el) { el.textContent = pretty; });
  $$("[data-tel]").forEach(function (el) { el.setAttribute("href", "tel:+" + intl(phone)); });
  $$("[data-wa]").forEach(function (el) {
    var msg = el.getAttribute("data-wa-text") || "Hello " + C.brandName + ", I need help with my e-commerce seller account.";
    el.setAttribute("href", "https://wa.me/" + intl(wa) + "?text=" + encodeURIComponent(msg));
    el.setAttribute("target", "_blank"); el.setAttribute("rel", "noopener");
  });

  // Email / forms / testimonials
  var showEF = C.showEmailFormsTestimonials !== false;
  $$("[data-only='email']").forEach(function (el) { if (!showEF || !C.email) el.classList.add("hidden"); });
  $$("[data-only='forms']").forEach(function (el) { if (!showEF) el.classList.add("hidden"); });
  $$("[data-only='testimonials']").forEach(function (el) { if (!showEF) el.classList.add("hidden"); });
  $$("[data-mail]").forEach(function (el) { el.setAttribute("href", "mailto:" + C.email); });
  $$("[data-email]").forEach(function (el) { el.textContent = C.email; });

  // Affiliate
  $$("[data-only='affiliate']").forEach(function (el) { if (!C.affiliateLink) el.classList.add("hidden"); });
  $$("[data-affiliate]").forEach(function (el) {
    el.setAttribute("href", C.affiliateLink || "#"); el.setAttribute("target", "_blank");
    el.setAttribute("rel", "sponsored noopener");
  });
  $$("[data-affiliate-label]").forEach(function (el) { el.textContent = C.affiliateLabel; });

  // Mobile menu
  var btn = document.getElementById("menu-btn"), menu = document.getElementById("mobile-menu");
  if (btn && menu) btn.addEventListener("click", function () {
    var open = menu.classList.toggle("hidden") === false;
    btn.setAttribute("aria-expanded", open ? "true" : "false");
  });

  // Active nav link
  var here = location.pathname.split("/").pop() || "index.html";
  $$("[data-nav]").forEach(function (a) {
    if (a.getAttribute("href") === here) { a.classList.add("text-amber-500"); a.setAttribute("aria-current", "page"); }
  });

  // W3Forms handling
  $$("form[data-w3form]").forEach(function (form) {
    var status = form.querySelector("[data-status]");
    var say = function (msg, ok) {
      if (!status) return; status.textContent = msg;
      status.className = "mt-3 text-sm font-medium " + (ok ? "text-green-600" : "text-red-600");
    };
    form.addEventListener("submit", function (e) {
      e.preventDefault();
      if (!C.w3formsToken) {
        say("The contact form is not activated yet. Please reach us on WhatsApp or phone instead.", false); return;
      }
      var fd = new FormData(form);
      fd.append("access_key", C.w3formsToken);
      fd.append("subject", "New enquiry from " + C.brandName + " website (" + document.title + ")");
      fd.append("from_name", C.brandName + " Website");
      var submit = form.querySelector("button[type=submit]"); if (submit) submit.disabled = true;
      say("Sending your message...", true);
      fetch("https://api.web3forms.com/submit", { method: "POST", body: fd })
        .then(function (r) { return r.json(); })
        .then(function (d) {
          if (d.success) { window.location.href = "thank-you.html"; }
          else { say(d.message || "Something went wrong. Please try WhatsApp.", false); if (submit) submit.disabled = false; }
        })
        .catch(function () { say("Network error. Please try again or use WhatsApp.", false); if (submit) submit.disabled = false; });
    });
  });

  // Testimonials
  var host = document.getElementById("testimonial-list");
  if (host && showEF) {
    var render = function (items) {
      host.innerHTML = "";
      if (!items || !items.length) {
        var d = document.createElement("div");
        d.className = "md:col-span-3 rounded-2xl border border-dashed border-slate-300 p-8 text-center text-slate-600";
        d.innerHTML = "<p class='font-semibold text-slate-800'>Client stories are on the way.</p><p class='mt-1 text-sm'>Have you worked with us? <a class='text-indigo-700 underline' href='contact.html'>Share your experience</a>.</p>";
        host.appendChild(d); return;
      }
      items.slice(0, 6).forEach(function (it) {
        var card = document.createElement("figure");
        card.className = "rounded-2xl bg-white p-6 shadow-sm ring-1 ring-slate-200";
        var stars = document.createElement("div"); stars.className = "text-amber-500";
        var n = Math.max(0, Math.min(5, parseInt(it.rating || 5, 10)));
        stars.textContent = "★".repeat(n) + "☆".repeat(5 - n);
        stars.setAttribute("aria-label", n + " out of 5 stars");
        var q = document.createElement("blockquote"); q.className = "mt-3 text-slate-700"; q.textContent = "“" + (it.text || "") + "”";
        var cap = document.createElement("figcaption"); cap.className = "mt-4 text-sm font-semibold text-slate-900";
        cap.textContent = (it.name || "Verified client") + (it.role ? " • " + it.role : "");
        card.appendChild(stars); card.appendChild(q); card.appendChild(cap); host.appendChild(card);
      });
    };
    var tc = C.testimonials || {};
    if (tc.api) {
      var url = tc.api + (tc.key ? (tc.api.indexOf("?") > -1 ? "&" : "?") + "key=" + encodeURIComponent(tc.key) : "");
      fetch(url).then(function (r) { return r.json(); })
        .then(function (d) { render(Array.isArray(d) ? d : (d.items || [])); })
        .catch(function () { render(tc.items); });
    } else { render(tc.items); }
  }

  // FAQ accordions use native <details>; nothing needed.
})();

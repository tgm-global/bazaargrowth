#!/usr/bin/env python3
"""Generates every page of the Budget Bazaar static site. Run: python3 tools/build.py"""
import os, sys, html
sys.path.insert(0, os.path.dirname(__file__))
from data import *

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PAGES = []  # (filename, priority)
e = html.escape
PH = "+%s %s %s" % (CC, PHONE[-10:-5], PHONE[-5:])

def link(href, text, cls="text-indigo-700 underline"):
    return '<a class="%s" href="%s">%s</a>' % (cls, href, text)

NAV = [("index.html","Home"),("services.html","Services"),("marketplaces.html","Marketplaces"),("pricing.html","Pricing"),("locations.html","Cities"),("about.html","About"),("faq.html","FAQ"),("contact.html","Contact")]

def header():
    items = "".join('<a data-nav class="px-2 py-2 text-sm font-semibold text-slate-100 hover:text-amber-400" href="%s">%s</a>' % (h, t) for h, t in NAV)
    mob = "".join('<a class="block rounded-lg px-3 py-3 font-semibold text-slate-100 hover:bg-white/10" href="%s">%s</a>' % (h, t) for h, t in NAV)
    return '''<header class="sticky top-0 z-50 bg-slate-900/95 backdrop-blur shadow-lg">
<div class="mx-auto flex max-w-7xl items-center justify-between px-4 py-3">
<a href="index.html" class="flex items-center gap-2" aria-label="%(b)s home"><span class="grid h-9 w-9 place-items-center rounded-lg bg-amber-400 font-extrabold text-slate-900">B</span><span class="leading-tight"><span data-brand class="block text-lg font-extrabold text-white">%(b)s</span><span data-tagline class="block text-[11px] uppercase tracking-wider text-amber-300">E-commerce Seller Services</span></span></a>
<nav class="hidden items-center gap-1 lg:flex" aria-label="Main navigation">%(items)s</nav>
<div class="flex items-center gap-2">
<a data-only="phone" data-tel href="tel:+%(cc)s%(ph)s" class="hidden rounded-lg border border-white/30 px-3 py-2 text-sm font-bold text-white hover:bg-white/10 md:inline-flex">Call <span data-phone class="ml-1 hidden xl:inline">%(pretty)s</span></a>
<a data-only="wa" data-wa href="#" class="hidden rounded-lg bg-green-500 px-3 py-2 text-sm font-bold text-white hover:bg-green-600 sm:inline-flex">WhatsApp</a>
<button id="menu-btn" aria-label="Toggle menu" aria-expanded="false" aria-controls="mobile-menu" class="rounded-lg p-2 text-white lg:hidden"><svg width="26" height="26" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M4 6h16M4 12h16M4 18h16"/></svg></button>
</div></div>
<div id="mobile-menu" class="hidden max-h-[75vh] overflow-y-auto border-t border-white/10 px-4 pb-4 lg:hidden">%(mob)s
<div class="mt-3 flex gap-2"><a data-only="phone" data-tel href="tel:+%(cc)s%(ph)s" class="flex-1 rounded-lg border border-white/30 px-3 py-3 text-center font-bold text-white">Call now</a><a data-only="wa" data-wa href="#" class="flex-1 rounded-lg bg-green-500 px-3 py-3 text-center font-bold text-white">WhatsApp</a></div></div>
</header>''' % dict(b=BRAND, items=items, mob=mob, cc=CC, ph=PHONE, pretty=PH)

def footer():
    svc = "".join('<li><a class="hover:text-amber-400" href="%s.html">%s</a></li>' % (s["slug"], s["name"]) for s in SERVICES)
    cit = "".join('<li><a class="hover:text-amber-400" href="seller-services-%s.html">%s</a></li>' % (c["slug"], c["name"]) for c in CITIES[:8])
    return '''<footer class="bg-slate-900 text-slate-300">
<div class="mx-auto grid max-w-7xl gap-8 px-4 py-12 sm:grid-cols-2 lg:grid-cols-4">
<div><p data-brand class="text-xl font-extrabold text-white">%(b)s</p><p class="mt-3 text-sm leading-relaxed">Independent e-commerce seller services for Indian sellers: account setup, listings, compliance, ads and account health.</p>
<ul class="mt-4 space-y-1 text-sm"><li data-only="phone">Phone: <a data-tel data-phone class="font-semibold text-white" href="tel:+%(cc)s%(ph)s">%(pretty)s</a></li><li data-only="email">Email: <a data-mail data-email class="font-semibold text-white" href="#"></a></li></ul></div>
<div><h2 class="text-sm font-bold uppercase tracking-wider text-white">Services</h2><ul class="mt-3 space-y-2 text-sm">%(svc)s</ul></div>
<div><h2 class="text-sm font-bold uppercase tracking-wider text-white">Cities we serve</h2><ul class="mt-3 space-y-2 text-sm">%(cit)s<li><a class="font-semibold text-amber-400" href="locations.html">All cities &rarr;</a></li></ul></div>
<div><h2 class="text-sm font-bold uppercase tracking-wider text-white">Company</h2><ul class="mt-3 space-y-2 text-sm"><li><a class="hover:text-amber-400" href="about.html">About us</a></li><li><a class="hover:text-amber-400" href="marketplaces.html">Marketplaces</a></li><li><a class="hover:text-amber-400" href="pricing.html">Pricing</a></li><li><a class="hover:text-amber-400" href="faq.html">FAQ</a></li><li><a class="hover:text-amber-400" href="contact.html">Contact</a></li><li><a class="hover:text-amber-400" href="privacy.html">Privacy Policy</a></li><li><a class="hover:text-amber-400" href="terms.html">Terms &amp; Conditions</a></li><li><a class="hover:text-amber-400" href="disclaimer.html">Disclaimer</a></li></ul></div>
</div>
<div class="border-t border-white/10 px-4 py-6 text-center text-xs text-slate-400">Marketplace names mentioned belong to their respective owners. <span data-brand>%(b)s</span> is an independent service provider and is not affiliated with or endorsed by any marketplace.</div>
</footer>
<div class="fixed inset-x-0 bottom-0 z-40 border-t border-white/10 bg-slate-950 text-slate-200 shadow-[0_-4px_12px_rgba(0,0,0,.25)]">
<div class="mx-auto flex max-w-7xl flex-wrap items-center justify-between gap-x-4 gap-y-1 px-4 py-2 text-xs">
<p>&copy; <span data-year>2026</span> <span data-brand>%(b)s</span></p>
<p class="hidden gap-3 sm:flex"><a class="hover:text-amber-400" href="privacy.html">Privacy</a><a class="hover:text-amber-400" href="terms.html">Terms</a><a class="hover:text-amber-400" href="disclaimer.html">Disclaimer</a><a class="hover:text-amber-400" href="locations.html">Cities</a></p>
<p class="flex gap-2"><a data-only="phone" data-tel href="tel:+%(cc)s%(ph)s" class="rounded bg-white/10 px-3 py-1 font-bold">Call</a><a data-only="wa" data-wa href="#" class="rounded bg-green-500 px-3 py-1 font-bold text-white">WhatsApp</a><a href="contact.html" class="rounded bg-amber-400 px-3 py-1 font-bold text-slate-900">Get a quote</a></p>
</div></div>''' % dict(b=BRAND, cc=CC, ph=PHONE, pretty=PH, svc=svc, cit=cit)

def page(fn, title, desc, kw, body, prio="0.7", index=True, schema=""):
    if index: PAGES.append((fn, prio))
    robots = "index, follow" if index else "noindex, follow"
    out = '''<!DOCTYPE html>
<html lang="en-IN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>%(t)s</title>
<meta name="description" content="%(d)s">
<meta name="keywords" content="%(k)s">
<meta name="robots" content="%(r)s">
<link rel="canonical" href="%(u)s%(fn)s">
<meta property="og:type" content="website">
<meta property="og:title" content="%(t)s">
<meta property="og:description" content="%(d)s">
<meta property="og:url" content="%(u)s%(fn)s">
<meta property="og:site_name" content="%(b)s">
<meta name="twitter:card" content="summary">
<meta name="theme-color" content="#0f172a">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap" rel="stylesheet">
<script src="https://cdn.tailwindcss.com"></script>
<link rel="stylesheet" href="assets/styles.css">
<script type="application/ld+json">{"@context":"https://schema.org","@type":"ProfessionalService","name":"%(b)s","description":"E-commerce seller services in India","areaServed":"IN","telephone":"+%(cc)s%(ph)s","url":"%(u)s"}</script>
%(schema)s
</head>
<body class="bg-white text-slate-800 antialiased">
<a href="#main" class="sr-only focus:not-sr-only focus:absolute focus:z-[60] focus:bg-amber-400 focus:p-3">Skip to content</a>
%(h)s
<main id="main">
%(body)s
</main>
%(f)s
<script src="assets/config.js"></script>
<script src="assets/site.js"></script>
</body>
</html>
''' % dict(t=e(title), d=e(desc), k=e(kw), r=robots, u=SITE_URL, fn=fn, b=BRAND, cc=CC, ph=PHONE, schema=schema, h=header(), f=footer(), body=body)
    assert len(title) <= 70 and len(desc) <= 170, (fn, len(title), len(desc))
    with open(os.path.join(ROOT, fn), "w", encoding="utf-8") as f: f.write(out)

def hero(h1, sub, cta=True, kicker=""):
    c = ''
    if cta:
        c = '''<div class="mt-8 flex flex-wrap gap-3"><a href="contact.html" class="rounded-xl bg-amber-400 px-6 py-3 font-bold text-slate-900 shadow hover:bg-amber-300">Get a free consultation</a><a data-only="wa" data-wa href="#" class="rounded-xl bg-green-500 px-6 py-3 font-bold text-white hover:bg-green-600">Chat on WhatsApp</a><a href="services.html" class="rounded-xl border border-white/40 px-6 py-3 font-bold text-white hover:bg-white/10">Explore services</a></div>'''
    k = '<p class="text-sm font-bold uppercase tracking-widest text-amber-300">%s</p>' % kicker if kicker else ""
    return '<section class="hero-bg text-white"><div class="mx-auto max-w-7xl px-4 py-16 md:py-24"><div class="max-w-3xl">%s<h1 class="mt-2 text-3xl font-extrabold leading-tight md:text-5xl">%s</h1><p class="mt-5 text-lg text-slate-200">%s</p>%s</div></div></section>' % (k, h1, sub, c)

def wrap(inner, cls="py-14"):
    return '<section class="%s"><div class="mx-auto max-w-7xl px-4">%s</div></section>' % (cls, inner)

def h2(t, sub=""):
    s = '<p class="mt-3 max-w-3xl text-slate-600">%s</p>' % sub if sub else ""
    return '<h2 class="text-2xl font-extrabold text-slate-900 md:text-3xl">%s</h2>%s' % (t, s)

def form(fid):
    opts = "".join("<option>%s</option>" % e(s["name"]) for s in SERVICES) + "<option>Not sure yet</option>"
    return '''<form data-w3form id="%(i)s" class="rounded-2xl bg-white p-6 shadow-lg ring-1 ring-slate-200" novalidate>
<input type="checkbox" name="botcheck" class="hidden" style="display:none" tabindex="-1" autocomplete="off">
<div class="grid gap-4 sm:grid-cols-2">
<label class="block text-sm font-semibold text-slate-700">Full name<input required name="name" autocomplete="name" class="mt-1 w-full rounded-lg border border-slate-300 px-3 py-2 font-normal"></label>
<label class="block text-sm font-semibold text-slate-700">Phone / WhatsApp<input required name="phone" type="tel" autocomplete="tel" class="mt-1 w-full rounded-lg border border-slate-300 px-3 py-2 font-normal"></label>
<label class="block text-sm font-semibold text-slate-700">Email (optional)<input name="email" type="email" autocomplete="email" class="mt-1 w-full rounded-lg border border-slate-300 px-3 py-2 font-normal"></label>
<label class="block text-sm font-semibold text-slate-700">Service needed<select name="service" class="mt-1 w-full rounded-lg border border-slate-300 bg-white px-3 py-2 font-normal">%(o)s</select></label>
</div>
<label class="mt-4 block text-sm font-semibold text-slate-700">Tell us about your products and marketplaces<textarea required name="message" rows="4" class="mt-1 w-full rounded-lg border border-slate-300 px-3 py-2 font-normal"></textarea></label>
<button type="submit" class="mt-5 w-full rounded-xl bg-indigo-700 px-6 py-3 font-bold text-white hover:bg-indigo-800 disabled:opacity-60">Send enquiry</button>
<p data-status role="status" aria-live="polite" class="mt-3 text-sm"></p>
<p class="mt-2 text-xs text-slate-500">By submitting, you agree to our <a class="underline" href="privacy.html">Privacy Policy</a>.</p>
</form>''' % dict(i=fid, o=opts)

def lead_block(title="Tell us what you sell. We will suggest the next step."):
    return '<section class="bg-slate-50 py-14" data-only="forms"><div class="mx-auto grid max-w-7xl items-start gap-10 px-4 lg:grid-cols-2"><div>%s<p class="mt-4 text-slate-600">Share a few details and a member of our team will reply with a clear recommendation, not a sales script. Prefer a quick chat? Use WhatsApp.</p><ul class="mt-6 space-y-2 text-slate-700"><li>&#10003; Free first consultation</li><li>&#10003; Plain-language scope and quote</li><li>&#10003; You keep full ownership of your seller account</li></ul><p class="mt-6 text-sm text-slate-600">Browse our %s or see %s first.</p></div>%s</div></section>' % (h2(title), link("services.html","services"), link("pricing.html","how pricing works"), form("lead-form-%d" % len(PAGES)))

def cta_band(text="Ready to grow your marketplace business?"):
    return '<section class="bg-indigo-800 py-12 text-white"><div class="mx-auto flex max-w-7xl flex-col items-center gap-5 px-4 text-center md:flex-row md:justify-between md:text-left"><p class="text-2xl font-extrabold">%s</p><div class="flex flex-wrap justify-center gap-3"><a href="contact.html" class="rounded-xl bg-amber-400 px-6 py-3 font-bold text-slate-900">Request a quote</a><a data-only="wa" data-wa href="#" class="rounded-xl bg-green-500 px-6 py-3 font-bold text-white">WhatsApp us</a></div></div></section>' % text

def affiliate_block():
    return '<section data-only="affiliate" class="py-6"><div class="mx-auto max-w-7xl px-4"><a data-affiliate href="#" class="flex flex-col items-center justify-between gap-2 rounded-2xl border border-amber-300 bg-amber-50 p-5 text-center sm:flex-row sm:text-left"><span><strong data-affiliate-label class="text-slate-900"></strong><span class="block text-sm text-slate-600">Tools we find useful for sellers. This is an affiliate link and we may earn a commission at no extra cost to you.</span></span><span class="rounded-lg bg-amber-400 px-4 py-2 font-bold text-slate-900">View offer</span></a></div></section>'

def faq_list(items):
    return "".join('<details class="group rounded-xl bg-white p-5 ring-1 ring-slate-200"><summary class="flex items-center justify-between gap-4 font-bold text-slate-900"><h3 class="text-base font-bold">%s</h3><span class="chev text-indigo-700 transition-transform">&#9660;</span></summary><p class="mt-3 text-slate-700">%s</p></details>' % (e(q), e(a)) for q, a in items)

def faq_schema(items):
    import json
    d = {"@context":"https://schema.org","@type":"FAQPage","mainEntity":[{"@type":"Question","name":q,"acceptedAnswer":{"@type":"Answer","text":a}} for q,a in items]}
    return '<script type="application/ld+json">%s</script>' % json.dumps(d).replace("</", "<\\/")

def crumbs(items):
    return '<nav aria-label="Breadcrumb" class="border-b bg-slate-50"><ol class="mx-auto flex max-w-7xl flex-wrap gap-2 px-4 py-3 text-sm text-slate-600"><li><a class="underline" href="index.html">Home</a></li>%s</ol></nav>' % "".join("<li>/ %s</li>" % (link(h, t) if h else e(t)) for h, t in items)

def svc_cards(sub=False):
    return '<div class="mt-8 grid gap-6 sm:grid-cols-2 lg:grid-cols-3">%s</div>' % "".join('<article class="flex flex-col rounded-2xl bg-white p-6 shadow-sm ring-1 ring-slate-200 transition hover:-translate-y-1 hover:shadow-lg"><h3 class="text-lg font-extrabold text-slate-900">%s</h3><p class="mt-2 flex-1 text-slate-600">%s</p><a class="mt-4 font-bold text-indigo-700" href="%s.html">Learn more &rarr;</a></article>' % (s["name"].replace("&","&amp;"), e(s["short"]), s["slug"]) for s in SERVICES)

def city_chips(exclude=None):
    return '<div class="mt-6 flex flex-wrap gap-2">%s</div>' % "".join('<a class="rounded-full bg-white px-4 py-2 text-sm font-semibold text-indigo-800 ring-1 ring-slate-300 hover:bg-amber-100" href="seller-services-%s.html">%s</a>' % (c["slug"], c["name"]) for c in CITIES if c["slug"] != exclude)

def testimonials():
    return '<section data-only="testimonials" class="bg-slate-50 py-14"><div class="mx-auto max-w-7xl px-4">%s<div id="testimonial-list" class="mt-8 grid gap-6 md:grid-cols-3"></div></div></section>' % h2("What sellers say", "Real feedback from sellers we have supported.")

# ---------------- HOME ----------------
steps = [("Discover","A short call to understand your products, budget and marketplace goals."),("Plan","A clear scope with priorities, timelines and a transparent quote."),("Execute","Our team handles setup, listings, ads or compliance while you keep control."),("Improve","Weekly and monthly reviews that turn data into your next decision.")]
why = [("Seller-first focus","We work only on e-commerce seller problems, so our process is built around listings, settlements, returns and ads."),("Built for India","GST, pincode serviceability, cash-on-delivery risk and festive-season peaks shape every plan we write."),("Honest promises","No guaranteed rankings and no secret fees. You get scope, reporting and straight answers."),("You own everything","Your account, your brand, your data. We work with the access you grant and you can remove it any time.")]
body = hero("Sell smarter on Amazon, Flipkart and Meesho with %s" % BRAND, "End-to-end e-commerce seller services for Indian businesses: account setup, product listings, GST guidance, advertising and account-health protection.", kicker="E-commerce seller services in India")
body += wrap(h2("Everything a marketplace seller needs, in one team", "Pick one service or combine them. Each service has a clear scope, a defined process and plain-language reporting.") + svc_cards(), "py-14")
body += '<section class="bg-slate-50 py-14"><div class="mx-auto max-w-7xl px-4">%s<ol class="mt-8 grid gap-6 md:grid-cols-4">%s</ol></div></section>' % (h2("How we work with you"), "".join('<li class="rounded-2xl bg-white p-6 ring-1 ring-slate-200"><span class="grid h-10 w-10 place-items-center rounded-full bg-indigo-700 font-extrabold text-white">%d</span><h3 class="mt-4 text-lg font-bold">%s</h3><p class="mt-2 text-slate-600">%s</p></li>' % (i+1, t, d) for i,(t,d) in enumerate(steps)))
body += wrap(h2("Why sellers choose %s" % BRAND) + '<div class="mt-8 grid gap-6 md:grid-cols-2">%s</div>' % "".join('<div class="rounded-2xl border-l-4 border-amber-400 bg-white p-6 shadow-sm ring-1 ring-slate-200"><h3 class="text-lg font-bold">%s</h3><p class="mt-2 text-slate-600">%s</p></div>' % (t,d) for t,d in why))
body += '<section class="bg-slate-900 py-14 text-white"><div class="mx-auto max-w-7xl px-4"><h2 class="text-2xl font-extrabold md:text-3xl">Marketplaces we work with</h2><p class="mt-3 max-w-3xl text-slate-300">From giant platforms to emerging channels, we help you pick where to sell and how to win there. Read our %s guide.</p><div class="mt-6 flex flex-wrap gap-3">%s</div></div></section>' % (link("marketplaces.html","marketplaces","text-amber-300 underline"), "".join('<span class="rounded-full bg-white/10 px-4 py-2 text-sm font-semibold">%s</span>' % m[0] for m in MARKETS))
body += wrap(h2("Seller services across India", "We support sellers in major business hubs and remotely across the country. Choose your city to see local insights.") + city_chips() + '<p class="mt-4">%s</p>' % link("locations.html","See all city pages &rarr;"))
body += affiliate_block() + testimonials() + lead_block()
body += wrap(h2("Quick answers") + '<div class="mt-6 grid gap-3 md:grid-cols-2">%s</div><p class="mt-6">%s</p>' % (faq_list(FAQS[:4]), link("faq.html","Read all FAQs &rarr;")), "py-14") + cta_band()
page("index.html", "%s | E-commerce Seller Services India" % BRAND, "%s helps Indian sellers grow on Amazon, Flipkart and Meesho with account setup, listings, GST guidance, ads and account-health support." % BRAND,
 "e-commerce seller services India, Amazon seller services, Flipkart seller support, marketplace account management, product listing services, %s" % BRAND.lower(), body, "1.0", schema=faq_schema(FAQS[:4]))

# ---------------- SERVICES HUB ----------------
body = hero("E-commerce seller services built around your marketplace goals", "Six focused services that cover the full seller journey, from first registration to monthly growth reviews.", kicker="Our services")
body += crumbs([("", "Services")]) + wrap(svc_cards() + '<div class="prose-bb mt-12 max-w-3xl"><h2>How to choose the right service</h2><p>If you have not sold online before, start with %s so that your registration is clean. If you already sell but sales are flat, begin with %s and %s. If you have orders but profit is thin, %s and %s usually find the leaks first.</p><p>Not sure? Our %s explains how we scope work, or you can %s for a free consultation.</p></div>' % (link("seller-account-setup.html","account setup"), link("product-listing-catalog.html","catalogue management"), link("product-photography-aplus.html","product imagery"), link("marketplace-ads-growth.html","advertising control"), link("account-health-returns.html","returns and RTO management"), link("pricing.html","pricing page"), link("contact.html","contact us")))
body += affiliate_block() + cta_band()
page("services.html", "Seller Services | Listings, Ads, Compliance | %s" % BRAND, "Explore %s e-commerce seller services: account setup, product listings, GST support, marketplace ads, returns management and product photography." % BRAND,
 "ecommerce seller services, marketplace management services, seller account management India, listing services, ads management", body, "0.9")

# ---------------- SERVICE PAGES ----------------
for s in SERVICES:
    others = [o for o in SERVICES if o["slug"] != s["slug"]][:3]
    body = hero(s["name"].replace("&","&amp;") + " for Indian sellers", s["intro"], kicker="Service")
    body += crumbs([("services.html","Services"),("", s["name"])])
    body += wrap('<div class="grid gap-10 lg:grid-cols-3"><div class="prose-bb lg:col-span-2"><h2>What we do</h2><ul>%s</ul><h2>Who this service is for</h2><p>%s</p><h2>Our process</h2><ol class="mt-3 list-decimal space-y-2 pl-5 text-slate-700">%s</ol><h2>Related services</h2><p>%s</p><p>Based in a major business hub? See our city pages for %s, %s and %s, or browse %s.</p></div><aside class="h-fit rounded-2xl bg-slate-50 p-6 ring-1 ring-slate-200 lg:sticky lg:top-24"><h2 class="text-lg font-extrabold">Talk to a seller expert</h2><p class="mt-2 text-sm text-slate-600">Get a scope and quote for this service. No obligation.</p><a href="contact.html" class="mt-4 block rounded-xl bg-indigo-700 px-4 py-3 text-center font-bold text-white">Request a quote</a><a data-only="wa" data-wa data-wa-text="Hello, I am interested in %s." href="#" class="mt-3 block rounded-xl bg-green-500 px-4 py-3 text-center font-bold text-white">WhatsApp</a></aside></div>' % (
        "".join("<li>%s</li>" % e(x) for x in s["does"]), e(s["who"]), "".join("<li>%s</li>" % e(x) for x in s["steps"]),
        " &bull; ".join(link(o["slug"]+".html", o["name"].replace("&","&amp;")) for o in others),
        link("seller-services-delhi-ncr.html","Delhi NCR"), link("seller-services-mumbai.html","Mumbai"), link("seller-services-bengaluru.html","Bengaluru"), link("locations.html","all cities"), e(s["name"])))
    body += '<section class="bg-slate-50 py-14"><div class="mx-auto max-w-4xl px-4">%s<div class="mt-6 space-y-3">%s</div></div></section>' % (h2("Frequently asked questions"), faq_list(s["faqs"]))
    body += lead_block("Start with %s" % s["name"].replace("&","&amp;")) + cta_band()
    page(s["slug"]+".html", "%s | %s" % (s["title"], BRAND), (lambda d: d if len(d) <= 165 else d[:160].rsplit(" ",1)[0] + "...")("%s by %s. %s" % (s["name"], BRAND, s["short"])), s["kw"], body, "0.8", schema=faq_schema(s["faqs"]))

# ---------------- MARKETPLACES ----------------
body = hero("Marketplace guide for Indian e-commerce sellers", "Each marketplace rewards a different approach. Here is how we think about where to sell and how to win on each platform.", kicker="Marketplaces")
body += crumbs([("", "Marketplaces")])
body += wrap('<div class="grid gap-6 md:grid-cols-2">%s</div><div class="prose-bb mt-10 max-w-3xl"><h2>Should you sell on one marketplace or several?</h2><p>Starting with one lets you perfect listings, packaging and returns before you split attention. Once your first channel is stable and profitable, adding a second reduces dependence on one platform. We help you choose the order using your category, price point and margin.</p><p>Ready to begin? See our %s or %s service, or compare prices on our %s.</p></div>' % (
    "".join('<article class="rounded-2xl bg-white p-6 shadow-sm ring-1 ring-slate-200"><h2 class="text-xl font-extrabold">%s</h2><p class="mt-2 text-slate-600">%s</p></article>' % (e(n), e(d)) for n, d in MARKETS),
    link("seller-account-setup.html","account setup"), link("product-listing-catalog.html","listing management"), link("pricing.html","pricing page")))
body += affiliate_block() + cta_band("Not sure which marketplace fits your product?")
page("marketplaces.html", "Amazon, Flipkart, Meesho Seller Guide | %s" % BRAND, "Compare Indian marketplaces for sellers: Amazon, Flipkart, Meesho, Myntra, beauty platforms and ONDC. Learn where your products fit best.",
 "Amazon vs Flipkart seller, Meesho seller guide, best marketplace to sell online India, Myntra seller, ONDC seller", body, "0.8")

# ---------------- PRICING ----------------
tiers = [("Starter","One marketplace, a small catalogue and one core service such as account setup or a listing audit.",["Free first consultation","Clear one-time scope","Handover session"]),("Growth","One or two marketplaces with ongoing catalogue, content and advertising support.",["Monthly optimisation","Weekly ad reviews","Monthly performance report"]),("Scale","Multiple marketplaces, large catalogues, compliance coordination and account-health protection.",["Dedicated account contact","Priority notice response","Quarterly strategy review"])]
body = hero("Transparent pricing, scoped to your business", "Every seller's catalogue, categories and goals are different, so we quote on scope. No hidden fees and no long lock-in contracts.", kicker="Pricing")
body += crumbs([("", "Pricing")])
body += wrap('<div class="grid gap-6 md:grid-cols-3">%s</div><div class="prose-bb mt-10 max-w-3xl"><h2>What affects your quote</h2><ul><li>Number of SKUs and variations</li><li>Number of marketplaces</li><li>Which of our %s you need</li><li>Whether you need one-time work or monthly management</li></ul><p>Advertising budgets and marketplace fees are separate and are paid by you directly to the marketplace. Ready for an estimate? %s or message us on WhatsApp.</p></div>' % (
    "".join('<article class="rounded-2xl bg-white p-6 shadow-sm ring-1 ring-slate-200"><h2 class="text-xl font-extrabold text-indigo-800">%s</h2><p class="mt-2 text-slate-600">%s</p><ul class="mt-4 space-y-2 text-sm text-slate-700">%s</ul><a href="contact.html" class="mt-6 block rounded-xl bg-indigo-700 px-4 py-3 text-center font-bold text-white">Get a quote</a></article>' % (n, d, "".join("<li>&#10003; %s</li>" % x for x in f)) for n, d, f in tiers),
    link("services.html","services"), link("contact.html","Request a custom quote")))
body += cta_band()
page("pricing.html", "Pricing for Seller Services | %s" % BRAND, "See how %s prices e-commerce seller services: scope-based quotes for account setup, listings, ads and compliance with no hidden fees." % BRAND,
 "ecommerce seller services pricing, marketplace management cost India, listing service price, amazon account management fees", body, "0.7")

# ---------------- ABOUT ----------------
body = hero("About %s" % BRAND, "We exist to make marketplace selling simpler, safer and more profitable for Indian sellers of every size.", cta=False, kicker="About us")
body += crumbs([("", "About")])
body += wrap('<div class="prose-bb max-w-3xl"><h2>Our story</h2><p>%s started with a simple observation: capable shopkeepers, manufacturers and home-based entrepreneurs were losing weeks to rejected registrations, suppressed listings and confusing settlement reports. They did not need another generic agency. They needed a practical partner who understood the seller dashboard.</p><h2>What we believe</h2><ul><li><strong>Clarity over jargon.</strong> You should always know what we are doing and why.</li><li><strong>Compliance first.</strong> Shortcuts that risk your account are never worth it.</li><li><strong>Your data stays yours.</strong> We work through access you control.</li></ul><h2>Where we work</h2><p>We support sellers remotely across India, with local insights for hubs such as %s, %s and %s. See every %s.</p><h2>Work with us</h2><p>Browse our %s, check %s, or %s for a free conversation.</p></div>' % (BRAND, link("seller-services-delhi-ncr.html","Delhi NCR"), link("seller-services-surat.html","Surat"), link("seller-services-jaipur.html","Jaipur"), link("locations.html","city page"), link("services.html","services"), link("pricing.html","pricing"), link("contact.html","contact us")))
body += testimonials() + cta_band()
page("about.html", "About %s | Seller Services Team" % BRAND, "Learn about %s, an independent e-commerce seller services team helping Indian businesses sell safely and profitably on online marketplaces." % BRAND,
 "about budget bazaar, ecommerce seller support team India, marketplace consultants", body, "0.6")

# ---------------- FAQ ----------------
body = hero("Frequently asked questions", "Straight answers about our services, pricing, accounts and how we work with sellers.", cta=False, kicker="FAQ")
body += crumbs([("", "FAQ")])
body += wrap('<div class="mx-auto max-w-3xl space-y-3">%s</div><p class="mx-auto mt-8 max-w-3xl">Still have questions? %s, check our %s or read about %s.</p>' % (faq_list(FAQS), link("contact.html","Contact us"), link("pricing.html","pricing"), link("about.html","our team")))
body += cta_band()
page("faq.html", "E-commerce Seller Services FAQ | %s" % BRAND, "Answers to common questions about marketplace account setup, listings, GST help, ads, pricing and how %s works with Indian sellers." % BRAND,
 "ecommerce seller FAQ, marketplace seller questions, Amazon seller help, Flipkart seller FAQ", body, "0.6", schema=faq_schema(FAQS))

# ---------------- LOCATIONS HUB ----------------
body = hero("E-commerce seller services across India", "Local insight for India's biggest manufacturing, trading and D2C hubs, with remote support wherever you sell from.", cta=False, kicker="Cities")
body += crumbs([("", "Cities")])
body += wrap('<div class="grid gap-6 sm:grid-cols-2 lg:grid-cols-3">%s</div><p class="mt-10 max-w-3xl text-slate-700">Do not see your city? We work with sellers across India. %s and tell us where you are based. You can also explore our %s.</p>' % (
    "".join('<article class="rounded-2xl bg-white p-6 shadow-sm ring-1 ring-slate-200"><h2 class="text-xl font-extrabold"><a class="hover:text-indigo-700" href="seller-services-%s.html">Seller services in %s</a></h2><p class="mt-1 text-sm font-semibold text-amber-600">%s</p><p class="mt-3 text-slate-600">%s</p><a class="mt-4 inline-block font-bold text-indigo-700" href="seller-services-%s.html">See %s page &rarr;</a></article>' % (c["slug"], c["name"], e(c["state"]), e(c["opp"].split(". ")[0] + "."), c["slug"], c["name"]) for c in CITIES),
    link("contact.html","Contact us"), link("services.html","full service list")))
body += cta_band()
page("locations.html", "Seller Services by City in India | %s" % BRAND, "Find %s e-commerce seller services near you: Delhi NCR, Mumbai, Bengaluru, Hyderabad, Chennai, Kolkata, Pune, Ahmedabad, Jaipur, Surat and more." % BRAND,
 "ecommerce seller services by city, marketplace seller support Delhi Mumbai Bengaluru, seller agency India cities", body, "0.8")

# ---------------- CITY PAGES ----------------
for c in CITIES:
    n = c["name"]
    near = [x for x in CITIES if x["slug"] != c["slug"]]
    i = CITIES.index(c); near = [CITIES[(i+k) % len(CITIES)] for k in (1,2,3)]
    faqs = [c["faq"], ("Do you provide services in %s remotely or in person?" % n, "Most work is done remotely so we can serve %s sellers quickly. Calls and screen-sharing sessions replace office visits." % n), ("How do I get started if I sell from %s?" % n, "Send us a message on WhatsApp or the contact form with your product category and marketplaces. We will reply with the next step.")]
    body = hero("E-commerce seller services in %s" % n, "Marketplace account setup, listings, compliance guidance and ads for sellers in %s, %s." % (n, c["state"]), kicker=c["state"])
    body += crumbs([("locations.html","Cities"),("", n)])
    body += wrap('<div class="grid gap-10 lg:grid-cols-3"><div class="prose-bb lg:col-span-2"><h2>Selling online from %s</h2><p>%s</p><h2>Popular product categories in %s</h2><ul>%s</ul><h2>A practical tip for %s sellers</h2><p>%s</p><h2>Services for %s businesses</h2><p>We support %s sellers with %s, %s, %s and more. Every plan starts with a short call and a clear scope.</p><h2>Nearby cities we also serve</h2><p>%s</p></div><aside class="h-fit rounded-2xl bg-slate-50 p-6 ring-1 ring-slate-200 lg:sticky lg:top-24"><h2 class="text-lg font-extrabold">Free consultation for %s sellers</h2><p class="mt-2 text-sm text-slate-600">Tell us what you sell and where you want to sell it.</p><a href="contact.html" class="mt-4 block rounded-xl bg-indigo-700 px-4 py-3 text-center font-bold text-white">Request a quote</a><a data-only="wa" data-wa data-wa-text="Hello, I sell from %s and need help with marketplace selling." href="#" class="mt-3 block rounded-xl bg-green-500 px-4 py-3 text-center font-bold text-white">WhatsApp</a></aside></div>' % (
        n, e(c["opp"]), n, "".join("<li>%s</li>" % e(x) for x in c["cats"]), n, e(c["tip"]), n, n,
        link("seller-account-setup.html","account setup"), link("product-listing-catalog.html","catalogue management"), link("marketplace-ads-growth.html","advertising"),
        " &bull; ".join(link("seller-services-%s.html" % x["slug"], x["name"]) for x in near) + " &bull; " + link("locations.html","all cities"), n, n))
    body += '<section class="bg-slate-50 py-14"><div class="mx-auto max-w-4xl px-4">%s<div class="mt-6 space-y-3">%s</div></div></section>' % (h2("%s seller FAQs" % n), faq_list(faqs))
    body += lead_block("Grow your %s business online" % n) + cta_band()
    page("seller-services-%s.html" % c["slug"], "E-commerce Seller Services in %s | %s" % (n, BRAND), "Seller services in %s: marketplace account setup, product listings, GST guidance and ads for Amazon, Flipkart and Meesho sellers. Free consultation." % n,
     "ecommerce seller services %s, Amazon seller %s, Flipkart seller %s, marketplace account management %s, product listing services %s" % ((n.lower(),)*5), body, "0.7", schema=faq_schema(faqs))

# ---------------- CONTACT ----------------
body = hero("Contact %s" % BRAND, "Tell us about your products and goals. We usually respond fastest on WhatsApp.", cta=False, kicker="Contact")
body += crumbs([("", "Contact")])
body += wrap('<div class="grid gap-10 lg:grid-cols-2"><div><h2 class="text-2xl font-extrabold">Talk to us</h2><ul class="mt-6 space-y-4 text-slate-700"><li data-only="phone"><strong>Phone:</strong> <a class="text-indigo-700 underline" data-tel data-phone href="tel:+%s%s">%s</a></li><li data-only="wa"><strong>WhatsApp:</strong> <a class="text-indigo-700 underline" data-wa href="#">Start a chat</a></li><li data-only="email"><strong>Email:</strong> <a class="text-indigo-700 underline" data-mail data-email href="#"></a></li></ul><p class="mt-6 text-slate-600">Before you write, you may find answers in our %s or %s pages. Explore %s for local insight. Already sent an enquiry? See %s.</p></div><div data-only="forms">%s</div></div>' % (CC, PHONE, PH, link("faq.html","FAQ"), link("pricing.html","pricing"), link("locations.html","city pages"), link("thank-you.html","what happens next"), form("contact-form")))
page("contact.html", "Contact %s | Free Seller Consultation" % BRAND, "Contact %s for a free consultation on marketplace account setup, listings, ads and compliance. Call, WhatsApp or send an enquiry." % BRAND,
 "contact budget bazaar, ecommerce seller consultation, seller services enquiry, marketplace help India", body, "0.8")

# ---------------- THANK YOU ----------------
body = '<section class="hero-bg py-24 text-center text-white"><div class="mx-auto max-w-2xl px-4"><p class="text-5xl">&#10003;</p><h1 class="mt-4 text-3xl font-extrabold md:text-4xl">Thank you! We received your enquiry.</h1><p class="mt-4 text-slate-200">A member of our team will contact you shortly. For urgent questions, message us on WhatsApp.</p><div class="mt-8 flex flex-wrap justify-center gap-3"><a href="index.html" class="rounded-xl bg-amber-400 px-6 py-3 font-bold text-slate-900">Back to home</a><a href="services.html" class="rounded-xl border border-white/40 px-6 py-3 font-bold">Browse services</a><a data-only="wa" data-wa href="#" class="rounded-xl bg-green-500 px-6 py-3 font-bold">WhatsApp</a></div></div></section>'
page("thank-you.html", "Thank You | %s" % BRAND, "Thank you for contacting %s. We have received your enquiry and will respond shortly." % BRAND, "thank you, enquiry received", body, "0.1", index=False)

# ---------------- LEGAL ----------------
def legal(fn, title, desc, h1, paras, kw):
    body = hero(h1, "Last updated: November 4, 2026", cta=False)
    body += wrap('<div class="prose-bb max-w-3xl">%s<p class="mt-8">Questions? Visit our %s or return to the %s.</p></div>' % (paras, link("contact.html","contact page"), link("index.html","home page")))
    page(fn, title, desc, kw, body, "0.3")
page_p = lambda *a: "".join("<h2>%s</h2><p>%s</p>" % x for x in a)
legal("privacy.html", "Privacy Policy | %s" % BRAND, "How %s collects, uses and protects personal information submitted through this website." % BRAND, "Privacy Policy", page_p(
 ("Information we collect","When you submit a form, we receive the details you provide, such as your name, phone number, email address and message. Our hosting provider and tools may also record basic technical data such as browser type and pages visited."),
 ("How we use information","We use your details to respond to enquiries, provide quotes and deliver services you request. We do not sell your personal information."),
 ("Third-party services","Form submissions are processed by Web3Forms. Fonts and styling are loaded from Google Fonts and the Tailwind CSS CDN. These providers have their own privacy policies."),
 ("Data retention and your rights","We keep enquiry data only as long as needed to respond and provide services. You may ask us to access, correct or delete your information by contacting us."),
 ("Cookies","This website does not set advertising cookies itself. Third-party affiliate links, if shown, may set their own cookies once you click them."),
 ("Changes","We may update this policy from time to time. The date above shows the latest revision.")), "privacy policy, data protection, website privacy")
legal("terms.html", "Terms & Conditions | %s" % BRAND, "Terms and conditions for using the %s website and engaging our e-commerce seller services." % BRAND, "Terms &amp; Conditions", page_p(
 ("Use of this website","By using this website you agree to these terms. The content is for general information and may change without notice."),
 ("Services","Scope, timelines and fees for each engagement are agreed in writing before work begins. Marketplace fees and advertising spend are paid by you directly to the marketplace."),
 ("No guarantees","We do not guarantee sales, rankings, account approval or reinstatement. Marketplaces make independent decisions under their own policies."),
 ("Your responsibilities","You must provide accurate documents and information, hold the legal right to sell your products and comply with marketplace policies and applicable Indian law."),
 ("Limitation of liability","To the extent permitted by law, we are not liable for indirect or consequential losses arising from use of this website or from marketplace decisions beyond our control."),
 ("Governing law","These terms are governed by the laws of India.")), "terms and conditions, service terms")
legal("disclaimer.html", "Disclaimer | %s" % BRAND, "Disclaimer for %s: independent service provider, no marketplace affiliation, no guaranteed results, general information only." % BRAND, "Disclaimer", page_p(
 ("Independent service provider","%s is an independent business. We are not affiliated with, endorsed by or sponsored by Amazon, Flipkart, Meesho, Myntra, Nykaa, JioMart, ONDC or any other marketplace. All trademarks and names belong to their respective owners." % BRAND),
 ("No guaranteed results","Results depend on your products, pricing, competition and marketplace policies. Any examples on this site are illustrative."),
 ("Not legal, tax or financial advice","Information about GST and compliance is general guidance. Consult a qualified chartered accountant, lawyer or tax professional for advice on your situation."),
 ("Affiliate disclosure","Some links on this website may be affiliate links. If you buy through them we may earn a commission at no extra cost to you."),
 ("External links","We are not responsible for the content or practices of external websites.")), "disclaimer, affiliate disclosure, independent service provider")

# ---------------- SITEMAP / ROBOTS / 404 ----------------
sm = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + "".join('  <url><loc>%s%s</loc><lastmod>%s</lastmod><priority>%s</priority></url>\n' % (SITE_URL, "" if f == "index.html" else f, TODAY, p) for f, p in PAGES) + '</urlset>\n'
open(os.path.join(ROOT, "sitemap.xml"), "w").write(sm)
open(os.path.join(ROOT, "robots.txt"), "w").write("User-agent: *\nAllow: /\nDisallow: /thank-you.html\n\nSitemap: %ssitemap.xml\n" % SITE_URL)
open(os.path.join(ROOT, ".nojekyll"), "w").write("")
body = hero("Page not found", "The page you are looking for does not exist. Try one of these instead.", cta=False) + wrap('<div class="flex flex-wrap gap-3">%s</div>' % "".join('<a class="rounded-xl bg-indigo-700 px-5 py-3 font-bold text-white" href="%s">%s</a>' % x for x in NAV))
page("404.html", "Page Not Found | %s" % BRAND, "The requested page could not be found on the %s website." % BRAND, "404", body, index=False)
print("Built %d indexable pages" % len(PAGES))

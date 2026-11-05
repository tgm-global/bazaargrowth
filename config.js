/* ==========================================================================
   GLOBAL CONFIGURATION HUB  (edit ONLY this file)
   --------------------------------------------------------------------------
   Every page of the website reads these values, so changing one value here
   updates the brand, contact details, forms, testimonials and affiliate link
   on ALL pages at once.

   Easier way: open admin.html on your live site, fill the form, then click
   "Publish to GitHub" (or copy the generated text into this file).
   ========================================================================== */
window.SITE_CONFIG = {

  /* 1. BRAND / LOGO NAME (header, footer, page titles, meta tags, legal pages) */
  brandName: "E-commerce Bazar",
  tagline: "E-commerce seller services across India",

  /* 2. PHONE NUMBER (10 digits, no spaces) */
  phone: "8510813357",

  /* 3. WHATSAPP NUMBER (10 digits, no spaces) */
  whatsapp: "8510813357",
  countryCode: "91",

  /* 4. EMAIL ID (leave blank to hide email everywhere) */
  email: "truegainmedia@gmail.com",

  /* 5. WEB3FORMS ACCESS TOKEN (from https://web3forms.com; leave blank to send enquiries to WhatsApp instead) */
  w3formsToken: "59c94597-9ccf-4b50-9625-3e0b1d284bf8",

  /* 6. TESTIMONIALS API / KEY
        testimonialsApi: URL that returns a JSON list like [{ "name": "...", "role": "...", "text": "..." }]
        testimonialsKey: optional key, sent as an Authorization: Bearer header
        testimonialsItems: or type them here: [{ name: "Asha", role: "Seller, Surat", text: "Great service" }]
        Leave all three empty to hide the testimonials section. */
  testimonialsApi: "",
  testimonialsKey: "",
  testimonialsItems: [],

  /* 7. AFFILIATE LINK (leave blank to hide the partner offer band) */
  affiliateLink: "",
  affiliateLabel: "Recommended partner offer",

  /* 8. SOCIAL MEDIA LINKS (full https:// links; leave any blank to hide it) */
  social: {
    facebook: "",
    instagram: "",
    youtube: "",
    linkedin: "",
    twitter: "",
    telegram: ""
  },

  /* Optional modules: true = show, false = hide */
  showPhoneAndWhatsapp: true,
  showEmailFormAndTestimonials: true
};

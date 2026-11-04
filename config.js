/* ==========================================================================
   GLOBAL CONFIGURATION HUB
   Edit only this file. Every page reads these values, so changing one
   value here updates the whole website.
   ========================================================================== */
window.SITE_CONFIG = {
  // Brand shown in header, footer and forms
  brandName: "Bazar Growth",
  tagline: "E-commerce seller services across India",

  // Contact numbers: digits only, 10-digit Indian mobile numbers
  phone: "8510813357",
  whatsapp: "8510813357",
  countryCode: "91",

  // Email address. Leave blank to hide email everywhere.
  email: "",

  // Web3Forms access token (https://web3forms.com). Leave blank until you have one.
  // While blank, the enquiry form opens WhatsApp with the message pre-filled.
  w3formsToken: "",

  // Testimonials. Use "api" for a JSON URL that returns an array of
  // { name, role, text } objects, or fill "items" directly. Leave both
  // empty to hide the testimonials section.
  testimonials: {
    api: "",
    items: []
    // Example item: { name: "Client name", role: "Seller, Surat", text: "Short quote" }
  },

  // Affiliate / partner link. Leave blank to hide the partner offer band.
  affiliateLink: "",
  affiliateLabel: "Recommended partner offer",

  // Optional modules
  showPhoneAndWhatsapp: true,
  showEmailFormAndTestimonials: true
};

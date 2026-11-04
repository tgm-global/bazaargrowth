/* =====================================================================
   GLOBAL CONFIGURATION HUB  -  edit ONLY this file to update every page.
   ===================================================================== */
window.SITE_CONFIG = {
  brandName: "Budget Bazaar",          // Brand / logo name shown across all pages
  tagline: "E-commerce Seller Services",
  countryCode: "91",                    // Used for tel: and WhatsApp links
  phone: "8510813357",                  // Phone number (digits only)
  whatsapp: "8510813357",               // WhatsApp number (digits only)
  email: "",                            // Email ID - leave blank to hide email links
  w3formsToken: "",                     // W3Forms access key - get one free at https://web3forms.com
  testimonials: {
    api: "",                            // Optional JSON endpoint returning [{name, role, text, rating}]
    key: "",                            // Optional key appended as ?key=... to the API URL
    items: []                           // Or paste testimonials here: [{name:"", role:"", text:"", rating:5}]
  },
  affiliateLink: "",                    // Affiliate URL - leave blank to hide affiliate banners
  affiliateLabel: "Recommended seller tools",
  /* Feature switches */
  showPhoneWhatsapp: true,              // Phone + WhatsApp buttons in header/footer
  showEmailFormsTestimonials: true      // Email links, contact forms and testimonials
};

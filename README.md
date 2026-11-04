# Bazar Growth website (GitHub Pages)

A static, multi-page website built with HTML5, Tailwind CSS (CDN) and vanilla JavaScript.

## Publish on GitHub Pages
1. Create a GitHub repository and upload everything in this folder to the root of the repository.
2. Open Settings > Pages, choose the `main` branch and the `/ (root)` folder, then Save.
3. Replace the placeholder web address in the SEO files. Run this once in the folder
   (use your real address, for example https://bazargrowth.github.io/site):

       grep -rl "https://YOUR-USERNAME.github.io/YOUR-REPO" . | xargs sed -i 's#https://YOUR-USERNAME.github.io/YOUR-REPO#https://YOUR-ADDRESS#g'

   This updates canonical tags, sitemap.xml and robots.txt. Then submit sitemap.xml in Google Search Console.

## One place to change contact details: config.js
Brand name, phone, WhatsApp, email, Web3Forms token, testimonials and affiliate link live in `config.js`.
Every page reads it, so one edit updates the whole site.
- Email blank: email is hidden everywhere.
- Web3Forms token blank: the enquiry form opens WhatsApp with the message pre-filled. Add a token and it posts to Web3Forms, then opens thank-you.html.
- Testimonials blank: the section stays hidden. Add `items` or an `api` JSON URL to show it.
- Affiliate link blank: the partner band stays hidden.
- `showPhoneAndWhatsapp` and `showEmailFormAndTestimonials` switch those modules off completely.

Note: the brand name inside page titles and meta tags is plain HTML for SEO, so it is not changed by config.js.

## Pages
Home, About, Services (7 service pages), Cities (12 city pages), Contact, Thank you, Privacy, Terms, Disclaimer, 404, plus sitemap.xml and robots.txt.

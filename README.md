# Bazar Growth website (GitHub Pages)

A static, multi-page website built with HTML5, Tailwind CSS (CDN) and vanilla JavaScript.

## Publish on GitHub Pages
1. Create a GitHub repository and upload everything in this folder to the root of the repository.
2. Open Settings > Pages, choose the `main` branch and the `/ (root)` folder, then Save.
3. Replace the placeholder web address in the SEO files. Run this once in the folder
   (use your real address, for example https://bazargrowth.github.io/site):

       grep -rl "https://YOUR-USERNAME.github.io/YOUR-REPO" . | xargs sed -i 's#https://YOUR-USERNAME.github.io/YOUR-REPO#https://YOUR-ADDRESS#g'

   This updates canonical tags, sitemap.xml and robots.txt. Then submit sitemap.xml in Google Search Console.

## One place to change everything: config.js
Brand / logo name, phone, WhatsApp, email, Web3Forms token, testimonials API / key and affiliate link all live in `config.js`.
Every page reads it, so one edit updates the whole site, including page titles and meta tags.

Easiest way: open `admin.html` on your live site (for example https://your-address/admin.html), fill in the form
(brand, phone, WhatsApp, email, Web3Forms token, testimonials, affiliate link, social media links) and click
"Publish to GitHub". Or click "Copy config.js", open `config.js` on GitHub, click the pencil icon, paste over everything and commit.
For Publish to GitHub, create a fine-grained token (GitHub > Settings > Developer settings) for your repository only with
Contents: Read and write. The token is used once in the browser and is never stored.

- Email blank: email is hidden everywhere.
- Web3Forms token blank: the enquiry form opens WhatsApp with the message pre-filled. Add a token and it posts to Web3Forms, then opens thank-you.html.
- Testimonials empty: the section stays hidden. Fill `testimonialsApi` (and optional `testimonialsKey`) or `testimonialsItems` to show it.
- Affiliate link blank: the partner band stays hidden.
- Social links: any link left blank is hidden; filled ones show in the footer and on the Contact page.
- `showPhoneAndWhatsapp` and `showEmailFormAndTestimonials` switch those modules off completely.

## Pages
Home, About, Services (7 service pages), Cities (12 city pages), Contact, Thank you, Privacy, Terms, Disclaimer, 404, admin (Site settings, hidden from search), plus sitemap.xml and robots.txt.

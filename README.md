# The Vine Inn Cumnor – Intimate Weddings & Private Hire Website

Static website for promoting exclusive hire of The Vine Inn, Cumnor (Oxfordshire) for intimate weddings and private events.

**Live URL (after enabling Pages):**  
https://rhodirish-afk.github.io/vine-inn-cumnor-weddings/

## Features

- Fully responsive, mobile-first design
- Semantic HTML5 + Tailwind CSS (CDN – zero build step)
- Accessibility foundations (skip link, focus styles, reduced-motion support, proper labels & ARIA)
- Strong CTA: Bookings available from August 2026 · Now taking 2027 enquiries
- Sections: Hero, About, Intimate Weddings, Private Hire, Packages & Menus, Facilities + Gallery, 5-star Guest Reviews, Location (with Google Maps embed), Enquiry form
- Official venue images from vineinncumnor.com gallery
- Selected 5-star reviews from Google / OpenTable
- Suggested package pricing from project source material

## Form backend (Formspree)

The enquiry form uses Formspree.

1. Go to https://formspree.io and create a free account
2. Create a new form
3. Copy your form ID (looks like `xayzabcd` or similar)
4. In `index.html` find `YOUR_FORM_ID` and replace it with your real ID
5. Commit and push the change

Until you do this the form will not deliver messages. The page also shows the phone and email as backup.

## Enable GitHub Pages

1. Open https://github.com/rhodirish-afk/vine-inn-cumnor-weddings
2. Settings → Pages
3. Source: Deploy from a branch → Branch `main` → folder `/ (root)` → Save
4. Wait 1–2 minutes. The site will be live at the URL above.

## Design tokens

| Token | Value / Role |
|-------|--------------|
| Primary (forest) | `#1B4332` / `#2D6A4F` |
| Accent (gold) | `#C9A227` |
| Cream | `#F8F5F0` / `#FDFBF7` |
| Fonts | Playfair Display (headings) + Inter (body) |

## Local preview

```bash
npx serve .
# or open index.html directly in a browser
```

## Optional next steps

- Replace `YOUR_FORM_ID` with a real Formspree ID
- Switch to multi-page structure if preferred (current is high-converting single-page)
- Add more high-resolution photos (Parlour Room, open fire, evening events)
- Custom domain
- Tour Groups secondary page

## Venue contact

- Phone: 01865 862567  
- Email: info@vineinncumnor.com  
- Main site: https://www.vineinncumnor.com/  
- Instagram: @vineinnpub.cumnor  
- Facebook: facebook.com/vineinncumnor  

---

Built August 2026 from the complete Vine Inn Cumnor project summary.

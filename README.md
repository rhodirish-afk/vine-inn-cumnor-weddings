# The Vine Inn Cumnor – Intimate Weddings & Private Hire Website

Multi-page static site for exclusive hire of The Vine Inn, Cumnor (Oxfordshire).

**Live URL (after enabling Pages):**  
https://rhodirish-afk.github.io/vine-inn-cumnor-weddings/

## Pages

- `index.html` – Home / Hero + intro + reviews teaser
- `weddings.html` – Intimate Weddings
- `private-hire.html` – Private Hire / “Rent the Pub”
- `packages.html` – Menus & pricing (sit-down, buffet, BBQ, cocktails)
- `facilities.html` – Facilities + gallery
- `location.html` – Location, travel & Google Maps embed
- `enquire.html` – Enquiry form with Formspree (AJAX + honeypot)

## SEO

Each page has unique title, meta description, canonical URL and Open Graph tags. Home page includes JSON-LD LocalBusiness schema.

## Form (Formspree)

1. Create a free form at https://formspree.io
2. Copy your form ID
3. In `enquire.html` replace `YOUR_FORM_ID` with the real ID
4. Commit & push

The form uses AJAX (no page reload), a honeypot spam field, success/error messaging, and sets `_replyto` automatically.

## Enable GitHub Pages

Repo → Settings → Pages → Source: Deploy from branch `main` / root → Save.

## Design

- Forest green `#1B4332` / `#2D6A4F`
- Gold accent `#C9A227`
- Cream backgrounds
- Playfair Display + Inter

## Local preview

```bash
npx serve .
```

Built August 2026 from the Vine Inn Cumnor project summary.

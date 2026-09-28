# The Vine Inn, Cumnor – Pub, Weddings & Private Hire Website

Multi-page static site for The Vine Inn, Cumnor (Oxfordshire): the pub itself (winter hours, menu, events) plus weddings and exclusive hire.

**Live URL (GitHub Pages, no custom domain):**  
https://rhodirish-afk.github.io/vine-inn-cumnor-weddings/

## Pages

- `index.html` – Home / Hero + intro + reviews teaser
- `weddings.html` – Intimate Weddings
- `private-hire.html` – Private Hire / “Rent the Pub”
- `packages.html` – Menus & pricing (sit-down, buffet, BBQ, cocktails)
- `facilities.html` – Facilities + gallery
- `location.html` – Location, travel & Google Maps embed
- `enquire.html` – Wedding / private hire enquiry form (FormSubmit, captcha on, honeypot)
- `thanks.html` – Thank-you page shown after an enquiry is sent (noindex)
- `winter.html` – Winter at The Vine: opening hours (from Fri 2 Oct 2026), menu highlights, weekly events, Aunt Sally hire, downloadable poster
- `landlord.html` – From the landlord: “Still pouring after 35 days” by Rory Hanrahan
- `yarning.html` – Yarning at The Vine: winter evenings of veterans' stories by the fire (linked from the home page)

## Winter poster

The poster lives as HTML in `poster-src/poster.html`. When it changes, the **Build winter poster** GitHub Action (`.github/workflows/build-poster.yml`) renders it to `assets/poster/` (web JPG, thumbnail and print-ready A4 PDF) and commits the files. To change the poster, edit the HTML and push; you can also run the workflow by hand from the Actions tab.

## SEO

Each page has a unique title, meta description, canonical URL, Open Graph and Twitter card tags. The home page includes JSON-LD (BarOrPub) with the winter opening hours.

## Form (FormSubmit)

`enquire.html` posts straight to https://formsubmit.co/myone_ie@hotmail.co.uk (no account or form ID needed). Hidden fields set the email subject (`_subject`), a tidy table layout (`_template=table`), the redirect to `thanks.html` (`_next`), and a `_honey` spam trap. FormSubmit's captcha is left **on** (there is no `_captcha=false`). Replies go to the address the visitor types in the Email field.

The very first submission from this page triggers a one-off FormSubmit activation email to myone_ie@hotmail.co.uk. Click the link in it, or enquiries won't be delivered.

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

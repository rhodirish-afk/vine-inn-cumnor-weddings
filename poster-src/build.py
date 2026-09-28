"""Render the Winter at The Vine poster (poster-src/poster.html) to a web JPG and an A4 PDF.

Run by .github/workflows/build-poster.yml. Output goes to assets/poster/.
Photo: "The Vine Inn in Cumnor" (c) Steve Daniels, geograph.org.uk/p/2313019, CC BY-SA 2.0,
fetched from Wikimedia Commons, then cropped and colour-graded (same grade as the printed poster).
"""
import asyncio, os, urllib.request
from pathlib import Path
from PIL import Image, ImageEnhance

HERE = Path(__file__).resolve().parent
OUT = HERE.parent / "assets" / "poster"
PHOTO_URL = ("https://upload.wikimedia.org/wikipedia/commons/5/5f/"
             "The_Vine_Inn_in_Cumnor_-_geograph.org.uk_-_2313019.jpg")
UA = "VineInnPosterBuild/1.0 (https://github.com/rhodirish-afk/vine-inn-cumnor-weddings)"


def make_qr():
    import qrcode
    from qrcode.image.svg import SvgPathImage
    q = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_M, border=0, box_size=40)
    q.add_data("https://rhodirish-afk.github.io/vine-inn-cumnor-weddings/")
    q.make(fit=True)
    q.make_image(image_factory=SvgPathImage).save(str(HERE / "qr.svg"))


def fetch_and_grade_photo():
    raw = HERE / "photo_original.jpg"
    req = urllib.request.Request(PHOTO_URL, headers={"User-Agent": UA})
    raw.write_bytes(urllib.request.urlopen(req, timeout=60).read())
    im = Image.open(raw).convert("RGB")
    r, g, b = im.split()
    r = r.point(lambda v: min(255, int(v * 1.06 + 4)))
    b = b.point(lambda v: int(v * 0.88))
    im = Image.merge("RGB", (r, g, b))
    im = ImageEnhance.Contrast(im).enhance(1.08)
    im = ImageEnhance.Color(im).enhance(0.95)
    im.save(HERE / "photo_graded.jpg", quality=95)


async def render():
    from playwright.async_api import async_playwright
    OUT.mkdir(parents=True, exist_ok=True)
    shot = HERE / "shot.png"
    async with async_playwright() as p:
        kw = {"args": ["--no-sandbox"]}
        if os.environ.get("CHROME_PATH"):
            kw["executable_path"] = os.environ["CHROME_PATH"]
        browser = await p.chromium.launch(**kw)
        page = await browser.new_page(viewport={"width": 794, "height": 1123},
                                      device_scale_factor=2480 / 793.7)
        await page.goto((HERE / "poster.html").as_uri())
        await page.wait_for_load_state("networkidle")
        await page.evaluate("document.fonts.ready")
        await page.wait_for_timeout(500)
        await page.screenshot(path=str(shot), clip={"x": 0, "y": 0, "width": 793.7, "height": 1122.5})
        await page.pdf(path=str(OUT / "vine-winter-poster-A4.pdf"), width="210mm", height="297mm",
                       print_background=True, margin={"top": "0", "bottom": "0", "left": "0", "right": "0"})
        await browser.close()
    im = Image.open(shot).convert("RGB")
    if im.size != (2480, 3508):
        im = im.resize((2480, 3508), Image.LANCZOS)
    web = im.resize((1240, 1754), Image.LANCZOS)
    web.save(OUT / "vine-winter-poster.jpg", "JPEG", quality=84, optimize=True, progressive=True)
    im.resize((600, 849), Image.LANCZOS).save(OUT / "vine-winter-poster-thumb.jpg", "JPEG",
                                              quality=80, optimize=True, progressive=True)
    for f in ("shot.png", "photo_original.jpg", "photo_graded.jpg", "qr.svg"):
        (HERE / f).unlink(missing_ok=True)


if __name__ == "__main__":
    make_qr()
    fetch_and_grade_photo()
    asyncio.run(render())
    for f in sorted(OUT.iterdir()):
        print(f.name, f.stat().st_size)

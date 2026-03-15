#!/usr/bin/env python3
"""Backup all posts from tejaswin.com to markdown files with local images."""

import os
import re
import time
import hashlib
import xml.etree.ElementTree as ET
from urllib.parse import urlparse, urljoin

import requests
import bs4
import html2text

SITE = "https://tejaswin.com"
SITEMAP_URL = f"{SITE}/wp-sitemap-posts-post-1.xml"
OUTPUT_DIR = os.path.dirname(os.path.abspath(__file__))
IMAGES_DIR = os.path.join(OUTPUT_DIR, "images")
DELAY = 0.5  # seconds between requests, be polite

session = requests.Session()
session.headers.update({"User-Agent": "PersonalBackup/1.0 (owner backup)"})


def fetch(url):
    """Fetch a URL with retries."""
    for attempt in range(3):
        try:
            resp = session.get(url, timeout=30)
            resp.raise_for_status()
            return resp
        except requests.RequestException as e:
            if attempt == 2:
                print(f"  FAILED: {url} - {e}")
                return None
            time.sleep(2)


def get_post_urls():
    """Get all post URLs from the sitemap."""
    resp = fetch(SITEMAP_URL)
    if not resp:
        raise RuntimeError("Could not fetch sitemap")

    root = ET.fromstring(resp.content)
    ns = {"sm": "http://www.sitemaps.org/schemas/sitemap/0.9"}
    urls = []
    for url_elem in root.findall("sm:url", ns):
        loc = url_elem.find("sm:loc", ns)
        if loc is not None:
            urls.append(loc.text)
    return urls


def url_to_slug(url):
    """Extract date and slug from URL like /2021/03/22/bitcoin-is-forever/"""
    path = urlparse(url).path.strip("/")
    parts = path.split("/")
    if len(parts) >= 4:
        year, month, day = parts[0], parts[1], parts[2]
        slug = parts[3]
        return f"{year}-{month}-{day}", slug
    return None, path


def download_image(img_url):
    """Download an image and return the local relative path."""
    os.makedirs(IMAGES_DIR, exist_ok=True)

    parsed = urlparse(img_url)
    # Keep original filename but prefix with a short hash to avoid collisions
    original_name = os.path.basename(parsed.path)
    if not original_name:
        original_name = hashlib.md5(img_url.encode()).hexdigest()[:8] + ".jpg"

    local_path = os.path.join(IMAGES_DIR, original_name)

    # Skip if already downloaded
    if os.path.exists(local_path):
        return f"images/{original_name}"

    resp = fetch(img_url)
    if resp:
        with open(local_path, "wb") as f:
            f.write(resp.content)
        return f"images/{original_name}"
    return None


def is_local_image(url):
    """Check if image is hosted on tejaswin.com or is a relative URL."""
    if not url:
        return False
    parsed = urlparse(url)
    if not parsed.scheme:  # relative URL
        return True
    return parsed.hostname and "tejaswin.com" in parsed.hostname


def process_post(url):
    """Fetch a post, extract content, download images, return markdown."""
    resp = fetch(url)
    if not resp:
        return None, None, None

    soup = bs4.BeautifulSoup(resp.text, "html.parser")

    # Extract title
    title_elem = soup.find("h1", class_="entry-title") or soup.find("h1")
    title = title_elem.get_text(strip=True) if title_elem else "Untitled"

    # Extract date
    time_elem = soup.find("time", class_="entry-date")
    date_str = time_elem.get("datetime", "")[:10] if time_elem else ""

    # Extract content
    content_elem = soup.find("div", class_="entry-content")
    if not content_elem:
        content_elem = soup.find("article")
    if not content_elem:
        print(f"  WARNING: No content found for {url}")
        return None, None, None

    # Process images in the content
    for img in content_elem.find_all("img"):
        src = img.get("src", "")
        if not src:
            continue

        # Resolve relative URLs
        full_url = urljoin(url, src)

        if is_local_image(full_url):
            local_path = download_image(full_url)
            if local_path:
                img["src"] = local_path

        # Also handle srcset (WordPress responsive images)
        if img.get("srcset"):
            del img["srcset"]
        if img.get("sizes"):
            del img["sizes"]

    # Also handle images in <a> tags (lightbox links to full-size images)
    for a_tag in content_elem.find_all("a"):
        href = a_tag.get("href", "")
        full_href = urljoin(url, href)
        if is_local_image(full_href) and any(
            ext in href.lower()
            for ext in [".jpg", ".jpeg", ".png", ".gif", ".webp", ".svg"]
        ):
            local_path = download_image(full_href)
            if local_path:
                a_tag["href"] = local_path

    # Convert to markdown
    h = html2text.HTML2Text()
    h.body_width = 0  # no line wrapping
    h.protect_links = True
    h.images_as_html = False
    h.ignore_emphasis = False

    content_html = str(content_elem)
    markdown = h.handle(content_html)

    return title, date_str, markdown.strip()


def main():
    print("Fetching sitemap...")
    urls = get_post_urls()
    print(f"Found {len(urls)} posts\n")

    for i, url in enumerate(urls, 1):
        date_prefix, slug = url_to_slug(url)
        filename = f"{date_prefix}-{slug}.md" if date_prefix else f"{slug}.md"
        filepath = os.path.join(OUTPUT_DIR, filename)

        # Skip if already backed up
        if os.path.exists(filepath):
            print(f"[{i}/{len(urls)}] SKIP (exists): {filename}")
            continue

        print(f"[{i}/{len(urls)}] {url}")
        title, date_str, content = process_post(url)

        if content is None:
            print(f"  SKIPPED: could not extract content")
            continue

        # Write markdown with frontmatter
        with open(filepath, "w", encoding="utf-8") as f:
            f.write("---\n")
            f.write(f"title: \"{title}\"\n")
            f.write(f"date: {date_str}\n")
            f.write(f"source: {url}\n")
            f.write("---\n\n")
            f.write(content)
            f.write("\n")

        print(f"  -> {filename}")
        time.sleep(DELAY)

    print("\nDone!")


if __name__ == "__main__":
    main()

import requests
import re
from bs4 import BeautifulSoup


def analyze_website(url):
    if not url.strip():
        return {
            "HTTPS": "No Website Provided",
            "Mobile Friendly": "N/A",
            "Meta Title": "N/A",
            "Meta Description": "N/A",
            "H1 Tag": "N/A",
            "Sitemap": "N/A",
            "Robots.txt": "N/A",
            "Favicon": "N/A",
            "Contact Information": "N/A",
            "Google Maps Embedded": "N/A",
            "WhatsApp Button": "N/A"
        }

    try:
        response = requests.get(
            url,
            headers={"User-Agent": "Mozilla/5.0"},
            timeout=10
        )

        soup = BeautifulSoup(response.text, "html.parser")

        # HTTPS
        https_status = "Yes" if url.startswith("https://") else "No"

        # Mobile Friendly
        viewport = soup.find("meta", attrs={"name": "viewport"})
        mobile_status = "Yes" if viewport else "No"

        # Meta Title
        title = soup.title.get_text(strip=True) if soup.title else "Not Found"

        # Meta Description
        meta = soup.find("meta", attrs={"name": "description"})
        meta_description = (
            meta.get("content").strip()
            if meta and meta.get("content")
            else "Not Found"
        )

        # H1
        h1 = soup.find("h1")
        h1_text = h1.get_text(strip=True) if h1 else "Not Found"

        # Sitemap
        sitemap = requests.get(
            url.rstrip("/") + "/sitemap.xml",
            timeout=10
        )
        sitemap_status = "Found" if sitemap.status_code == 200 else "Not Found"

        # Robots
        robots = requests.get(
            url.rstrip("/") + "/robots.txt",
            timeout=10
        )
        robots_status = "Found" if robots.status_code == 200 else "Not Found"

        # Favicon
        favicon = soup.find("link", rel=lambda x: x and "icon" in x.lower())
        favicon_status = "Found" if favicon else "Not Found"

        # Contact Information
        page_text = soup.get_text(" ", strip=True)

        email = re.search(
            r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}",
            page_text
        )

        phone = re.search(
            r"(\+?\d[\d\s\-]{8,}\d)",
            page_text
        )

        contact_status = "Found" if email or phone else "Not Found"

        # Google Maps Embedded
        iframe = soup.find("iframe")

        maps_status = "Not Found"

        if iframe:
            src = iframe.get("src", "")
            if "google.com/maps" in src or "maps.google" in src:
                maps_status = "Found"

        # WhatsApp Button
        whatsapp_status = "Not Found"

        html = response.text.lower()

        if (
            "wa.me" in html
            or "api.whatsapp.com" in html
            or "whatsapp" in html
        ):
            whatsapp_status = "Found"

        return {
            "HTTPS": https_status,
            "Mobile Friendly": mobile_status,
            "Meta Title": title,
            "Meta Description": meta_description,
            "H1 Tag": h1_text,
            "Sitemap": sitemap_status,
            "Robots.txt": robots_status,
            "Favicon": favicon_status,
            "Contact Information": contact_status,
            "Google Maps Embedded": maps_status,
            "WhatsApp Button": whatsapp_status
        }

    except Exception as e:
        return {
            "HTTPS": "Error",
            "Mobile Friendly": "Error",
            "Meta Title": "Error",
            "Meta Description": "Error",
            "H1 Tag": "Error",
            "Sitemap": "Error",
            "Robots.txt": "Error",
            "Favicon": "Error",
            "Contact Information": "Error",
            "Google Maps Embedded": "Error",
            "WhatsApp Button": "Error",
            "Error": str(e)
        }
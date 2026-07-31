import requests
from bs4 import BeautifulSoup


def check_local_seo(url, location):
    if not url.strip():
        return {
            "Location in Title": "No Website",
            "Location in Meta Description": "No Website",
            "Location in H1": "No Website",
            "Location in Content": "No Website"
        }

    try:
        response = requests.get(url, timeout=10)
        soup = BeautifulSoup(response.text, "html.parser")

        # Get title
        title = soup.title.string if soup.title else ""

        # Get meta description
        meta = soup.find("meta", attrs={"name": "description"})
        meta_description = meta.get("content", "") if meta else ""

        # Get H1
        h1 = soup.find("h1")
        h1_text = h1.get_text(strip=True) if h1 else ""

        # Get all page text
        page_text = soup.get_text(separator=" ", strip=True)

        location = location.lower()

        return {
            "Location in Title": "Yes" if location in title.lower() else "No",
            "Location in Meta Description": "Yes" if location in meta_description.lower() else "No",
            "Location in H1": "Yes" if location in h1_text.lower() else "No",
            "Location in Content": "Yes" if location in page_text.lower() else "No"
        }

    except Exception:
        return {
            "Location in Title": "Error",
            "Location in Meta Description": "Error",
            "Location in H1": "Error",
            "Location in Content": "Error"
        }
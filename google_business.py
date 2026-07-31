from googlesearch import search


def get_google_business_data(business_name, category, location):
    query = f"{business_name} {category} {location} Google Maps"

    maps_link = "Not Found"

    try:
        for url in search(query, num_results=5):
            if "google.com/maps" in url:
                maps_link = url
                break
    except Exception:
        maps_link = "Search Failed"

    business_data = {
        "Business Name": business_name,
        "Category": category,
        "Location": location,
        "Rating": "Not Available",
        "Total Reviews": "Not Available",
        "Website": "Not Available",
        "Phone": "Not Available",
        "Address": "Not Available",
        "Business Hours": "Not Available",
        "Google Maps Link": maps_link
    }

    return business_data
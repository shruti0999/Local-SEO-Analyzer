def calculate_scores(business_data, website_data, local_seo_data):

    # -------------------------
    # Google Business Profile (40 Marks)
    # -------------------------
    google_score = 0

    if business_data["Rating"] not in ["Not Available", "", "N/A"]:
        google_score += 8

    if business_data["Total Reviews"] not in ["Not Available", "", "N/A"]:
        google_score += 8

    if business_data["Website"] not in ["Not Available", "", "N/A"]:
        google_score += 8

    if business_data["Phone"] not in ["Not Available", "", "N/A"]:
        google_score += 8

    if business_data["Address"] not in ["Not Available", "", "N/A"]:
        google_score += 4

    if business_data["Business Hours"] not in ["Not Available", "", "N/A"]:
        google_score += 4

    google_score = min(google_score, 40)

    # -------------------------
    # Website SEO (40 Marks)
    # -------------------------
    website_score = 0

    checks = [
        website_data["HTTPS"] == "Yes",
        website_data["Mobile Friendly"] == "Yes",
        website_data["Meta Title"] != "Not Found",
        website_data["Meta Description"] != "Not Found",
        website_data["H1 Tag"] != "Not Found",
        website_data["Sitemap"] == "Found",
        website_data["Robots.txt"] == "Found",
        website_data["Favicon"] == "Found",
        website_data["Contact Information"] == "Found",
        website_data["Google Maps Embedded"] == "Found",
        website_data["WhatsApp Button"] == "Found",
    ]

    website_score = round((sum(checks) / len(checks)) * 40)

    # -------------------------
    # Local SEO (20 Marks)
    # -------------------------
    local_checks = [
        local_seo_data["Location in Title"] == "Yes",
        local_seo_data["Location in Meta Description"] == "Yes",
        local_seo_data["Location in H1"] == "Yes",
        local_seo_data["Location in Content"] == "Yes",
    ]

    local_score = round((sum(local_checks) / len(local_checks)) * 20)

    # -------------------------
    # Overall Score
    # -------------------------
    overall_score = google_score + website_score + local_score

    return {
        "Google Business Profile Score (40)": google_score,
        "Website SEO Score (40)": website_score,
        "Local SEO Score (20)": local_score,
        "Overall SEO Score (100)": overall_score
    }
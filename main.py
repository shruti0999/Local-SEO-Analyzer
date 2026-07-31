from google_business import get_google_business_data
from website_analyzer import analyze_website
from seo_checker import check_local_seo
from score_calculator import calculate_scores
from report_generator import generate_excel_report


def main():
    print("===================================")
    print("        LOCAL SEO ANALYZER")
    print("===================================")

    # -----------------------------
    # User Input
    # -----------------------------
    business_name = input("Enter Business Name: ")
    category = input("Enter Business Category: ")
    location = input("Enter Location: ")
    website = input("Enter Website URL (Optional): ")

    print("\nBusiness Details")
    print("----------------------------")
    print("Business Name :", business_name)
    print("Category      :", category)
    print("Location      :", location)
    print("Website       :", website)

    # -----------------------------
    # Google Business Profile
    # -----------------------------
    business_data = get_google_business_data(
        business_name,
        category,
        location
    )

    print("\nEnter Google Business Details")
    print("(If you don't know any value, type N/A)\n")

    business_data["Rating"] = input("Google Rating: ")
    business_data["Total Reviews"] = input("Total Reviews: ")
    business_data["Website"] = input("Business Website: ")
    business_data["Phone"] = input("Phone Number: ")
    business_data["Address"] = input("Business Address: ")
    business_data["Business Hours"] = input("Business Hours: ")
    business_data["Google Maps Link"] = input("Google Maps Link: ")

    print("\nGoogle Business Profile Data")
    print("----------------------------")

    for key, value in business_data.items():
        print(f"{key}: {value}")

    # -----------------------------
    # Website Analysis
    # -----------------------------
    website_data = analyze_website(website)

    print("\nWebsite Analysis")
    print("----------------------------")

    for key, value in website_data.items():
        print(f"{key}: {value}")

    # -----------------------------
    # Local SEO Analysis
    # -----------------------------
    local_seo_data = check_local_seo(
        website,
        location
    )

    print("\nLocal SEO Analysis")
    print("----------------------------")

    for key, value in local_seo_data.items():
        print(f"{key}: {value}")

    # -----------------------------
    # SEO Score
    # -----------------------------
    scores = calculate_scores(
        business_data,
        website_data,
        local_seo_data
    )

    print("\nSEO SCORE")
    print("----------------------------")

    for key, value in scores.items():
        print(f"{key}: {value}")

    # -----------------------------
    # Generate Excel Report
    # -----------------------------
    generate_excel_report(
        business_data,
        website_data,
        local_seo_data,
        scores
    )


if __name__ == "__main__":
    main()
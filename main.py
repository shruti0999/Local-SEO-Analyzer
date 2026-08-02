from google_business import get_google_business_data
from website_analyzer import analyze_website
from seo_checker import check_local_seo
from score_calculator import calculate_scores
from report_generator import (
    generate_excel_report,
    generate_comparison_report
)

from business_comparison import compare_business_profiles


# ==========================================
# EXISTING LOCAL SEO ANALYZER
# ==========================================
def run_local_seo_analyzer():

    print("\n===================================")
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

    business_data["Rating"] = input(
        "Google Rating: "
    )

    business_data["Total Reviews"] = input(
        "Total Reviews: "
    )

    business_data["Website"] = input(
        "Business Website: "
    )

    business_data["Phone"] = input(
        "Phone Number: "
    )

    business_data["Address"] = input(
        "Business Address: "
    )

    business_data["Business Hours"] = input(
        "Business Hours: "
    )

    business_data["Google Maps Link"] = input(
        "Google Maps Link: "
    )

    print("\nGoogle Business Profile Data")
    print("----------------------------")

    for key, value in business_data.items():
        print(f"{key}: {value}")

    # -----------------------------
    # Website Analysis
    # -----------------------------
    website_data = analyze_website(
        website
    )

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


# ==========================================
# GOOGLE BUSINESS PROFILE COMPARISON
# ==========================================
def run_business_comparison():

    print("\n==========================================")
    print("   GOOGLE BUSINESS PROFILE COMPARISON")
    print("==========================================")

    # -----------------------------
    # Basic Information
    # -----------------------------
    business_name_1 = input(
        "Enter Business Name 1: "
    )

    business_name_2 = input(
        "Enter Business Name 2: "
    )

    location = input(
        "Enter Location: "
    )

    # ==========================================
    # BUSINESS 1
    # ==========================================
    print("\n==========================================")
    print("ENTER DETAILS FOR BUSINESS 1")
    print("==========================================")

    business1 = {

        "Business Name":
            business_name_1,

        "Google Rating":
            input("Google Rating: "),

        "Total Reviews":
            input("Total Reviews: "),

        "Business Category":
            input("Business Category: "),

        "Website":
            input(
                "Website (N/A if unavailable): "
            ),

        "Phone Number":
            input("Phone Number: "),

        "Business Hours":
            input("Business Hours: "),

        "Google Maps Link":
            input("Google Maps Link: "),

        "Location":
            location
    }

    # ==========================================
    # BUSINESS 2
    # ==========================================
    print("\n==========================================")
    print("ENTER DETAILS FOR BUSINESS 2")
    print("==========================================")

    business2 = {

        "Business Name":
            business_name_2,

        "Google Rating":
            input("Google Rating: "),

        "Total Reviews":
            input("Total Reviews: "),

        "Business Category":
            input("Business Category: "),

        "Website":
            input(
                "Website (N/A if unavailable): "
            ),

        "Phone Number":
            input("Phone Number: "),

        "Business Hours":
            input("Business Hours: "),

        "Google Maps Link":
            input("Google Maps Link: "),

        "Location":
            location
    }

    # ==========================================
    # COMPARE BUSINESSES
    # ==========================================
    comparison = compare_business_profiles(
        business1,
        business2
    )

    # ==========================================
    # DISPLAY COMPARISON TABLE
    # ==========================================
    print("\n")
    print("=" * 100)
    print("GOOGLE BUSINESS PROFILE COMPARISON")
    print("=" * 100)

    print(
        f"{'PROFILE DETAIL':<25}"
        f"{business_name_1:<35}"
        f"{business_name_2:<35}"
    )

    print("-" * 100)

    fields = [
        "Google Rating",
        "Total Reviews",
        "Business Category",
        "Website",
        "Phone Number",
        "Business Hours",
        "Google Maps Link"
    ]

    for field in fields:

        value1 = str(
            business1.get(
                field,
                "N/A"
            )
        )

        value2 = str(
            business2.get(
                field,
                "N/A"
            )
        )

        print(
            f"{field:<25}"
            f"{value1:<35}"
            f"{value2:<35}"
        )

    print("=" * 100)

    # ==========================================
    # PROFILE SCORES
    # ==========================================
    print("\nPROFILE SCORES")
    print("----------------------------")

    print(
        f"{business_name_1}: "
        f"{comparison['Business 1 Score']}"
    )

    print(
        f"{business_name_2}: "
        f"{comparison['Business 2 Score']}"
    )

    # ==========================================
    # SUMMARY
    # ==========================================
    print("\nCOMPARISON SUMMARY")
    print("----------------------------")

    print(
        "\nBetter Google Business Profile:"
    )

    print(
        comparison["Better Profile"]
    )

    # -----------------------------
    # Business 1 Strengths
    # -----------------------------
    print(
        f"\nKey Strengths of "
        f"{business_name_1}:"
    )

    for strength in comparison[
        "Business 1 Strengths"
    ]:

        print(
            "-",
            strength
        )

    # -----------------------------
    # Business 2 Strengths
    # -----------------------------
    print(
        f"\nKey Strengths of "
        f"{business_name_2}:"
    )

    for strength in comparison[
        "Business 2 Strengths"
    ]:

        print(
            "-",
            strength
        )

    # -----------------------------
    # Business 1 Improvements
    # -----------------------------
    print(
        f"\nAreas where "
        f"{business_name_1} can improve:"
    )

    for improvement in comparison[
        "Business 1 Improvements"
    ]:

        print(
            "-",
            improvement
        )

    # ==========================================
    # EXPORT COMPARISON TO EXCEL
    # ==========================================
    generate_comparison_report(
        business1,
        business2,
        comparison
    )

    print("\n==========================================")
    print("COMPARISON COMPLETED")
    print("==========================================")


# ==========================================
# MAIN MENU
# ==========================================
def main():

    print("\n===================================")
    print("        LOCAL SEO ANALYZER")
    print("===================================")

    print("\nSelect an option:\n")

    print("1. Analyze Local SEO")
    print("2. Compare Google Business Profiles")

    choice = input(
        "\nEnter your choice (1 or 2): "
    )

    if choice == "1":

        run_local_seo_analyzer()

    elif choice == "2":

        run_business_comparison()

    else:

        print(
            "\nInvalid choice."
        )

        print(
            "Please select 1 or 2."
        )


# ==========================================
# RUN PROGRAM
# ==========================================
if __name__ == "__main__":
    main()
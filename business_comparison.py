# --------------------------------
# Google Business Profile Comparison
# --------------------------------


def compare_business_profiles(business1, business2):

    """
    Compare two Google Business Profiles
    and generate a comparison summary.
    """

    # --------------------------------
    # Calculate Profile Scores
    # --------------------------------
    score1 = calculate_profile_score(business1)
    score2 = calculate_profile_score(business2)


    # --------------------------------
    # Decide Better Profile
    # --------------------------------
    if score1 > score2:

        better_business = business1["Business Name"]

    elif score2 > score1:

        better_business = business2["Business Name"]

    else:

        better_business = "Both businesses have similar profiles"


    # --------------------------------
    # Find Strengths
    # --------------------------------
    strengths1 = get_strengths(
        business1,
        business2
    )

    strengths2 = get_strengths(
        business2,
        business1
    )


    # --------------------------------
    # Find Improvement Areas
    # for Business 1
    # --------------------------------
    improvements = get_improvements(
        business1,
        business2
    )


    # --------------------------------
    # Final Comparison Result
    # --------------------------------
    comparison = {

        "Business 1": business1,

        "Business 2": business2,

        "Business 1 Score": score1,

        "Business 2 Score": score2,

        "Better Profile": better_business,

        "Business 1 Strengths": strengths1,

        "Business 2 Strengths": strengths2,

        "Business 1 Improvements": improvements
    }

    return comparison


# --------------------------------
# Calculate Profile Score
# --------------------------------
def calculate_profile_score(business):

    score = 0


    # Rating
    try:

        rating = float(
            business.get(
                "Google Rating",
                0
            )
        )

        score += rating * 10

    except:

        pass


    # Reviews
    try:

        reviews = int(
            str(
                business.get(
                    "Total Reviews",
                    0
                )
            ).replace(",", "")
        )

        if reviews >= 100:
            score += 20

        elif reviews >= 50:
            score += 15

        elif reviews >= 10:
            score += 10

        elif reviews > 0:
            score += 5

    except:

        pass


    # Business Category
    if is_available(
        business.get("Business Category")
    ):

        score += 5


    # Website
    if is_available(
        business.get("Website")
    ):

        score += 10


    # Phone
    if is_available(
        business.get("Phone Number")
    ):

        score += 5


    # Business Hours
    if is_available(
        business.get("Business Hours")
    ):

        score += 5


    return round(score, 2)


# --------------------------------
# Check Availability
# --------------------------------
def is_available(value):

    if value is None:
        return False

    value = str(value).strip().lower()

    unavailable_values = [
        "",
        "n/a",
        "not available",
        "none",
        "no"
    ]

    return value not in unavailable_values


# --------------------------------
# Find Strengths
# --------------------------------
def get_strengths(business, competitor):

    strengths = []


    # Rating
    try:

        rating1 = float(
            business.get(
                "Google Rating",
                0
            )
        )

        rating2 = float(
            competitor.get(
                "Google Rating",
                0
            )
        )

        if rating1 > rating2:

            strengths.append(
                "Higher Google rating"
            )

    except:

        pass


    # Reviews
    try:

        reviews1 = int(
            str(
                business.get(
                    "Total Reviews",
                    0
                )
            ).replace(",", "")
        )

        reviews2 = int(
            str(
                competitor.get(
                    "Total Reviews",
                    0
                )
            ).replace(",", "")
        )

        if reviews1 > reviews2:

            strengths.append(
                "More customer reviews"
            )

    except:

        pass


    # Website
    if is_available(
        business.get("Website")
    ):

        strengths.append(
            "Website is available"
        )


    # Phone
    if is_available(
        business.get("Phone Number")
    ):

        strengths.append(
            "Phone number is available"
        )


    # Business Hours
    if is_available(
        business.get("Business Hours")
    ):

        strengths.append(
            "Business hours are available"
        )


    if not strengths:

        strengths.append(
            "No major advantage identified"
        )


    return strengths


# --------------------------------
# Find Areas for Improvement
# --------------------------------
def get_improvements(business1, business2):

    improvements = []


    # Rating comparison
    try:

        rating1 = float(
            business1.get(
                "Google Rating",
                0
            )
        )

        rating2 = float(
            business2.get(
                "Google Rating",
                0
            )
        )

        if rating1 < rating2:

            improvements.append(
                "Improve Google rating by "
                "encouraging satisfied customers "
                "to leave positive reviews"
            )

    except:

        pass


    # Reviews comparison
    try:

        reviews1 = int(
            str(
                business1.get(
                    "Total Reviews",
                    0
                )
            ).replace(",", "")
        )

        reviews2 = int(
            str(
                business2.get(
                    "Total Reviews",
                    0
                )
            ).replace(",", "")
        )

        if reviews1 < reviews2:

            improvements.append(
                "Increase the number of "
                "customer reviews"
            )

    except:

        pass


    # Website
    if not is_available(
        business1.get("Website")
    ):

        improvements.append(
            "Add an official website "
            "to the Google Business Profile"
        )


    # Phone
    if not is_available(
        business1.get("Phone Number")
    ):

        improvements.append(
            "Add a phone number to "
            "the Google Business Profile"
        )


    # Business Hours
    if not is_available(
        business1.get("Business Hours")
    ):

        improvements.append(
            "Add complete and accurate "
            "business hours"
        )


    # Business Category
    if not is_available(
        business1.get("Business Category")
    ):

        improvements.append(
            "Add the correct business category"
        )


    if not improvements:

        improvements.append(
            "Business profile is already "
            "well optimized compared to "
            "the competitor"
        )


    return improvements
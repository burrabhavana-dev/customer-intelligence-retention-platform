def get_recommendation(segment, risk):

    recommendations = {

        ("Premium Customers", "Low"):
            "VIP rewards and premium engagement",

        ("Premium Customers", "Medium"):
            "Personalized retention offer and account review",

        ("Premium Customers", "High"):
            "Dedicated account manager and loyalty incentive",

        ("Loyal Customers", "Low"):
            "Upsell premium services",

        ("Loyal Customers", "Medium"):
            "Loyalty rewards and engagement campaign",

        ("Loyal Customers", "High"):
            "Retention outreach and contract renewal offer",

        ("Growing Customers", "Low"):
            "Monitor onboarding progress",

        ("Growing Customers", "Medium"):
            "Personalized onboarding and engagement",

        ("Growing Customers", "High"):
            "Welcome offer and proactive support outreach",

        ("At-Risk High-Value Customers", "Low"):
            "Monitor usage patterns",

        ("At-Risk High-Value Customers", "Medium"):
            "Targeted engagement campaign",

        ("At-Risk High-Value Customers", "High"):
            "Immediate retention campaign and discount"
    }

    return recommendations.get(
        (segment, risk),
        "Monitor customer behavior"
    )
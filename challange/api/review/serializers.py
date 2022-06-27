from rest_framework import serializers
from api.review.models import *


class UserSerializer(serializers.ModelSerializer):
    original_name = serializers.CharField(allow_null=True, allow_blank=True)
    original_ip = serializers.CharField(allow_null=True, allow_blank=True)
    original_email = serializers.CharField(allow_null=True, allow_blank=True)

    class Meta:
        model = CustomUser
        fields = ["id_ref", "original_name", "original_email", "original_ip"]

        extra_kwargs = {'original_email': {'required': False}}


class ReviewTitleSerializer(serializers.ModelSerializer):
    title = serializers.CharField(allow_null=True, allow_blank=True)
    review_id = serializers.IntegerField()


    class Meta:
        model = ReviewTitle
        fields = ["review_id", "title", "language"]


class ReviewTextSerializer(serializers.ModelSerializer):
    review_id = serializers.IntegerField()

    class Meta:
        model = ReviewText
        fields = ["review_id", "text", "language"]


class ReviewSerializer(serializers.ModelSerializer):


    user_id = serializers.IntegerField()
    general_review = serializers.IntegerField(allow_null=True, required=False)
    location_review = serializers.IntegerField(allow_null=True)
    service_review = serializers.IntegerField(allow_null=True)
    price_quality_review = serializers.IntegerField(allow_null=True)
    food_review = serializers.IntegerField(allow_null=True)
    room_review = serializers.IntegerField(allow_null=True)
    childFriendly_review = serializers.IntegerField(allow_null=True)
    interior_review = serializers.IntegerField(allow_null=True)
    size_review = serializers.IntegerField(allow_null=True)
    activities_review = serializers.IntegerField(allow_null=True)
    restaurants_review = serializers.IntegerField(allow_null=True)
    sanitary_state_review = serializers.IntegerField(allow_null=True)
    accessibility_review = serializers.IntegerField(allow_null=True)
    nightlife_review = serializers.IntegerField(allow_null=True)
    culture_review = serializers.IntegerField(allow_null=True)
    surrounding_review = serializers.IntegerField(allow_null=True)
    atmosphere_review = serializers.IntegerField(allow_null=True)
    novice_ski_area_review = serializers.IntegerField(allow_null=True)
    advanced_ski_area_review = serializers.IntegerField(allow_null=True)
    apres_ski_review = serializers.IntegerField(allow_null=True)
    beach_review = serializers.IntegerField(allow_null=True)
    entertainment_review = serializers.IntegerField(allow_null=True)
    environmental_review = serializers.IntegerField(allow_null=True)
    pool_review = serializers.IntegerField(allow_null=True)
    terrace_review = serializers.IntegerField(allow_null=True)
    housing_review = serializers.IntegerField(allow_null=True)
    hygiene_review = serializers.IntegerField(allow_null=True)

    class Meta:
        model = Review
        fields = [
            "user_id",
            "travel_date",
            "locale",
            "location_review",
            "service_review",
            "price_quality_review",
            "food_review",
            "room_review",
            "childFriendly_review",
            "interior_review",
            "size_review",
            "activities_review",
            "restaurants_review",
            "sanitary_state_review",
            "accessibility_review",
            "nightlife_review",
            "culture_review",
            "surrounding_review",
            "atmosphere_review",
            "novice_ski_area_review",
            "advanced_ski_area_review",
            "apres_ski_review",
            "beach_review",
            "entertainment_review",
            "environmental_review",
            "pool_review",
            "terrace_review",
            "housing_review",
            "hygiene_review",
            "traveled_with",
            "cooperation_import_partner",
            "cooperation_syndication_partner_id",
            "entry_date",
            "general_review",
            "status_published",
            "status_checked",
            "status_reason"
        ]

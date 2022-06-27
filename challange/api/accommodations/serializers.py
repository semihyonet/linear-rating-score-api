from rest_framework import serializers
from api.accommodations.models import *


class AccommodationViewSerializer(serializers.ModelSerializer):
    contact_phone = serializers.CharField(allow_null=True, allow_blank=True)
    contact_email = serializers.CharField(allow_null=True,allow_blank=True)
    contact_url = serializers.CharField(allow_null=True, allow_blank=True)
    helios_url = serializers.CharField(allow_null=True, allow_blank=True)

    class Meta:
        model = Accommodation
        fields = [
            "vrw_id",
            "fallback_name",
            "type",
            "media_id_ref",  # UUID
            "geo_coordinate_type",
            "geo_coordinate_x",
            "geo_coordinate_y",
            "stars",
            "address_street",
            "address_zipcode",
            "contact_phone",
            "contact_email",
            "contact_url",
            "helios_url",
            "is_booking_com_block_enabled",
            "is_premium_ad_link_enabled",
            "owner_id",  # UUID
            "status_published",
            "status_checked",
            "status_reason",
            "id_ref",
            "helios_id",
            "updated_date",
            "popularity_score"
        ]


class AccommodationSerializer(serializers.ModelSerializer):
    contact_phone = serializers.CharField(allow_null=True, allow_blank=True)
    contact_email = serializers.CharField(allow_null=True,allow_blank=True)
    contact_url = serializers.CharField(allow_null=True, allow_blank=True)
    helios_url = serializers.CharField(allow_null=True, allow_blank=True)

    class Meta:
        model = Accommodation
        fields = [
            "vrw_id",
            "fallback_name",
            "type",
            "media_id_ref",  # UUID
            "geo_coordinate_type",
            "geo_coordinate_x",
            "geo_coordinate_y",
            "stars",
            "address_street",
            "address_zipcode",
            "contact_phone",
            "contact_email",
            "contact_url",
            "helios_url",
            "is_booking_com_block_enabled",
            "is_premium_ad_link_enabled",
            "owner_id",  # UUID
            "status_published",
            "status_checked",
            "status_reason",
            "id_ref",
            "helios_id",
            "updated_date",
            "popularity_score"
        ]


class AccommodationFacilitySerializer(serializers.ModelSerializer):
    accommodation_id = serializers.IntegerField()
    class Meta:
        model = AccommodationFacility
        fields = ["id_ref", "accommodation_id"]


class AccommodationAwardSerializer(serializers.ModelSerializer):
    accommodation_id = serializers.IntegerField()
    class Meta:
        model = AccommodationAward
        fields = ["accommodation_id", "type", "year"]


class HeliosHistoricalUrlSerializer(serializers.ModelSerializer):
    accommodation_id = serializers.IntegerField()
    class Meta:
        model = HeliosHistoricalUrl
        fields = ["accommodation_id", "old_url", "new_url"]


class AccommodationParentsSerializer(serializers.ModelSerializer):
    accommodation_id = serializers.IntegerField()
    class Meta:
        model = AccommodationParents
        fields = ["accommodation_id", "id_ref"]


class AccommodationNamesSerializer(serializers.ModelSerializer):
    accommodation_id = serializers.IntegerField()

    class Meta:
        model = AccommodationNames
        fields = ["accommodation_id", "language", "name"]

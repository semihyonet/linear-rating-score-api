from rest_framework import serializers
from api.accommodations.models import *


class AccommodationSerializer(serializers.ModelSerializer):

    contact_phone = serializers.CharField(allow_null=True, allow_blank=True)
    contact_email = serializers.CharField(allow_null=True, allow_blank=True)
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


class AccommodationFacilityViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = AccommodationFacility
        fields = ["id_ref", "accommodation"]


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

class AccommodationNamesViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = AccommodationNames
        fields = ["accommodation", "language", "name"]


class AccommodationViewSerializer(serializers.ModelSerializer):
    accommodation_facility = AccommodationFacilityViewSerializer(many=True)
    accommodation_names = AccommodationNamesViewSerializer(many=True)
    accommodation_parents = AccommodationParentsSerializer(many=True)
    accommodation_awards = AccommodationAwardSerializer(many=True)
    accommodation_helios_historical_url = HeliosHistoricalUrlSerializer(many=True)

    contact_phone = serializers.CharField(allow_null=True, allow_blank=True)
    contact_email = serializers.CharField(allow_null=True, allow_blank=True)
    contact_url = serializers.CharField(allow_null=True, allow_blank=True)
    helios_url = serializers.CharField(allow_null=True, allow_blank=True)

    class Meta:
        model = Accommodation
        fields = [
            "accommodation_helios_historical_url",
            "accommodation_awards",
            "accommodation_parents",
            "accommodation_names",
            "accommodation_facility",
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

from django.db import models
from api.core.models import AbstractModel


# Create your models here.
class Accommodation(AbstractModel):
    id_ref = models.CharField(max_length=60)

    vrw_id = models.PositiveIntegerField()
    fallback_name = models.CharField(max_length=128)
    type = models.CharField(max_length=16)  # Q:What kinds of Types there are? TODO: Change it to ENUM

    media_id_ref = models.CharField(max_length=128)  # UUID

    # Optimal representation of GEO MODELS are PostGIS
    geo_coordinate_type = models.CharField(max_length=16)
    geo_coordinate_x = models.FloatField()
    geo_coordinate_y = models.FloatField()

    stars = models.PositiveSmallIntegerField()

    address_street = models.CharField(max_length=128)
    address_zipcode = models.CharField(max_length=16)

    contact_phone = models.CharField(max_length=32)
    contact_email = models.CharField(max_length=128)
    contact_url = models.CharField(max_length=128)

    helios_url = models.CharField(max_length=128)

    is_booking_com_block_enabled = models.BooleanField(default=False)
    is_premium_ad_link_enabled = models.BooleanField(default=False)

    owner_id = models.CharField(max_length=128)  # UUID

    status_published = models.BooleanField(default=False)
    status_checked = models.BooleanField(default=False)
    status_reason = models.CharField(max_length=128)

    helios_id = models.PositiveBigIntegerField()

    updated_date = models.DateTimeField()

    popularity_score = models.FloatField(default=0)


class AccommodationFacility(AbstractModel):
    id_ref = models.CharField(max_length=128)
    accommodation = models.ForeignKey(Accommodation, on_delete=models.CASCADE, related_name="accommodation_facility")


class AccommodationAward(AbstractModel):
    award_types = (("w", "winner"), ("r", "recommended"))

    accommodation = models.ForeignKey(Accommodation, on_delete=models.CASCADE, related_name="accommodation_awards")
    type = models.CharField(choices=award_types, max_length=32)
    year = models.IntegerField(null=True)


class HeliosHistoricalUrl(AbstractModel):
    accommodation = models.ForeignKey(Accommodation, on_delete=models.CASCADE,
                                      related_name="accommodation_helios_historical_url")

    old_url = models.CharField(max_length=128)
    new_url = models.CharField(max_length=128)


class AccommodationParents(AbstractModel):
    accommodation = models.ForeignKey(Accommodation, on_delete=models.CASCADE, related_name="accommodation_parents")

    id_ref = models.CharField(max_length=63)


class AccommodationNames(AbstractModel):
    accommodation = models.ForeignKey(Accommodation, on_delete=models.CASCADE, related_name="accommodation_names")

    language = models.CharField(max_length=16)

    name = models.CharField(max_length=128)

from django.db import models


# Create your models here.
class Accommodation(models.Model):
    vrw_id = models.PositiveIntegerField()
    fallback_name = models.CharField(max_length=64)
    type = models.CharField(max_length=16)  # Q:What kinds of Types there are? TODO: Change it to ENUM

    media_id_ref = models.CharField(max_length=64)  # UUID

    # Optimal representation of GEO MODELS are PostGIS
    geo_coordinate_type = models.CharField(max_length=16)
    geo_coordinate_x = models.FloatField()
    geo_coordinate_y = models.FloatField()

    stars = models.PositiveSmallIntegerField()

    address_street = models.CharField(max_length=32)
    address_zipcode = models.CharField(max_length=16)

    contact_phone = models.CharField(max_length=16)
    contact_email = models.CharField(max_length=32)
    contact_url = models.CharField(max_length=32)

    heliosUrl = models.CharField(max_length=64)

    is_booking_com_block_enabled = models.BooleanField(default=False)
    is_premium_ad_link_enabled = models.BooleanField(default=False)

    owner_id = models.CharField(max_length=64)  # UUID

    status_published = models.BooleanField(default=False)
    status_checked = models.BooleanField(default=False)
    status_reason = models.CharField(max_length=32)
    id_ref = models.CharField(max_length=32)

    helios_id = models.PositiveBigIntegerField()

    updated_date = models.DateTimeField()

    popularity_score = models.FloatField(default=0)


class AccommodationFacility(models.Model):
    id_ref = models.CharField(max_length=32)
    accommodation = models.ForeignKey(Accommodation, on_delete=models.CASCADE)


class AccommodationAward(models.Model):
    awardTypes = (("w", "winner"), ("r", "recommended"))


    accommodation = models.ForeignKey(Accommodation, on_delete=models.CASCADE)
    type = models.CharField(choices=awardTypes, max_length=32)
    date = models.DateTimeField()


class HeliosHistoricalUrl(models.Model):
    accommodation = models.ForeignKey(Accommodation, on_delete=models.CASCADE)

    old_url = models.CharField(max_length=64)
    new_url = models.CharField(max_length=64)


class AccommodationParents(models.Model):
    accommodation = models.ForeignKey(Accommodation, on_delete=models.CASCADE)

    id_ref = models.CharField(max_length=32)


class AccommodationNames(models.Model):
    accommodation = models.ForeignKey(Accommodation, on_delete=models.CASCADE)

    language = models.CharField(max_length=16)

    name = models.CharField(max_length=128)

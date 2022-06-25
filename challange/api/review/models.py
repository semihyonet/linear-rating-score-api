from django.db import models


# Create your models here.

class User(models.Model):
    id_ref = models.CharField(max_length=32)
    original_name = models.CharField(max_length=64)
    original_email = models.EmailField(64)
    original_ip = models.CharField(max_length=32)


class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    travel_date = models.DateTimeField()
    locale = models.CharField(max_length=8)

    location_review = models.SmallIntegerField(null=True) # TODO SMALL INTEGER FIELDS SHOULD HAVE 5 AS MAX
    service_review = models.SmallIntegerField(null=True)
    priceQuality_review = models.SmallIntegerField(null=True)
    food_review = models.SmallIntegerField(null=True)
    room_review = models.SmallIntegerField(null=True)
    childFriendly_review = models.SmallIntegerField(null=True)
    interior_review = models.SmallIntegerField(null=True)
    size_review = models.SmallIntegerField(null=True)
    activities_review = models.SmallIntegerField(null=True)
    restaurants_review = models.SmallIntegerField(null=True)
    sanitaryState_review = models.SmallIntegerField(null=True)
    accessibility_review = models.SmallIntegerField(null=True)
    nightlife_review = models.SmallIntegerField(null=True)
    culture_review = models.SmallIntegerField(null=True)
    surrounding_review = models.SmallIntegerField(null=True)
    atmosphere_review = models.SmallIntegerField(null=True)
    noviceSkiArea_review = models.SmallIntegerField(null=True)
    advancedSkiArea_review = models.SmallIntegerField(null=True)
    apresSki_review = models.SmallIntegerField(null=True)
    beach_review = models.SmallIntegerField(null=True)
    entertainment_review = models.SmallIntegerField(null=True)
    environmental_review = models.SmallIntegerField(null=True)
    pool_review = models.SmallIntegerField(null=True)
    terrace_review = models.SmallIntegerField(null=True)
    housing_review = models.SmallIntegerField(null=True)
    hygiene_review = models.SmallIntegerField(null=True)

    traveled_with = models.CharField(max_length=31)

    cooperation_import_partner = models.CharField(max_length=31)
    cooperation_syndication_partner_id = models.CharField(max_length=31)

    entry_date = models.DateTimeField()


class ReviewTitle(models.Model):
    review = models.ForeignKey(Review, on_delete=models.CASCADE)
    title = models.TextField()
    language = models.CharField(max_length=8)
    # TODO Adding a user relationship to this table might be needed


class ReviewText(models.Model):
    review = models.ForeignKey(Review, on_delete=models.CASCADE)
    text = models.TextField()
    language = models.CharField(max_length=8)


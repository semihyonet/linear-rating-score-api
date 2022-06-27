from django.db import models
from api.accommodations.models import Accommodation
from api.core.models import AbstractModel


# Create your models here.


class CustomUser(AbstractModel):
    id_ref = models.CharField(max_length=64)
    original_name = models.CharField(max_length=64)
    original_email = models.EmailField(max_length=254, null=True)
    original_ip = models.CharField(max_length=32)


class Review(AbstractModel):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="user")
    accommodation = models.ForeignKey(Accommodation, on_delete=models.CASCADE, related_name="accommodation_user")

    travel_date = models.DateTimeField()
    locale = models.CharField(max_length=8)

    general_review = models.PositiveSmallIntegerField(null=True,
                                                      blank=True)  # TODO SMALL INTEGER FIELDS SHOULD HAVE 5 AS MAX

    location_review = models.PositiveSmallIntegerField(null=True)  # TODO SMALL INTEGER FIELDS SHOULD HAVE 5 AS MAX
    service_review = models.PositiveSmallIntegerField(null=True)
    price_quality_review = models.PositiveSmallIntegerField(null=True)
    food_review = models.PositiveSmallIntegerField(null=True)
    room_review = models.PositiveSmallIntegerField(null=True)
    childFriendly_review = models.PositiveSmallIntegerField(null=True)
    interior_review = models.PositiveSmallIntegerField(null=True)
    size_review = models.PositiveSmallIntegerField(null=True)
    activities_review = models.PositiveSmallIntegerField(null=True)
    restaurants_review = models.PositiveSmallIntegerField(null=True)
    sanitary_state_review = models.PositiveSmallIntegerField(null=True)
    accessibility_review = models.PositiveSmallIntegerField(null=True)
    nightlife_review = models.PositiveSmallIntegerField(null=True)
    culture_review = models.PositiveSmallIntegerField(null=True)
    surrounding_review = models.PositiveSmallIntegerField(null=True)
    atmosphere_review = models.PositiveSmallIntegerField(null=True)
    novice_ski_area_review = models.PositiveSmallIntegerField(null=True)
    advanced_ski_area_review = models.PositiveSmallIntegerField(null=True)
    apres_ski_review = models.PositiveSmallIntegerField(null=True)
    beach_review = models.PositiveSmallIntegerField(null=True)
    entertainment_review = models.PositiveSmallIntegerField(null=True)
    environmental_review = models.PositiveSmallIntegerField(null=True)
    pool_review = models.PositiveSmallIntegerField(null=True)
    terrace_review = models.PositiveSmallIntegerField(null=True)
    housing_review = models.PositiveSmallIntegerField(null=True)
    hygiene_review = models.PositiveSmallIntegerField(null=True)

    traveled_with = models.CharField(max_length=31, null=True, blank=True)

    cooperation_import_partner = models.CharField(max_length=31)
    cooperation_syndication_partner_id = models.CharField(max_length=64)

    entry_date = models.DateTimeField()

    status_published = models.BooleanField(default=False)
    status_checked = models.BooleanField(default=False)
    status_reason = models.TextField(null=True)


class ReviewTitle(AbstractModel):
    review = models.ForeignKey(Review, on_delete=models.CASCADE, related_name="review_title")
    title = models.TextField()
    language = models.CharField(max_length=8)
    # TODO Adding a user relationship to this table might be needed


class ReviewText(AbstractModel):
    review = models.ForeignKey(Review, on_delete=models.CASCADE, related_name="review_text")
    text = models.TextField()
    language = models.CharField(max_length=8)


# TODO: Morph relationship with Review and Accommodation
class ReviewParent(AbstractModel):
    id_ref = models.CharField(max_length=64)
    review = models.ForeignKey(Review, on_delete=models.CASCADE, related_name="review_parent")

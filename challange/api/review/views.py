from api.core.views import AbstractViewClass
from api.accommodations.models import Accommodation
from api.review.models import Review
from api.review.serializers import ReviewViewSerializer
from rest_framework.views import  Response


# Create your views here.

class ReviewListApi(AbstractViewClass):
    def get(self, request,accommodation_id_ref, format=None):

        accommodation = Accommodation.objects.filter(id_ref=accommodation_id_ref)[0]

        reviews = Review.objects.filter(accommodation_id=accommodation.id)

        reviews = ReviewViewSerializer(data=reviews, many=True)
        reviews.is_valid()
        return Response(reviews.data)

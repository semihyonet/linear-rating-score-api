from api.core.views import AbstractViewClass
from api.accommodations.models import Accommodation
from api.review.models import Review
from api.review.serializers import ReviewViewSerializer
from rest_framework import generics
from rest_framework.views import Response
from rating_calculator import initator

from rest_framework.permissions import AllowAny
from rest_framework.pagination import PageNumberPagination

from django.db.models import ObjectDoesNotExist


class ReviewShowApi(AbstractViewClass):
    def get(self, request, review_id_ref, format=None):
        try:
            review = Review.objects.filter(id_ref=review_id_ref)
        except ObjectDoesNotExist as e:
            return self.with_error("Error")

        if len(review) == 0:
            return self.with_error("Accommodation couldn't be found. Please provide a valid id.")

        reviews = ReviewViewSerializer(review[0])

        return Response(reviews.data)


class ReviewListAPIView(generics.ListAPIView):
    queryset = Review.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = ReviewViewSerializer
    pagination_class = PageNumberPagination

    def get_queryset(self):
        accommodation = Accommodation.objects.filter(id_ref=self.kwargs["accommodation_id_ref"])

        if len(accommodation) == 0:
            raise Exception("Accommodation couldn't be found. Please provide a valid id.")

        return Review.objects.filter(accommodation_id=accommodation[0].id)


class CalculateAccommodationRatingsApi(AbstractViewClass):
    def get(self, request, accommodation_id_ref, format=None):
        accommodation = Accommodation.objects.filter(id_ref=accommodation_id_ref)

        if len(accommodation) == 0:
            return self.with_error("Accommodation couldn't be found. Please provide a valid id.")


        return self.with_data(initator.calculate_reviews_job(accommodation[0].id)[accommodation[0].id])

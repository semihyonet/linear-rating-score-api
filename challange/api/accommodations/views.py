from rest_framework import views, generics
from django.http import HttpResponse, JsonResponse
from api.core.views import AbstractViewClass
from api.accommodations.serializers import *
from rest_framework.permissions import AllowAny
from rest_framework.pagination import PageNumberPagination

def index(request):
    accommodation = Accommodation.objects.all()

    return JsonResponse(AccommodationViewSerializer(accommodation).data)


class AccommodationListAPIView(generics.ListAPIView):
    queryset = Accommodation.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = AccommodationSerializer
    pagination_class = PageNumberPagination





class AccommodationShow(AbstractViewClass):
    def get(self, request, id_ref, format=None):
        accommodation = Accommodation.objects.filter(id_ref=id_ref)

        accommodation_view_serializer = AccommodationViewSerializer(accommodation, many=True, ).data

        if len(accommodation_view_serializer) == 0:
            return self.with_error("Accommodation couldn't be found. Please provide a valid id.")

        return self.with_data(accommodation_view_serializer[0])

from rest_framework import views
from django.http import HttpResponse, JsonResponse
from api.accommodations.models import *
from api.accommodations.serializers import *

from django.http import HttpResponse


def index(request, id_ref):
    accommodation = Accommodation.objects.filter(id_ref=id_ref)

    return JsonResponse(AccommodationViewSerializer(accommodation, many=True, ).data, safe=False)


class AccommodationIndexView(views.APIView):
    def get(self, request, format=None):
        return HttpResponse("Test Route for Index")

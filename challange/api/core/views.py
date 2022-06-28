from rest_framework.views import APIView, Response
from django.http import HttpResponse, JsonResponse


# Create your views here.

class AbstractViewClass(APIView):

    def no_content(self):
        response = HttpResponse()
        response.status_code = 204

        return response

    def with_data(self, data, code=200):
        response_data = {
            "data": data
        }
        return HttpResponse(data,status=code)


    def with_error(self, message, code=400):
        response_data = {
            "error": {
                "message": message
            }
        }
        return JsonResponse(data=response_data, status=code)

    def with_pagination(self, data, code=200):
        response_data = {
            "data": data
        }
        return Response(data, code),

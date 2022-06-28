from rest_framework.views import APIView, Response, Request
from django.http import HttpResponse, JsonResponse, HttpResponseNotFound
from api.core.models import AbstractModel
from django.core.paginator import Paginator


# Create your views here.
def page_not_found_view(request, exception):
    return HttpResponse(
        data={{"error": "Page Not Found"}},
        code=404
    )


class ORMHelper:

    def find_by_ref(self, model: AbstractModel, id_ref: str):
        try:
            return model.objects.filter(id_ref=id_ref)[0]
        except Exception as e:
            return None


class AbstractViewClass(APIView):

    def no_content(self):
        response = HttpResponse()
        response.status_code = 204

        return response

    def with_data(self, data, code=200):
        response_data = {
            "data": data
        }
        return Response(response_data, status=code)

    def with_error(self, message, code=400):
        response_data = {
            "error": {
                "message": message
            }
        }
        return JsonResponse(data=response_data, status=code)

    def with_pagination(self, data, page_number, items_per_page=25, code=200):
        paginator = Paginator(data, items_per_page)  # Show 25 contacts per page.

        return Response({"data": paginator.get_page(page_number)})

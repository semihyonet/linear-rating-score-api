from django.urls import path
from api.review import views


urlpatterns = [
    path('<slug:accommodation_id_ref>/review', views.ReviewListApi.as_view(), name='index'),
]

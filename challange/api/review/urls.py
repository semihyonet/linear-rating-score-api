from django.urls import path
from api.review import views


urlpatterns = [
    path('<slug:review_id_ref>/', views.ReviewShowApi.as_view(), name='show'),
]

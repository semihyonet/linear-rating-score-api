from django.urls import path
from api.accommodations import views as accommodation_view
from api.review import views as review_view


urlpatterns = [
    path('<slug:id_ref>/', accommodation_view.index, name='index'),

    path('<slug:accommodation_id_ref>/review', review_view.ReviewListApi.as_view(), name='index'),
]

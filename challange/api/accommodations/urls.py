from django.urls import path
from api.accommodations import views as accommodation_view
from api.review import views as review_view

urlpatterns = [
    path('', accommodation_view.AccommodationListAPIView.as_view(), name='index'),
    path('<slug:id_ref>/', accommodation_view.AccommodationShow.as_view(), name='show'),


    path('<slug:accommodation_id_ref>/review', review_view.ReviewListAPIView.as_view(), name='list'),
    path('<slug:accommodation_id_ref>/calculate-reviews', review_view.CalculateAccommodationRatingsApi.as_view(), name='index'),


]

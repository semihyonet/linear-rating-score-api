from django.urls import path
from api.accommodations import views


urlpatterns = [
    path('<slug:id_ref>/', views.index, name='index'),

    path('test', views.AccommodationIndexView.as_view()),
]

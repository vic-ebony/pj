from django.urls import path
from .views import AnimalListAPIView

urlpatterns = [
    path('api/animals/', AnimalListAPIView.as_view(), name='animal_list_api'),
]

# URL for client. Example: Get User or update Review.
from django.urls import path
from .view.service_view import ServiceAPIView


urlpatterns = [
    path('apiview/service/', ServiceAPIView.as_view()),
]

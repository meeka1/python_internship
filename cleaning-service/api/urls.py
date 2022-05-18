# URL for client. Example: Get User or update Review.
from django.urls import path

from api.view.service_view import ServiceViewSet
from api.view.request_view import RequestViewSet
from api.view.requestStatus_view import RequestStatusViewSet
from api.view.user_view import UserViewSet
from api.view.roles_view import RolesViewSet
from api.view.review_view import ReviewViewSet


urlpatterns = [
    path('apiview/service/', ServiceViewSet.as_view({'get': 'list'})),
    path('api/service/<int:pk>/', ServiceViewSet.as_view({'put': 'update'})),
    path('api/request/', RequestViewSet.as_view({'get': 'list'})),
    path('api/request/<int:pk>/', RequestViewSet.as_view({'put': 'update'})),
    path('api/requestStatus/', RequestStatusViewSet.as_view({'get': 'list'})),
    path('api/requestStatus/<int:pk>/', RequestStatusViewSet.as_view({'put': 'update'})),
    path('api/user/', UserViewSet.as_view({'get': 'list'})),
    path('api/user/<int:pk>/', UserViewSet.as_view({'put': 'update'})),
    path('api/roles/', RolesViewSet.as_view({'get': 'list'})),
    path('api/roles/<int:pk>/', RolesViewSet.as_view({'put': 'update'})),
    path('api/review/', ReviewViewSet.as_view({'get': 'list'})),
    path('api/review/<int:pk>/', ReviewViewSet.as_view({'put': 'update'})),
]

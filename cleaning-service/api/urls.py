from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from api.view.service_view import ServiceViewSet
from api.view.request_view import RequestViewSet
from api.view.requestStatus_view import RequestStatusViewSet
from api.view.user_view import UserViewSet
from api.view.roles_view import RolesViewSet
from api.view.review_view import ReviewViewSet
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="ClEANING SERVICE API",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="Test License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)

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
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
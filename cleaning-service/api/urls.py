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
      title="CLEANING SERVICE API",
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
    path('api/service/', ServiceViewSet.as_view({'get': 'list'}), name='service_list'),
    path('api/service/create/', ServiceViewSet.as_view({'post': 'create'}), name='service_create'),
    path('api/service/<int:pk>/', ServiceViewSet.as_view({'get': 'retrieve'}), name='service_detail'),
    path('api/service/update/<int:pk>/', ServiceViewSet.as_view({'put': 'update'}), name='service_update'),
    path('api/service/delete/<int:pk>/', ServiceViewSet.as_view({'delete': 'destroy'}), name='service_delete'),

    path('api/order/', RequestViewSet.as_view({'get': 'list'}), name='order_list'),
    path('api/order/create/', RequestViewSet.as_view({'post': 'create'}), name='order_create'),
    path('api/order/<int:pk>/', RequestViewSet.as_view({'get': 'retrieve'}), name='order_detail'),
    path('api/order/update/<int:pk>/', RequestViewSet.as_view({'put': 'update'}), name='order_update'),
    path('api/order/delete/<int:pk>/', RequestViewSet.as_view({'delete': 'destroy'}), name='order_delete'),

    path('api/user/', UserViewSet.as_view({'get': 'list'}), name='user_list'),
    path('api/user/create/', UserViewSet.as_view({'post': 'create'}), name='user_create'),
    path('api/user/<int:pk>/', UserViewSet.as_view({'get': 'retrieve'}), name='user_detail'),
    path('api/user/update/<int:pk>/', UserViewSet.as_view({'put': 'update'}),name='user_update'),
    path('api/user/delete/<int:pk>/', UserViewSet.as_view({'delete': 'destroy'}), name='user_delete'),

    path('api/review/', ReviewViewSet.as_view({'get': 'list'}), name='review_list'),
    path('api/review/create/', ReviewViewSet.as_view({'post': 'create'}), name='review_create'),
    path('api/review/<int:pk>/', ReviewViewSet.as_view({'get': 'retrieve'}), name='review_detail'),
    path('api/review/update/<int:pk>/', ReviewViewSet.as_view({'put': 'update'}), name='review_update'),
    path('api/review/delete/<int:pk>/', ReviewViewSet.as_view({'delete': 'destroy'}), name='review_delete'),

    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
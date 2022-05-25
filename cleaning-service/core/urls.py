from django.urls import path
from core import views

urlpatterns = [
    path('', views.UserListView.as_view(), name='read'),
    path('create/', views.UserCreateView.as_view(), name='create'),
    path('<int:pk>/delete/', views.UserDeleteView.as_view(), name='delete'),
    path('<int:pk>/update/', views.UserUpdateView.as_view(), name='update'),
]

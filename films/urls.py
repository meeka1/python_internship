from django.urls import path
from . import views

app_name = 'films'

urlpatterns = [
    path('', views.FilmListView.as_view(), name='read'),
    path('create/', views.FilmCreateView.as_view(), name='create'),
    path('<int:pk>/delete/', views.FilmDeleteView.as_view(), name='delete'),
    path('<int:pk>/update/', views.FilmUpdateView.as_view(), name='update'),
]

from . import views
from django.urls import path

urlpatterns = [
    path('', views.homeView, name='home'),
    path('map/', views.map_view, name='map'),
]

from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('search/', views.search, name='search'),
    path('property/<int:id>/', views.property_detail, name='property_detail'),
]

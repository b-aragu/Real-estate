from django.urls import path
from . import views 
from .views import add_to_wishlist, remove_from_wishlist, wishlist

urlpatterns = [
    path('home/', views.home, name='home'),
    path('search/', views.search, name='search'),
    path('property/<int:id>/', views.property_detail, name='property_detail'),
    path('wishlist/add/<int:property_id>/', add_to_wishlist, name='add_to_wishlist'),
    path('wishlist/remove/<int:property_id>/', remove_from_wishlist, name='remove_from_wishlist'),
    path('wishlist/', wishlist, name='wishlist'),
    path('compare/', views.compare_properties, name='compare_properties'),
    path('property/<int:property_id>/schedule/', views.schedule_appointment, name='schedule_appointment'),
]

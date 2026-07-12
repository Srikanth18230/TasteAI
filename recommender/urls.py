from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('add/<str:food_name>/', views.add_item),
    path('remove/<str:food_name>/', views.remove_item),
    path('checkout/', views.checkout),
]
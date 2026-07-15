from django.urls import path
from . import views

urlpatterns = [
    path('', views.landing, name='landing'),
    path('menu/', views.home, name='menu'),
    path('add/<str:food_name>/', views.add_item, name='add_item'),
    path('remove/<str:food_name>/', views.remove_item, name='remove_item'),
    path('checkout/', views.checkout, name='checkout'),
]
path("login/",views.login),
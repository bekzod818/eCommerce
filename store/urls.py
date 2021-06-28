from django.urls import path
from . import views

urlpatterns = [
    path('', views.store, name='store'),
    path('card/', views.card, name='card'),
    path('checkout/', views.checkout, name='checkout')
]

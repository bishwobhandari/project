from django.contrib import admin
from django.urls import path
from propertytax import views

urlpatterns = [
    path('', views.getPropertyTax)
]

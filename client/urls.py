from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('/', views.home),
    path("serviceTable/", views.serviceTable),
    path("attenteDelais/", views.attenteDelais),
    path("selectionProd1/", views.selectionProduct1),
    path("selectionProd2/", views.selectionProduct2),
    path("selectionProd3/", views.selectionProduct3),
]

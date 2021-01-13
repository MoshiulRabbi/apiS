from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name = "home" ),
    path("bore",views.bore, name = "bore")
]

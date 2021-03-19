from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("", views.phenomena, name="phenomena"),
    path("locations", views.locations, name="locations")
]
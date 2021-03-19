from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<int:phenomena_id>/", views.PhenomenaView.as_view(), name="phenomena"),
    path("locations/", views.locations, name="locations")
]
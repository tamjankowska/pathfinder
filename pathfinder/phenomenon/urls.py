from django.urls import path
from . import views

urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("phenomenon/<int:phenomena_id>/", views.PhenomenaView.as_view(), name="phenomena"),
    path("locations/", views.LocationsView.as_view(), name="locations"),
    path("locations/<int:location_id>/", views.IndividualLocationView.as_view(), name="location")
]
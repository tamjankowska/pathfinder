from django.shortcuts import render
from .models import Phenomena, Location, NavbarItem
from django.views.generic import TemplateView
from django.http import HttpResponse

class IndexView(TemplateView):
    template_name = "phenomenon/index.html"

    def get(self, request, *args, **kwargs):
        context = {"phenomenon": Phenomena.objects.all()}
        return render(request, self.template_name, context)

class PhenomenaView(TemplateView):
    template_name = "phenomenon/phenomena.html"

    def get(self, request, phenomena_id, *args, **kwargs):
        context = {"phenomena": Phenomena.objects.get(pk=phenomena_id)}
        return render(request, self.template_name, context)
    
    def post(self, request, phenomena_id, *args, **kwargs):
        print(request.POST)
        return HttpResponse("Whatever you want")


class IndividualLocationView(TemplateView):
    template_name = "phenomenon/location.html"

    def get(self, request, location_id, *args, **kwargs):
        context = {"location": Location.objects.get(pk=location_id)}
        return render(request, self.template_name, context)

class LocationsView(TemplateView):
    template_name = "phenomenon/locations.html"

    def get(self, request, *args, **kwargs):
        context = {"locations": Location.objects.all()}
        return render(request, self.template_name, context)

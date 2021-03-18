from django.shortcuts import render
from .models import Phenomena, Location

def index(request):
    context = {"phenomenon": Phenomena.objects.all()}
    return render(request, "phenomenon/index.html", context)

def phenomena(request, phenomena_id):
    context = {"phenomena": Phenomena.objects.get(pk=phenomena_id)}
    return render(request, "phenomenon/phenomena.html", context)

def locations(request):
    context = {"locations": Location.objects.all()}
    return render(request, "phenomenon/locations.html", context)
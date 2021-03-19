from django.shortcuts import render
from .models import Phenomena, Location
from django.views.generic import TemplateView
from django.http import HttpResponse

class PhenomenaView(TemplateView):
    template_name = "phenomenon/phenomena.html"

    def get(self, request, phenomena_id, *args, **kwargs):
        context = {"phenomena": Phenomena.objects.get(pk=phenomena_id)}
        return render(request, self.template_name, context)
    
    def post(self, request, phenomena_id, *args, **kwargs):
        print(request.POST)
        return HttpResponse("Whatever you want")

def index(request):
    context = {"phenomenon": Phenomena.objects.all()}
    return render(request, "phenomenon/index.html", context)

# def phenomena(request, phenomena_id):
#     context = {"phenomena": Phenomena.objects.get(pk=phenomena_id)}
#     return render(request, "phenomenon/phenomena.html", context)

def locations(request):
    context = {"locations": Location.objects.all()}
    return render(request, "phenomenon/locations.html", context)
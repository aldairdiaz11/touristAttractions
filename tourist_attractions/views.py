from django.shortcuts import render
from .models import State, Attraction


def home(request):
    # The context is all the variables we want passed into the template.
    all_attractions = Attraction.objects.all()
    context = {"attractions": all_attractions}
    return render(request, 'touristAttractions/home.html', context)


def details(request, state_name):
    # We replace the dash with a space for later ease of use. The dash is there because of the slugify filter.
    attractions = Attraction.objects.all()
    context = {"attractions": attractions, "state_name": state_name.replace("-", " ")}
    return render(request, 'touristAttractions/details.html', context)

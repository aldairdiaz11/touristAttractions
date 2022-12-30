from django.shortcuts import render

# Create your views here.
# This is the dictionary for all the attractions
attractions = [
    {'attraction_name': 'Niagara Falls', 'state': 'New York'},
    {'attraction_name': 'Grand Canyon National Park', 'state': 'Arizona'},
    {'attraction_name': 'Mall of America', 'state': 'Minnesota'},
    {'attraction_name': 'Mount Rushmore', 'state': 'South Dakota'},
    {'attraction_name': 'Times Square', 'state': 'New York'},
    {'attraction_name': 'Walt Disney World', 'state': 'Florida'}
]


def home(request):
    # The context is all the variables we want passed into the template.
    context = {"attractions": attractions}
    return render(request, 'touristAttractions/home.html', context)


def details(request, statename):
    # We replace the dash with a space for later ease of use. The dash is there because of the slugify filter.
    context = {"attractions": attractions, "statename": statename.replace("-", " ")}
    return render(request, 'touristAttractions/details.html', context)

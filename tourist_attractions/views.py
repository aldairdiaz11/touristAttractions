from django.shortcuts import render
from .models import State, Attraction
from .forms import StateCreateForm, AttractionCreateForm
from django.views.generic import CreateView, TemplateView


class Home(TemplateView):
    # The context is all the variables we want passed into the template.
    template_name = "touristAttractions/home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context["attractions"] = Attraction.objects.all()
        context["states"] = State.objects.all()
        return context


def details(request, state_name):
    # We replace the dash with a space for later ease of use. The dash is there because of the slugify filter.
    attractions = Attraction.objects.all()
    context = {"attractions": attractions, "state_name": state_name.replace("-", " ")}
    return render(request, 'touristAttractions/details.html', context)


# Class forms
class StateCreate(CreateView):
    model = State
    form_class = StateCreateForm
    template_name = "touristAttractions/state_create_form.html"


class AttractionCreate(CreateView):
    model = Attraction
    form_class = AttractionCreateForm
    template_name = "touristAttractions/attraction_create_form.html"

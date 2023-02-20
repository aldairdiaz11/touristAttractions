from django.urls import path
from . import views

urlpatterns = [
    path("", views.Home.as_view(), name='home'),
    path("details/<statename>", views.details, name="details"),
    path("state/create", views.StateCreate.as_view(), name="state-create"),
    path("attraction/create", views.AttractionCreate.as_view(), name="attraction-create")
]
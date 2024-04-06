from django.urls import path
from . import views

urlpatterns = [
    path("", views.home),
    path("about", views.about),
    path("events", views.events),
    path("team", views.team),
    path("branches", views.branches),
    path("contact", views.contact)
]
from django.shortcuts import render
from .models import Event, Team, Branch

def home(request):
    return render(request, "cawebsite/home.html")

def about(request):
    return render(request, "cawebsite/about.html")

def events(request):
    eventInstances = Event.objects.all()
    return render(request, "cawebsite/events.html", {"eventInstances": eventInstances})

def team(request):
    teamInstances = Team.objects.all()
    return render(request, "cawebsite/team.html", {"teamInstances": teamInstances})

def branches(request):
    branchInstances = Branch.objects.all()
    return render(request, "cawebsite/branches.html", {"branchInstances": branchInstances})

def contact(request):
    return render(request, "cawebsite/contact.html")
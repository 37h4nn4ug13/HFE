import re
from django.shortcuts import render
from .models import SlideShow, Event
from django.views.generic import ListView, DetailView

# Create your views here.

def index(request):
    min = 1000
    for i in SlideShow.objects.all():
        if i.pk < min:
            min = i.pk

    context = {
        'slides': SlideShow.objects.all(),
        'min': min
    }
    return render(request, 'events/home.html', context)


class EventView(ListView):
    model = Event

class EventDetailView(DetailView):
    model = Event

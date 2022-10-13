from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from .models import Field, Observation

# Create your views here.

#Show all the fields in my farm
def index(request):
    return HttpResponse("Hello, world! You're at the farmnotes index, or 'home' page.")

def notes(request, field_id):
    field = get_object_or_404(Field, pk=field_id)
    return render(request, 'farmnotes/notes.html', {'field': field})

#View the details of a single observation
def observation(request, observation_id):
    observation = get_object_or_404(Observation, pk=observation_id)
    return render(request, 'farmnotes/{{ field.id }}/observation.html', {'observation': observation})

def index(request):
    latest_fields = Field.objects.all()
    context = {'latest_fields': latest_fields}
    return render(request, 'farmnotes/index.html', context)
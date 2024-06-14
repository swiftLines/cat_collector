from django.shortcuts import render
from django.views.generic.edit import CreateView
from .models import Cat
# Add imports
from django.http import HttpResponse

# Define the home view
def home(request):
    return render(request, 'home.html')


# Render the about view
def about(request): 
    return render(request, 'about.html')


# Render the cats_index view
def cats_index(request):
    cats = Cat.objects.all()
    return render(request, 'cats/index.html', {'cats': cats})


# Render cats_detail view
def cats_detail(request, cat_id):
    cat = Cat.objects.get(id=cat_id)
    return render(request, 'cats/detail.html', { 'cat': cat})


class CatCreate(CreateView):
    model = Cat
    fields = '__all__'


def __init__(self, name, breed, description, age):
    self.name = name
    self.breed = breed
    self.description = description
    self.age = age

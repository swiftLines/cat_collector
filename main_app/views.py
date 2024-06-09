from django.shortcuts import render
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

# Add the Cat class & list and view function below the imports

def __init__(self, name, breed, description, age):
    self.name = name
    self.breed = breed
    self.description = description
    self.age = age

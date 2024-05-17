from django.shortcuts import render

# Add imports
from django.http import HttpResponse
from main_app.models import cats

# Define the home view
def home(request):
    return HttpResponse('<h1>Hello ᓚᘏᗢ</h1>')

# Render the about view
def about(request): 
    return render(request, 'about.html')

# Render the cats_index view
def cats_index(request):
    return render(request, 'cats/index.html', {'cats': cats})

from django.urls import path
from . import views

urlpatterns = [
    # route for home page
    path('', views.home, name='home'),
    # route for about page
    path('about/', views.about, name='about'),
    # route for cats index
    path('cats/', views.cats_index, name='cats_index'),
    path('cats/<int:cat_id>/', views.cats_detail, name='cats_detail'),
    # route to show a form and create a cat
    path('cats/create/', views.CatCreate.as_view(), name='cats_create'),
]

from django.urls import path

from . import views

app_name = 'calories'

urlpatterns = [
    path('add/', views.add_meal, name='add_meal'),
    path('foods/', views.food_list, name='food_list'),
    path('history/', views.history, name='history'),
]

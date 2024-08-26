from django.urls import path
from . import views


urlpatterns = [
    path("hello", views.say_hello) # we are not passing the function, so providing function signature 
]

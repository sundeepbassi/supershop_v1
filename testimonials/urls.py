"""This file performs url matching functionality."""

from django.urls import path
from . import views


urlpatterns = [
    path('submit', views.display_testimonial_form,
         name='display_testimonial_form'),
    path('', views.display_all_testimonials, name='testimonials'),
]

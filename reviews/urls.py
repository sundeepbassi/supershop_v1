"""This file performs url matching functionality."""

from django.urls import path
from . import views


urlpatterns = [
    # Edit a product review (Example URL: /reviews/edit/15)
    path('update_product_review/<int:pk>',
         views.update_product_review.as_view(),
         name='update_product_review'),

    # Delete a product review (Example URL: /reviews/delete/15)
    path('delete_product_review/<int:pk>',
         views.delete_product_review.as_view(),
         name='delete_product_review'),
]

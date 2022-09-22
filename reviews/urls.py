"""This file performs url matching functionality."""

from django.urls import path
from . import views


urlpatterns = [
    # Edit a product review (Example URL: /reviews/edit/15)
    path('edit/<int:pk>',
         views.UpdateProductReview.as_view(),
         name='update_product_review'),

    # Delete a product review (Example URL: /reviews/delete/15)
    path('delete/<int:pk>',
         views.DeleteProductReview.as_view(),
         name='delete_product_review'),
]

"""This file performs url matching functionality."""

from django.urls import path
from . import views


# Specify all the URL pattern logic, i.e. for each different URL
# specify the action we want to take, e.g. if the URL is /about
# then we should display the about page.
urlpatterns = [
    path('', views.all_products, name='products'),
    path('<int:product_id>/', views.product_detail, name='product_detail'),
    path('add/', views.add_product, name='add_product'),
    path('edit/<int:product_id>/', views.edit_product, name='edit_product'),
    path('delete/<int:product_id>/', views.delete_product,
         name='delete_product'),
]

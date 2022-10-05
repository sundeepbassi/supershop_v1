""" The model for product reviews """

from django.db import models

# Used to generate URLs by reversing the URL patterns
from django.urls import reverse

from django.core.validators import MinLengthValidator

from django.contrib.auth.models import User

from products.models import Product

# Create your models here.


class ProductReview(models.Model):
    """ Create the model class for product reviews """
    product = models.ForeignKey(Product, on_delete=models.CASCADE,
                                related_name='product_reviews')

    # Foreign Key used because a product review can only have one author
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    # Specify a minimum product review title of 5,
    # to at least enforce a reasonable title!
    #
    # Specify a maximum review title of 200,
    # as that is all the model field can have.
    title = models.CharField(max_length=200,
                             validators=[MinLengthValidator(5)])

    # Specify a minimum product review title of 10,
    # to at least enforce a reasonable description!
    #
    # Specify a maximum review title of 1000,
    # as that is all the model field can have.
    review = models.TextField(max_length=1000,
                              help_text='Enter a review for this product',
                              validators=[MinLengthValidator(10)])

    approved = models.BooleanField(default=False)

    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        """ Ordering our product reviews by date order """
        ordering = ['-created_on']

    def __str__(self):
        """ String for representing the Model object."""
        return f"Product review of {self.product.name} by {self.author}"

    def get_absolute_url(self):
        """ Returns the URL to access a detail record for this review."""
        return reverse('book-detail', args=[str(self.id)])

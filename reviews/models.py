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

    # Foreign Key used because book can only have one author, but authors can
    # have multiple books. Author is a string rather than an object because
    # it hasn't been declared yet in the file
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    title = models.CharField(max_length=200,
                             validators=[MinLengthValidator(5)])

    review = models.TextField(max_length=1000,
                              help_text='Enter a review for this product',
                              validators=[MinLengthValidator(10)])

    approved = models.BooleanField(default=False)

    created_on = models.DateTimeField(auto_now_add=True)

    # image = models.ImageField(null=True, blank=True)

    # ManyToManyField used because genre can contain many books. Books can
    # cover many genres. Genre class has already been defined so we can specify
    # the object above.
    # genre = models.ManyToManyField(Genre,
    #                                help_text='Select a genre for this book')

    class Meta:
        """ Ordering our product reviews by date order """
        ordering = ['-created_on']

    def __str__(self):
        """ String for representing the Model object."""
        return f"Product review of {self.product.name} by {self.author}"

    def get_absolute_url(self):
        """ Returns the URL to access a detail record for this book."""
        return reverse('book-detail', args=[str(self.id)])

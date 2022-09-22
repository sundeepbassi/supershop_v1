""" Product review form functionality. """
from django import forms

from reviews.models import ProductReview


class ProductReviewForm(forms.ModelForm):
    """
    The Product Review Form allows users to add product reviews to
    the site.
    """
    class Meta:
        """ Meta class for product review form class """
        model = ProductReview
        fields = ['title', 'review']

from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):

    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return str(self.name)

    def get_friendly_name(self):
        return self.friendly_name


class Product(models.Model):
    category = models.ForeignKey('Category', null=True,
                                 blank=True, on_delete=models.SET_NULL)
    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)
    description = models.TextField()
    has_sizes = models.BooleanField(default=False, null=True, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    rating = models.DecimalField(max_digits=6,
                                 decimal_places=2, null=True, blank=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return str(self.name)


class ProductReview(models.Model):
    # Product review class
    product = models.ForeignKey(Product, on_delete=models.CASCADE,
                                related_name='product_reviews')
    author = models.ForeignKey(User, blank=False, null=False,
                               on_delete=models.CASCADE)
    title = models.CharField(max_length=250)
    body = models.TextField()
    approved = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)
    product_review_image = models.ImageField(null=True, blank=True)

    class Meta:
        """
        Ordering our posts in created order,
        the lack of '-' means in ascending order.
        """
        ordering = ['-created_on']

    def __str__(self):
        """
        Returns a string showing the author's name
        and the content of the product review.
        """
        return f"Product review of {self.product.name} by {self.author}"

class NumberOfProductReviewsForCurrentUser(models.Model):
        price = models.FloatField("Price", blank=True, null=True)
        voucher_id = models.CharField(max_length=255,blank=True, null=True)
        voucher_amount = models.IntegerField(blank=True, null=True)

        @property
        def number_of_product_reviews_for_current_user(self):
             return (self.voucher_amount/100)*self.price


# course = Course.objects.get(id=1)
# course.discounted_amount # returns the calculated discount
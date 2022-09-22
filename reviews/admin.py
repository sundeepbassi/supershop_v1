from django.contrib import admin

from .models import ProductReview

# Register your models here.


@admin.register(ProductReview)
class ProductReviewAdmin(admin.ModelAdmin):
    # ProductReviewAdmin class
    list_display = ('title', 'review', 'created_on', 'approved')
    list_filter = ('approved', 'created_on')
    search_fields = ('title', 'review')
    actions = ['approve_product_reviews']

    def approve_product_reviews(self, _request, queryset):
        # This method approves the product reviews
        queryset.update(approved=True)

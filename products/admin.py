from django.contrib import admin
from .models import Product, Category, ProductReview

# Register your models here.


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'name',
        'category',
        'price',
        'rating',
        'image',
    )

    ordering = ('sku',)


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )


@admin.register(ProductReview)
class ProductReviewAdmin(admin.ModelAdmin):
    # ProductReviewAdmin class
    list_display = ('title', 'body', 'created_on', 'approved')
    list_filter = ('approved', 'created_on')
    search_fields = ('title', 'body', 'body')
    actions = ['approve_product_reviews']

    def approve_product_reviews(self, _request, queryset):
        # This method approves the product reviews
        queryset.update(approved=True)


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
# admin.site.register(ProductReview, ProductReviewAdmin)

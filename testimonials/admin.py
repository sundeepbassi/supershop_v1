from django.contrib import admin
from .models import Testimonial


class TestimonialAdmin(admin.ModelAdmin):
    list_display = (
        'full_name',
        'location',
        'display_on_website',
        'sent_on',
        'processed',
    )
    # actions = ['display_on_website']

    def display_on_website(self, _request, queryset):
        queryset.update(approved=True)
        ordering = ('-sent_on',)


admin.site.register(Testimonial, TestimonialAdmin)

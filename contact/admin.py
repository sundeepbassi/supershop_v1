from django.contrib import admin
from .models import Contact


class ContactAdmin(admin.ModelAdmin):
    list_display = (
        'full_name',
        'email',
        'subject',
        'sent_on',
        'responded',
    )

    ordering = ('-sent_on',)


admin.site.register(Contact, ContactAdmin)

from django.contrib import admin

from .models import LostFoundItem


@admin.register(LostFoundItem)
class LostFoundItemAdmin(admin.ModelAdmin):

    list_display = (
        'item_id',
        'item_name',
        'category',
        'status',
        'location',
        'date_reported',
        'contact_name',
    )

    list_filter = (
        'status',
        'category',
    )

    search_fields = (
        'item_name',
        'description',
        'location',
        'contact_name',
        'contact_information',
    )

    ordering = (
        '-date_reported',
    )

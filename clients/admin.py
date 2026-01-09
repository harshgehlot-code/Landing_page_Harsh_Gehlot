from django.contrib import admin
from django.utils.html import format_html
from .models import Client


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ['image_preview', 'name', 'designation', 'description_preview', 'created_at', 'updated_at']
    list_filter = ['created_at', 'updated_at', 'designation']
    search_fields = ['name', 'designation', 'description']
    readonly_fields = ['image_preview', 'created_at', 'updated_at']
    list_per_page = 20
    
    def image_preview(self, obj):
        """Display image preview in list view"""
        if obj.image:
            return format_html(
                '<img src="{}" style="width: 50px; height: 50px; object-fit: cover; border-radius: 4px;" />',
                obj.image.url
            )
        return "No Image"
    image_preview.short_description = 'Image'
    
    def description_preview(self, obj):
        """Show truncated description in list view"""
        if obj.description:
            return obj.description[:100] + '...' if len(obj.description) > 100 else obj.description
        return '-'
    description_preview.short_description = 'Description'
    
    fieldsets = (
        ('Basic Information', {
            'fields': ('name', 'designation', 'description')
        }),
        ('Image', {
            'fields': ('image', 'image_preview')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )

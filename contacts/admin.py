from django.contrib import admin
from .models import Contact


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'email', 'mobile', 'city', 'created_at']
    list_filter = ['city', 'created_at', 'updated_at']
    search_fields = ['full_name', 'email', 'mobile', 'city']
    readonly_fields = ['full_name', 'email', 'mobile', 'city', 'created_at', 'updated_at']
    list_per_page = 20
    
    # Make Contact view-only (no add, change, or delete)
    def has_add_permission(self, request):
        return False
    
    def has_change_permission(self, request, obj=None):
        return False
    
    def has_delete_permission(self, request, obj=None):
        return False
    
    fieldsets = (
        ('Contact Information', {
            'fields': ('full_name', 'email', 'mobile', 'city')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )

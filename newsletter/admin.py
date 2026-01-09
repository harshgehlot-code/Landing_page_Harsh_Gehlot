from django.contrib import admin
from .models import Subscriber


@admin.register(Subscriber)
class SubscriberAdmin(admin.ModelAdmin):
    list_display = ['email', 'created_at', 'updated_at']
    list_filter = ['created_at', 'updated_at']
    search_fields = ['email']
    readonly_fields = ['email', 'created_at', 'updated_at']
    list_per_page = 20
    
    # Make Subscriber view-only (no add, change, or delete)
    def has_add_permission(self, request):
        return False
    
    def has_change_permission(self, request, obj=None):
        return False
    
    def has_delete_permission(self, request, obj=None):
        return False
    
    fieldsets = (
        ('Subscriber Information', {
            'fields': ('email',)
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )

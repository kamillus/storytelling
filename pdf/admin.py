from django.contrib import admin
from django.contrib.auth.models import User
from pdf.models import AccessCode, AccessCodeTracking

class AccessCodeAdmin(admin.ModelAdmin):
    list_display = ('user','code')
    
class AccessCodeTrackingAdmin(admin.ModelAdmin):
    list_display = ('access_code', 'date_accessed', 'action')
    
    def has_add_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False
    
admin.site.register(AccessCode, AccessCodeAdmin)
admin.site.register(AccessCodeTracking, AccessCodeTrackingAdmin)

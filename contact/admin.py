from django.contrib import admin
from contact.models import ContactMessage, CV


class ContactMessageAdmin(admin.ModelAdmin):
    fields = ['full_name', 'phone_no', 'email', 'message']
    list_display = ['full_name', 'phone_no', 'email', 'message']

    def has_add_permission(self, request):
        return False


class CVAdmin(admin.ModelAdmin):
    fields = ['name', 'email', 'cv', 'phone_no']
    list_display = ['name', 'email', 'cv', 'phone_no']


admin.site.register(ContactMessage, ContactMessageAdmin)
admin.site.register(CV, CVAdmin)

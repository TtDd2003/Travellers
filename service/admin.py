from django.contrib import admin
from .models import Service  # Import the Service model

class ServiceAdmin(admin.ModelAdmin):
    list_display = ('icon', 'title', 'description')  # Customize the admin view

admin.site.register(Service, ServiceAdmin)

# Register your models here.

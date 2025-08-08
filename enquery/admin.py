from django.contrib import admin
from .models import Enquery  # Import the Service model

class EnqueryAdmin(admin.ModelAdmin):
    display = ('name','email','phone','whatsapp_no','description','image')
admin.site.register(Enquery, EnqueryAdmin)

# Register your models here.

from django.contrib import admin
from.models import Image
class ImageAdmin(admin.ModelAdmin):
    display= ('captiom','image','experience')

admin.site.register(Image)
# Register your models here.

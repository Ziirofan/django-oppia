# oppia/av/admin.py
from django.contrib import admin
from oppia.av.models import UploadedMedia, UploadedMediaImage

class UploadedMediaAdmin(admin.ModelAdmin):
    list_display = ('file', 'created_date', 'md5', 'length')
 
class UploadedMediaImageAdmin(admin.ModelAdmin):
    list_display = ('image', 'uploaded_media', 'default_image', 'created_date')   
    
admin.site.register(UploadedMedia, UploadedMediaAdmin)  
admin.site.register(UploadedMediaImage, UploadedMediaImageAdmin)     
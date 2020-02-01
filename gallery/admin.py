from django.contrib import admin
from .models import Category,Image,Location
# Register your models here.
# class MyModelAdmin(admin.ModelAdmin):
#     class Media:
#         js = ('show-copy-btn.js',) 
admin.site.register(Category)
admin.site.register(Image)
admin.site.register(Location)

from django.contrib import admin
from .models import Category, Property, Image, Comment, Location
# Register your models here.


class CategoryAdmin (admin.ModelAdmin):
    list_display = ['id', 'name']
    search_fields = ['name']
    list_filter = ['id', 'name']

admin.site.register(Category, CategoryAdmin)
admin.site.register(Location)
admin.site.register(Property)
admin.site.register(Image)
admin.site.register(Comment)

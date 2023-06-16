from django.contrib import admin
from .models import CategoryModel
# Register your models here.
class CategoryModelAdmin(admin.ModelAdmin):
    list_display = ('id','code','name','grade','parent_id','grade','picture_url')
    fields = ('code','name','parent','picture_url','grade')



admin.site.register(CategoryModel,CategoryModelAdmin)
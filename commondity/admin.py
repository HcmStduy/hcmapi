from django.contrib import admin
from .models import CategoryModel,YgeatModel
# Register your models here.
class CategoryModelAdmin(admin.ModelAdmin):
    list_display = ('id','code','name','grade','parent_id','grade','picture_url')
    fields = ('code','name','parent','picture_url','grade')

class YgeatModelAdmin(admin.ModelAdmin):
    list_display = ('eat_img', 'eat_content', 'eat_time', 'hot')
    fields =  ('eat_img', 'eat_content', 'eat_time', 'hot')

admin.site.register(CategoryModel,CategoryModelAdmin)
admin.site.register(YgeatModel,YgeatModelAdmin)
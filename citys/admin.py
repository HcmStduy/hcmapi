from django.contrib import admin
from .models import CityModel,CityAreaModel
# Register your models here.

class CityModelAdmin(admin.ModelAdmin):
    list_display = ('city_name','city_letter','city_hot')
    fields = ('city_name','city_letter','city_hot')

class CityAreaModelAdmin(admin.ModelAdmin):
    list_display = ('cityareaname','city_id')
    fields = ('cityareaname','city_id')

admin.site.register(CityModel,CityModelAdmin)
admin.site.register(CityAreaModel,CityAreaModelAdmin)

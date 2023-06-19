from django.contrib import admin
from .models import AddressModel,DiscountModel,ActivesModel
# Register your models here.

class AddressModelAdmin(admin.ModelAdmin):
    list_display = ('address','state','user')
    fields = ('address','state','user')
class DiscountModelAdmin(admin.ModelAdmin):
    list_display = ('user_id','deduction','total_maney','datatime','time_of_validity')
    fields = ('user_id','deduction','total_maney','datatime','time_of_validity')

class ActivesModelAdmin(admin.ModelAdmin):
    list_display = ('active_name','active_url','icon')
    fields = ('active_name','active_url','icon')
admin.site.register(AddressModel,AddressModelAdmin)
admin.site.register(DiscountModel,DiscountModelAdmin)
admin.site.register(ActivesModel,ActivesModelAdmin)
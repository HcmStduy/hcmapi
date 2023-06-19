from django.contrib import admin
from .models import CartModel,OrderGoods,OrderlistModel
# Register your models here.
class CartModelAdmin(admin.ModelAdmin):
    list_display = ('user','goods','count')
    fields = ('user','goods','count')
class OrderGoodsAdmin(admin.ModelAdmin):
    list_display = ('order','goods','count')
    fields = ('order','goods','count')
class OrderlistModelAdmin(admin.ModelAdmin):
    list_display = ('user','order_time','order_statues','addr_id')
    fields = ('user','order_time','order_statues','addr_id')

admin.site.register(CartModel,CartModelAdmin)
admin.site.register(OrderGoods,OrderGoodsAdmin)
admin.site.register(OrderlistModel,OrderlistModelAdmin)
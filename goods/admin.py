from django.contrib import admin
from .models import GoodsModel,GoodsInfoModel,TagModel,GoodsImageModel
# Register your models here.

class GoodsModelAdmin(admin.ModelAdmin):
    list_display = ('goods_name','goods_code','maxcount','price','goods_hot')
    fields = ('categoryid','goods_name','goods_code','maxcount','price','goods_hot')

class  GoodsInfoModelAdmin(admin.ModelAdmin):
    list_display = ('goods_id','goods_info','sellprice','subtitle','unit','spec','video','placeoforgin')
    fields =  ('goods_id','goods_info','sellprice','subtitle','unit','spec','video','placeoforgin')

class TagModelAdmin(admin.ModelAdmin):
    list_display =('tag',)
    fields =('tag',)
class GoodsImageModelAdmin(admin.ModelAdmin):
    list_display = ('img1','goods_id')
    fields =  ('img1','goods_id')
admin.site.register(GoodsModel,GoodsModelAdmin)
admin.site.register(GoodsInfoModel,GoodsInfoModelAdmin)
admin.site.register(TagModel,TagModelAdmin)
admin.site.register(GoodsImageModel,GoodsImageModelAdmin)

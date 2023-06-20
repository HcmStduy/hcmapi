from django.db import models

# Create your models here.
from common import YGBaseModel
from commondity.models import CategoryModel

class GoodsModel(YGBaseModel):
    class Meta:
        db_table = 't_goods'
        verbose_name_plural = verbose_name = '商品表'

    categoryid = models.ManyToManyField(CategoryModel,
                                        related_name='goods_cate',
                                        db_table='t_goods_cate',
                                        verbose_name='所属分类',
                                        )
    goods_name = models.CharField(max_length=100,
                                     verbose_name='商品名')
    goods_code = models.CharField(max_length=30, verbose_name='编号')
    maxcount = models.IntegerField(verbose_name='最大购买数')
    price = models.DecimalField(verbose_name='原价',
                                        max_digits=10,
                                        decimal_places=2)
    goods_hot = models.IntegerField(verbose_name='热度')

    def __str__(self):
        return self.goods_name

class TagModel(YGBaseModel):
    class Meta:
        db_table = 't_tag'
        verbose_name_plural = verbose_name = '标签表'

    tag = models.CharField(max_length=100, verbose_name='标签')

    def __str__(self):
        return self.tag



class GoodsInfoModel(YGBaseModel):
    class Meta:
        db_table = 't_goods_info'
        verbose_name_plural = verbose_name = '商品详情表'

    goods_id = models.OneToOneField(GoodsModel,
                                    on_delete=models.CASCADE,
                                    related_name='info',
                                    verbose_name='商品id')
    goods_info = models.CharField(max_length=200,
                                     verbose_name='商品说明')
    sellprice = models.FloatField(verbose_name='折扣价')
    subtitle = models.CharField(max_length=200,
                                verbose_name='副标题')
    promotiontag = models.ManyToManyField(TagModel,
                                          db_table='tag_goods_info',
                                          related_name='goods_tag',
                                          verbose_name='标签名')
    unit = models.CharField(max_length=20,
                            verbose_name='规格')
    spec = models.CharField(max_length=30,
                            verbose_name='单位/规格')
    video = models.CharField(max_length=200,
                             verbose_name='视频',
                             null=True,
                             blank=True)
    placeoforgin = models.CharField(max_length=100,
                                    verbose_name='产地')

    def __str__(self):
        return self.goods_id.goods_name


class GoodsImageModel(YGBaseModel):
    class Meta:
        db_table = 't_goods_image'
        verbose_name_plural = verbose_name = '商品图片'

    img1 = models.CharField(max_length=200,
                            verbose_name='商品图片')

    goods_id = models.ForeignKey(GoodsModel,
                                 on_delete=models.SET_NULL,
                                 related_name='image',
                                 verbose_name='商品id',
                                 null=True,
                                 blank=True)
    # @property
    # def goodname(self):
    #     return self.goods_id.goods_name

    def __str__(self):
        return self.goods_id.goods_name



# 轮播图表
class SiwapModel(YGBaseModel):
    class Meta:
        db_table = 't_siwap'
        verbose_name_plural = verbose_name = '轮播图表'

    active_id = models.OneToOneField('address.ActivesModel',
                                     on_delete=models.CASCADE,
                                     related_name='actives',
                                     verbose_name='活动表')
    active_img = models.CharField(max_length=200,
                                  verbose_name='活动大图')

    def __str__(self):
        return self.active_id.active_name
from django.db import models
from common import YGBaseModel


# Create your models here.
class CategoryModel(YGBaseModel):
    code = models.CharField(max_length=20, verbose_name='编码')
    name = models.CharField(max_length=20, verbose_name='名称')
    grade = models.IntegerField(default=1, verbose_name='等级')
    parent = models.ForeignKey('self', on_delete=models.CASCADE, verbose_name='父类', blank=True, null=True)
    picture_url = models.CharField(max_length=200, verbose_name='图片路径', blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 't_category'
        verbose_name = '分类表'
        verbose_name_plural = verbose_name


class YgeatModel(YGBaseModel):
    eat_img = models.CharField(max_length=200, verbose_name='图片地址')
    eat_content = models.CharField(max_length=50, verbose_name='描述')
    eat_time = models.CharField(max_length=20, verbose_name='时间')
    hot = models.IntegerField(verbose_name='热度')

    class Meta:
        db_table = 't_ygeat'
        verbose_name_plural = verbose_name = '吃喝玩乐'

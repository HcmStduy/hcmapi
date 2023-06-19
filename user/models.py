import uuid

from django.db import models


from common import  YGBaseModel

# Create your models here.

class AppUserManager(models.Manager):
    def get_queryset(self):
        return super(AppUserManager, self).get_queryset().filter(~models.Q(status=2))

def user_directory_path(instance, filename):
    ext = filename.split('.')[-1]
    filename = f'{instance.id}.{ext}'
    return f"users/{filename}"

class AppUser(YGBaseModel):
    name = models.CharField(max_length=20
                            ,verbose_name='用户名')
    anth_key = models.CharField(max_length=100,
                                verbose_name='口令')
    phone = models.CharField(max_length=11,verbose_name='手机号')
    email = models.CharField(max_length=50,verbose_name='邮件')
    create_time = models.DateField(verbose_name='注册时间',auto_now_add=True)
    status = models.IntegerField(verbose_name='状态',default=0,choices=((2,'已注销'),(1,"已激活"),
                                                            (0,"未激活")))
    img1 = models.ImageField(max_length=100,verbose_name='头像',blank=True,null=True,
                             upload_to=user_directory_path
                             )
    objects = AppUserManager()

    def __str__(self):
        return self.name

    class Meta:
        db_table ='t_app_user'
        verbose_name ='用户表'
        verbose_name_plural =verbose_name

class CommentsModel(YGBaseModel):
    order_id = models.ForeignKey('cartlist.OrderlistModel',
                                 verbose_name='订单ID',
                                 on_delete=models.CASCADE,
                                 related_name='good_comment')
    comments = models.TextField(max_length=500,
                                verbose_name='评论内容')
    comment_time = models.CharField(max_length=30,
                                    verbose_name='评论时间')

    def __str__(self):
        return self.comment_time

    class Meta:
        db_table = 't_comments'
        verbose_name_plural = verbose_name = '评论表'

class NavModel(YGBaseModel):
    nav_child_id = models.ForeignKey('commondity.CategoryModel',
                                     verbose_name='分类ID',
                                     on_delete=models.CASCADE,
                                     related_name='nav',
                                     blank=True,
                                     null=True)
    actives_id = models.ForeignKey('address.ActivesModel',
                                   verbose_name='活动ID',
                                   on_delete=models.CASCADE,
                                   related_name='Navs',
                                   blank=True,
                                   null=True)
    name = models.CharField(max_length=20,
                            verbose_name='名称')
    image = models.CharField(max_length=200,
                             verbose_name='导航图片')

    def __str__(self):
        return self.name

    class Meta:
        db_table = 't_nav'
        verbose_name_plural = verbose_name = '导航表'
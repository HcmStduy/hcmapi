from django.contrib import admin
from .models import AppUser,CommentsModel,NavModel
from .forms import AppUserForms
# Register your models here.

class AppUserAdmin(admin.ModelAdmin):
    list_display = ('id','name','anth_key','phone','email','create_time','status','img1')
    fields = ('name','anth_key','phone','email','status','img1')
    form = AppUserForms

class CommentsModelAdmin(admin.ModelAdmin):
    list_display = ('order_id','comments','comment_time')
    fields = ('order_id','comments','comment_time')

class NavModelAdmin(admin.ModelAdmin):
    list_display = ('nav_child_id','actives_id','name','image')
    fields = ('nav_child_id','actives_id','name','image')

admin.site.register(AppUser,AppUserAdmin)
admin.site.register(CommentsModel,CommentsModelAdmin)
admin.site.register(NavModel,NavModelAdmin)

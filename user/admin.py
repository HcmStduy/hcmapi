from django.contrib import admin
from .models import AppUser
from .forms import AppUserForms
# Register your models here.

class AppUserAdmin(admin.ModelAdmin):
    list_display = ('id','name','anth_key','phone','email','create_time','status','img1')
    fields = ('name','anth_key','phone','email','status','img1')
    form = AppUserForms


admin.site.register(AppUser,AppUserAdmin)
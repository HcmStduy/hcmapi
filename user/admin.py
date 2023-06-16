from django.contrib import admin
from .models import AppUser
from .forms import AppUserForms
# Register your models here.

class AppUserAdmin(admin.ModelAdmin):
    list_display = ('name','anth_key','phone','email','create_time','status')
    # fields = ('name','anth_key','phone','email','status')
    form = AppUserForms


admin.site.register(AppUser,AppUserAdmin)
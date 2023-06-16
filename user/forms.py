from django import forms
from django.core.exceptions import ValidationError

from .models import AppUser
import  re #正则
from .widgets import SendEmailButton,IDwidget
class AppUserForms(forms.ModelForm):
    id = forms.CharField(disabled=True,label='主键',widget=IDwidget)

    name = forms.CharField(min_length=3,max_length=30,required=True,
                           error_messages={
                               "required": '用户是必填项',
                               'max_length': '用户不能超过20000000',
                               'min_length':'用户不能少于3',
                           })
    #自定义验证规则：包含大小写数字等
    anth_key =forms.CharField(widget=forms.PasswordInput,label='口令',
                              error_messages={
                                                         "required": '口令不能空',
                                                         'min_length':'口令最少6',
                                                     }
                              )
    phone = forms.CharField(min_length=11,max_length=11,required=False)

    #通过widget定义widget小部件
    email = forms.CharField(required=False,widget=SendEmailButton)

    img1 = forms.CharField(max_length=100,label='头像')
    class Meta:
        model = AppUser
        # fields = '__all__'
        fields = ('id','name','anth_key','phone','email')
        error_messages = {
            'name':{
                "required":'用户是必填项',
                'max_length':'用户不能超过20000000'
            },
            'email':{
                "required": 'email is not empty!',
            }
        }
    def is_valid(self):
        print('-----is_valid-----')
        return super(AppUserForms, self).is_valid()
    def clean_anth_key(self):
        print('-----clean_anth_key-----')
        #上面验证通过后进行下面的
        anth_key =self.cleaned_data.get('anth_key')
        # 自定义验证规则：包含大小写数字等
        print(anth_key)
        print(re.search(r'\d+',anth_key,re.M))
        print(re.search(r'[a-z]+',anth_key,re.M))
        print(re.search(r'[A-Z]+',anth_key,re.M))
        if all((re.search(r'\d+',anth_key,re.M),
                re.search(r'[a-z]+',anth_key,re.M),
                re.search(r'[A-Z]+',anth_key,re.M)
               )):
            return anth_key
        raise  ValidationError('包含大小写数字等')
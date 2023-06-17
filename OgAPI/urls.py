"""
URL configuration for OgAPI project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.core.files.uploadedfile import InMemoryUploadedFile
from django.http import JsonResponse
from django.urls import path
from django.views.decorators.csrf import csrf_exempt
from django.core.mail import send_mail
from OgAPI import settings
from threading import Thread
from common.mail import my_send_email
def send_email(request,email):
    print('send_email:',email)

    mssg= '<html>欢迎您的注册，请先激活<a href = "www.baidu.com">cccc</a></html>'
    title1 ='A cool subject'
    # send_mail(
    #     subject=title,
    #     message=f"holle {email} ",
    #     html_message=mssg,
    #     from_email=email,
    #     recipient_list=[email])
    Thread(target=my_send_email,
           kwargs={
               'title':title1,
               'massage':mssg,
               'receiver':[email]
           }).start()


    return JsonResponse({
        'msg':'发送成功',
        'info':{
            'email':email
        }
    })
@csrf_exempt
def img_load(request,user_id):
    img1 : InMemoryUploadedFile= request.FILES.get('img1')


    #user_idz作为文件名
    return JsonResponse({
        'code':200,
        'msg':'上传成功',
        'path':'user/1.jpg'
    })

urlpatterns = [
    path('admin/', admin.site.urls),
    path('email/<email>/',send_email),
    path('img1/<user_id>/',img_load),
]

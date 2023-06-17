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
from django.conf.urls.static import static
from django.contrib import admin
from django.core.files.uploadedfile import InMemoryUploadedFile
from django.http import JsonResponse, HttpResponse
from django.urls import path, include
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

# @csrf_exempt
def img_load(request,user_id):
    file: InMemoryUploadedFile = request.FILES.get('img1')
    if file:
        # print(file.name)#文件名
        # print(file.content_type)#文件类型
        print(file.size)  # 大小
        # print(file.charset)
        # 上传必须是图片且小于50k
        if all((
                file.content_type.startswith('media/'),
                file.size < 75 * 1024
        )):
            print(request.META.get('REMOTE_ADDR'), '上传了', file.name)
            filename = user_id
            # 将内存中的文件写入磁盘中
            with open('media/' + filename, 'wb') as f:
                # 分段写入
                for chunk in file.chunks():
                    f.write(chunk)
                f.flush()
            return JsonResponse({
        'code':200,
        'msg':'上传成功',
        'path':'user/1.jpg'
    })

        else:
            return JsonResponse({
        'code':400,
        'msg':'上传失败',
        'path':'user/1.jpg'
    })


urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/',include('user.urls')),
    path('email/<email>/',send_email),
    path('img1/<user_id>/',img_load),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

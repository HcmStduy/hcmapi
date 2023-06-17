import os

from django.core.files.uploadedfile import InMemoryUploadedFile
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.views.decorators.csrf import csrf_exempt

from OgAPI.settings import BASE_DIR
from .forms import AppUserForms
from .models import AppUser


@csrf_exempt
def register(request):
    if request.method == 'POST':
        form = AppUserForms(request.POST)  # 包含用户名和密码
        if form.is_valid():  # 判断表单数据是否合法
            id = form.cleaned_data.get('id')
            name = form.cleaned_data['name']  # cleaned_data类型是字典，里面是提交成功后的信息
            anth_key = form.cleaned_data['anth_key']
            phone = form.cleaned_data['phone']
            email = form.cleaned_data['email']
            file: InMemoryUploadedFile = request.FILES.get('img1')

            if file:
            # print(file.name)#文件名
                   # print(file.content_type)#文件类型
                   print(file.size)  # 大小
                   # print(file.charset)
                   # 上传必须是图片且小于50k
                   if all((
                           file.content_type.startswith('image/'),
                           file.size < 75 * 1024
                   )):
                       print(request.META.get('REMOTE_ADDR'), '上传了', file.name)
                       filename = id + os.path.splitext(file.name)[-1]
                       # 将内存中的文件写入磁盘中
                       path1 = os.path.join(BASE_DIR,'media/users/')
                       path2 = 'users/'
                       filepath1 = path1+filename
                       filepath2 = path2 + filename
                       with open(filepath1, 'wb') as f:
                           # 分段写入
                           for chunk in file.chunks():
                               f.write(chunk)
                           f.flush()
                           print((id, name, anth_key, phone, email, filepath2))
                   else:
                       return HttpResponse('上传失败！')

            AppUser.objects.create(id=id,name=name,anth_key=anth_key,phone=phone,email=email,img1=filepath2)
            return render(request, 'login.html', locals())  # 将提交后的信息渲染到页面上
        else:
            return HttpResponse('请输入有效信息')
    else:

        form = AppUserForms()
    return render(request, 'register.html', locals())



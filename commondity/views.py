from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from django.views import View

from commondity.models import CategoryModel,YgeatModel
from api.commondity_set import CategoryModelSerializer,YgeatModelSerializer

class CategoryView(View):
    def get(self,request):
        datas = CategoryModel.objects.filter(parent="e4c872671bd443b1a91f014c96aa55f0").all()
        # datas = CategoryModel.objects.all()
        ser = CategoryModelSerializer(datas,many=True,context={'request': request})
        print(datas)
        return JsonResponse({
            'data':ser.data,
            'status': 200,
        })

class CatechildView(View):
    def get(self,request):
        f_id = request.GET.get('id',None)
        print(f_id)
        if f_id:
            datas = CategoryModel.objects.filter(parent=f_id).all()
        else:
            datas = CategoryModel.objects.filter(parent="e4c872671bd443b1a91f014c96aa55f0").all()
        ser = CategoryModelSerializer(datas, many=True,context={'request': request})
        return JsonResponse({
            'data': ser.data,
            'status':200
        })

class YgeatView(View):
        def get(self, request):
            datas = YgeatModel.objects.all()
            ser = YgeatModelSerializer(datas, many=True)
            return JsonResponse({
                'data': ser.data,
                'status': 200
            })

class SearchCategory(View):
    def get(self, request):
        name = request.GET.get('info', None)
        print(name)
        id = CategoryModel.objects.values('id').filter(name=name).first()
        print(id)
        if id:
            datas = CategoryModel.objects.filter(parent=id['id']).all()
            cateinfo = CategoryModelSerializer(datas,many=True,context={'request': request})
            return JsonResponse({
                'data':cateinfo.data,
                'status': 200
            })
        else:
            return JsonResponse({
                'mesg':'未查询到对应商品',
                'status': 400
            })
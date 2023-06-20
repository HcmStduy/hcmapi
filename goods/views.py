from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
# 首页所有信息
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from api.goods_set import GoodsInfoModelSerializer,GoodsModelSerializer,GoodsImageModelSerializer,TagModelSerializer,SiwapModelSerializers
from  api.user_set import NavModelSerializers
from commondity.models import CategoryModel
from goods.models import SiwapModel, GoodsModel, GoodsInfoModel
from user.models import NavModel

#首页
class GetHomeDataView(View):
    @csrf_exempt
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request):
        # 该请求是根据地区来获取商品数据的，目前数据只有西安地区的数据，所以不需要考虑

        siwap_serialize = SiwapModelSerializers(instance=SiwapModel.objects.all(), many=True)
        nav_serialize = NavModelSerializers(instance=NavModel.objects.all(), many=True,context={'request': request})
        goods1_cate = CategoryModel.objects.filter(name='常温食品').first()

        goods1_serialize = GoodsModelSerializer(goods1_cate.goods_cate.all().order_by('goods_hot').all(),
                                                 many=True,context={'request': request})
        goods1_1_serialize = GoodsModelSerializer(goods1_cate.goods_cate.all().order_by('goods_hot').all(),
                                                   many=True,context={'request': request})

        goods2_serialize = GoodsModelSerializer(
            GoodsModel.objects.filter(goods_name__contains='盒').order_by('goods_hot').all(), many=True,context={'request': request})
        # info__unit__contains = '盒'
        goods3_cate = CategoryModel.objects.filter(name='米面杂粮').first()
        goods3_serialize = GoodsModelSerializer(goods3_cate.goods_cate.all().order_by('goods_hot').all(),
                                                 many=True,context={'request': request})

        goods4_cate = CategoryModel.objects.filter(name='进口水果').first()
        goods4_serialize = GoodsModelSerializer(goods4_cate.goods_cate.all().order_by('goods_hot').all(),
                                                 many=True,context={'request': request})

        goods5_cate = CategoryModel.objects.filter(name='果干/零食').first()
        goods5_serialize = GoodsModelSerializer(goods5_cate.goods_cate.all().order_by('goods_hot').all(),
                                                 many=True,context={'request': request})
        goods6_serialize = GoodsModelSerializer(
            GoodsModel.objects.filter(goods_name__startswith='Mission').all().order_by('goods_hot').all(),
            many=True,context={'request': request})
        return JsonResponse({
            'city': request.session.get('city', None),
            'siwap_data': siwap_serialize.data,
            'nav_data': nav_serialize.data,
            'goods1_data': goods1_serialize.data,
            'goods1_1_data': {'data': goods1_1_serialize.data},
            'goods2_data': {'name': '礼盒专场',
                            'data': goods2_serialize.data},
            'goods3_data': {
                'name': '精致杂粮',
                'data': goods3_serialize.data,
                'info': ''
            },
            'goods4_data': {
                'name': '品质干货',
                'data': goods4_serialize.data
            },
            'goods5_data': {
                'name': '精选坚果',
                'data': goods5_serialize.data
            },
            'goods6_data': {
                'name': '更多好货',
                'data': goods6_serialize.data
            }
        })

    def post(self, request):
        # 获取商品详情表单
        info_name = request.POST.get('info_name', None)

        if info_name:
            goods_info = GoodsInfoModel.objects.all()
            serialize = GoodsInfoModelSerializer(instance=goods_info, many=True)
            return JsonResponse({'data': serialize.data})
        else:
            goods = GoodsModel.objects.all()

            serialize = GoodsModelSerializer(instance=goods, many=True)
            return JsonResponse({'data': serialize.data})


# 根据分类获取商品信息
class GetCateGoodDataView(View):
    @csrf_exempt
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request):
        oneid = request.GET.get('oneid')
        twoid = request.GET.get('twoid')
        print(oneid)
        print(twoid)
        if not twoid:
            print('132')
            fruit = (CategoryModel.objects.get(id=oneid)).goods_cate.all()
            serialize = GoodsModelSerializer(instance=fruit, many=True,context={'request': request})
            print(serialize.data)
            return JsonResponse({
                'code': 200,
                'data': serialize.data,
                'msg': '成功'
            })

        elif twoid:
            fruit = (CategoryModel.objects.get(id=twoid)).goods_cate.all()
            serialize = GoodsModelSerializer(instance=fruit, many=True)
            return JsonResponse({
                'code': 200,
                'data': serialize.data,
                'msg': '成功'
            })
        else:
            return JsonResponse({
                'code': 200,
                'msg': '失败'
            })


class GetGoodInfoView(View):
    @csrf_exempt
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request):
        code = request.GET.get('goods_code')
        goods_code = GoodsInfoModel.objects.filter(goods_id__goods_code=code).all()
        serialize = GoodsInfoModelSerializer(instance=goods_code, many=True,context={'request': request})
        return JsonResponse({
            'code': 200,
            'data': serialize.data,
            'msg': '成功'
        })
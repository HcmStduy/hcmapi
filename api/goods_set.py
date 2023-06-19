from  rest_framework import serializers,viewsets
from goods.models import  GoodsModel,GoodsInfoModel,TagModel,GoodsImageModel
class GoodsModelSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = GoodsModel
        fields = ('id','categoryid','goods_name','goods_code','maxcount','price','goods_hot')

class GoodsInfoModelSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = GoodsInfoModel
        fields = ('id','goods_id', 'goods_info', 'sellprice', 'subtitle', 'unit', 'spec', 'video', 'placeoforgin')

class TagModelSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = TagModel
        fields = ('tag','id')


class GoodsImageModelSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = GoodsImageModel
        fields =  ('id','img1','goods_id')
#API视图类
class GoodsModelAPIView(viewsets.ModelViewSet):
    queryset = GoodsModel.objects.all()
    serializer_class = GoodsModelSerializer

#API视图类
class GoodsInfoModelAPIView(viewsets.ModelViewSet):
    queryset = GoodsInfoModel.objects.all()
    serializer_class = GoodsInfoModelSerializer

class TagModelAPIView(viewsets.ModelViewSet):
    queryset = TagModel.objects.all()
    serializer_class = TagModelSerializer

class GoodsImageModelAPIView(viewsets.ModelViewSet):
    queryset = GoodsImageModel.objects.all()
    serializer_class = GoodsImageModelSerializer
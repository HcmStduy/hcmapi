from  rest_framework import serializers,viewsets

from api.commondity_set import CategoryModelSerializer
from goods.models import GoodsModel, GoodsInfoModel, TagModel, GoodsImageModel, SiwapModel
from api.address_set import ActivesModelserializers

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

#轮播图
class SiwapModelSerializers(serializers.ModelSerializer):
    active_id = ActivesModelserializers

    class Meta:
        model = SiwapModel
        fields = ['active_id', 'active_img']

class GoodsImage_OneSerializers(serializers.ModelSerializer):
    class Meta:
        model = GoodsImageModel
        fields = ['img1']

class GoodsModel_twoSerializers(serializers.HyperlinkedModelSerializer):
    categoryid = CategoryModelSerializer
    image = GoodsImageModelSerializer(many=True)

    class Meta:
        model = GoodsModel
        fields = ['image', 'id', 'goods_name', 'price']
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
from rest_framework import serializers,viewsets
from cartlist.models import OrderGoods,CartModel,OrderlistModel
from api.user_set import AppUserSerializers
from  api.goods_set import GoodsModelSerializer
class CartModelSerializers(serializers.HyperlinkedModelSerializer):
    user = AppUserSerializers()
    goods = GoodsModelSerializer()
    class Meta:
        model =CartModel
        fields = ('id','user', 'goods', 'count')


class OrderlistModelSerializers(serializers.HyperlinkedModelSerializer):
    user = AppUserSerializers()
    class Meta:
        model = OrderlistModel
        fields = ('id', 'user', 'order_time', 'order_statues', 'addr_id')


class OrderGoodsSerializers(serializers.HyperlinkedModelSerializer):
    order = OrderlistModelSerializers()
    goods = GoodsModelSerializer()
    class Meta:
        model = OrderGoods
        fields = ('order','goods','count')



class Order_list_1_SeraLier(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = OrderGoods
        fields = ('count')

class OrderGoodsAPIView(viewsets.ModelViewSet):
    queryset = OrderGoods.objects.all()
    serializer_class = OrderGoodsSerializers

class CartModelAPIView(viewsets.ModelViewSet):
    queryset = CartModel.objects.all()
    serializer_class = CartModelSerializers

class OrderlistModelAPIView(viewsets.ModelViewSet):
    queryset = OrderlistModel.objects.all()
    serializer_class = OrderlistModelSerializers

class Order_list_1_SeraLierView(viewsets.ModelViewSet):
    queryset = OrderGoods.objects.values('count').all()
    serializer_class = Order_list_1_SeraLier
from rest_framework import serializers,viewsets
from cartlist.models import OrderGoods,CartModel,OrderlistModel

class CartModelSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model =CartModel
        fields = ('user', 'goods', 'count')
class OrderGoodsSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = OrderGoods
        fields = ('order','goods','count')

class OrderlistModelSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = OrderlistModel
        fields = ('user','order_time','order_statues','addr_id')
class Order_list_1_SeraLier(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = OrderGoods
        fields = ('count',)

class OrderGoodsAPIView(viewsets.ModelViewSet):
    queryset = OrderGoods.objects.all()
    serializer_class = OrderGoodsSerializers
class CartModelAPIView(viewsets.ModelViewSet):
    queryset = CartModel.objects.all()
    serializer_class = CartModelSerializers
class OrderlistModelAPIView(viewsets.ModelViewSet):
    queryset = OrderlistModel.objects.all()
    serializer_class = OrderlistModelSerializers
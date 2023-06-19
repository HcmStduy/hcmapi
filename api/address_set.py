from rest_framework import serializers,viewsets
from address.models import AddressModel,ActivesModel,DiscountModel

class AddressModelserializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = AddressModel
        fields = ('id','address', 'state', 'user')

class ActivesModelserializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ActivesModel
        fields = ('id','active_name', 'active_url', 'icon')

class DiscountModelserializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = DiscountModel
        fields = ('id','user_id','deduction','total_maney','datatime','time_of_validity')

class AddressModelAPIView(viewsets.ModelViewSet):
    queryset = AddressModel.objects.all()
    serializer_class = AddressModelserializers

class ActivesModelAPIView(viewsets.ModelViewSet):
    queryset = ActivesModel.objects.all()
    serializer_class = ActivesModelserializers

class DiscountModelAPIView(viewsets.ModelViewSet):
    queryset = DiscountModel.objects.all()
    serializer_class = DiscountModelserializers
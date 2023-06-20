from rest_framework import serializers,viewsets
from citys.models import  CityModel,CityAreaModel

class CityModelSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CityModel
        fields = ('id','city_name', 'city_letter', 'city_hot')

class CityAreaModelSerializers(serializers.HyperlinkedModelSerializer):
    city_id = CityModelSerializers()
    class Meta:
        model = CityAreaModel
        fields = ('id','cityareaname', 'city_id')

class CityModelAPIView(viewsets.ModelViewSet):
    queryset = CityModel.objects.all()
    serializer_class = CityModelSerializers

class CityAreaModelAPIView(viewsets.ModelViewSet):
    queryset = CityAreaModel.objects.all()
    serializer_class = CityAreaModelSerializers

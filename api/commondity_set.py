
from  rest_framework import serializers,viewsets
from commondity.models import CategoryModel,YgeatModel

#序列化
class CategoryModelSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CategoryModel
        fields = ('id','code','name','grade','parent','picture_url')

class YgeatModelSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = YgeatModel
        fields = ('id','eat_img', 'eat_content', 'eat_time', 'hot')

#API视图类
class CategoryAPIView(viewsets.ModelViewSet):
    queryset = CategoryModel.objects.all()
    serializer_class = CategoryModelSerializer

class YgeatModelAPIView(viewsets.ModelViewSet):
        queryset = YgeatModel.objects.all()
        serializer_class = YgeatModelSerializer
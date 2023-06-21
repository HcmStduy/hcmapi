from rest_framework import serializers, viewsets
from user.models import AppUser, CommentsModel, NavModel


class AppUserSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = AppUser
        fields = ('name', 'anth_key', 'phone', 'email', 'status', 'img1')


class AppUserAPIView(viewsets.ModelViewSet):
    queryset = AppUser.objects.all()
    serializer_class = AppUserSerializers


class CommentsModelSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CommentsModel
        fields = ('order_id', 'comments', 'comment_time')


class CommentsModelAPIView(viewsets.ModelViewSet):
    queryset = CommentsModel.objects.all()
    serializer_class = CommentsModelSerializers


class NavModelSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = NavModel
        fields = ('nav_child_id', 'actives_id', 'name', 'image')


class NavModelAPIView(viewsets.ModelViewSet):
    queryset = NavModel.objects.all()
    serializer_class = NavModelSerializers


from django.urls import path
# from .views import CategoryView,CatechildView,YgeatView,SearchCategory
from citys.views import CityApi, CityAreaApi, SetCity

urlpatterns = [
    path('getcity/', CityApi.as_view(), name='city'),
    path('area/', CityAreaApi.as_view(), name='area'),
    path('setcity/', SetCity.as_view(), name='set_city')
]



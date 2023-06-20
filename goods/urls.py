
from django.urls import path
from goods.views import GetHomeDataView, GetCateGoodDataView, GetGoodInfoView

urlpatterns = [
    path('gethome/', GetHomeDataView.as_view(), name='get_home'),
    path('getcate/', GetCateGoodDataView.as_view(), name='get_cate'),
    path('getinfo/', GetGoodInfoView.as_view(), name='get_info')

]

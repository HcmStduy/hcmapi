from rest_framework import routers
from .commondity_set import CategoryAPIView,YgeatModelAPIView
from .goods_set import GoodsModelAPIView,GoodsInfoModelAPIView,TagModelAPIView,GoodsImageModelAPIView
from .address_set import ActivesModelAPIView,AddressModelAPIView,DiscountModelAPIView
from .user_set import AppUserAPIView,CommentsModelAPIView,NavModelAPIView
from  .citys_set import CityModelAPIView,CityAreaModelAPIView
from  .cartlist_set import CartModelAPIView,OrderGoodsAPIView,OrderlistModelAPIView,Order_list_1_SeraLierView
# 声明api路由
api_router = routers.DefaultRouter()

# 向api路由中注册ViewSet
api_router.register('commondity/category', CategoryAPIView)
api_router.register('commondity/ogeat', YgeatModelAPIView)

api_router.register('good/goods', GoodsModelAPIView)
api_router.register('good/info', GoodsInfoModelAPIView)
api_router.register('good/taq', TagModelAPIView)
api_router.register('good/img', GoodsImageModelAPIView)

api_router.register('address/address', AddressModelAPIView)
api_router.register('address/actives', ActivesModelAPIView)
api_router.register('address/discount', DiscountModelAPIView)

api_router.register('user/users', AppUserAPIView)
api_router.register('user/comments', CommentsModelAPIView)
api_router.register('user/nav', NavModelAPIView)

api_router.register('citys/city', CityModelAPIView)
api_router.register('citys/area', CityAreaModelAPIView)

api_router.register('cartlist/cart', CartModelAPIView)
api_router.register('cartlist/ordergoods', OrderGoodsAPIView)
api_router.register('cartlist/orderlist', OrderlistModelAPIView)
# api_router.register('cartlist/orderlist1', Order_list_1_SeraLierView)


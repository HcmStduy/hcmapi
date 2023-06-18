from rest_framework import routers
from .commondity_set import CategoryAPIView,YgeatModelAPIView


# 声明api路由
api_router = routers.DefaultRouter()

# 向api路由中注册ViewSet
api_router.register('commondity/category', CategoryAPIView)
api_router.register('commondity/ogeat', YgeatModelAPIView)


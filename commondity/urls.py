
from django.urls import path
from .views import CategoryView,CatechildView,YgeatView,SearchCategory
urlpatterns = [
    path('category/',CategoryView.as_view()),
    path('catechild/',CatechildView.as_view()),
    path('eat/',YgeatView.as_view()),
    path('search/',SearchCategory.as_view())
]

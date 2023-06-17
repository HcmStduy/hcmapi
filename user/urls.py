
from django.conf.urls.static import static
from django.contrib import admin
from django.core.files.uploadedfile import InMemoryUploadedFile
from django.http import JsonResponse, HttpResponse
from django.urls import path
from django.views.decorators.csrf import csrf_exempt
from django.core.mail import send_mail
from OgAPI import settings
from .views import register

urlpatterns = [
    path('register/',register)

]

from django.urls import path

from .views import index,test

urlpatterns = [
    path('index/', index, name='index'),
    path('test/', test, name='test'),
]
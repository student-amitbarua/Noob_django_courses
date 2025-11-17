from rest_framework.routers import DefaultRouter
from django.urls import path, include
from . import views

router = DefaultRouter() # Our router

router.register('', views.ServiceViewset) #ekta router create kore fellam


urlpatterns = [
    path('', include(router.urls)),
]

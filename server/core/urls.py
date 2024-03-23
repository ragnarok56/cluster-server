from django.urls import path
from . import views

from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register('hosts', views.HostViewSet, basename='host')
router.register('targets', views.TargetsViewSet, basename='target')

urlpatterns = [
    path('', views.index, name="index"),
] + router.urls
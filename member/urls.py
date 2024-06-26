from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import UserView
router = DefaultRouter()

router.register('list', UserView) 
urlpatterns = [
    path('', include(router.urls)),
]
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import *

from django.urls import path, include

router = DefaultRouter()
router.register('', TestApiViewSet, basename='test'),
router.register('signup', SignUpViewSet, basename='signup')

urlpatterns = [
    path('',include(router.urls)),
    path('login/', TokenObtainPairView.as_view(), name='login')
]

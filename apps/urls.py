from django.urls import path, include
from rest_framework.routers import DefaultRouter as DR

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from apps.views import RegisterView, StudentView
router = DR()

router.register('student', StudentView)

urlpatterns = [
    path('register', RegisterView.as_view()),
    path('login', TokenObtainPairView.as_view()),
    path('refresh', TokenRefreshView.as_view()),
    path('', include(router.urls))
]
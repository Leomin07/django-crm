from django.urls import path, include
from rest_framework import routers
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenBlacklistView,
    TokenVerifyView,
)
from todo.views import (
    UserProfileView,
    user_login,
    logout_user,
    user_register,
)

urlpatterns = [
    path("user/profile", UserProfileView.as_view(), name="profile"),
    # path("auth/login", TokenObtainPairView.as_view(), name="login"),
    # path("auth/refresh", TokenRefreshView.as_view(), name="token_refresh"),
    path("auth/login", user_login, name="login"),
    path("auth/register", user_register, name="register"),
    path("auth/logout", logout_user, name="logout"),
]

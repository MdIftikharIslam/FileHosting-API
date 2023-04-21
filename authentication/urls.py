from rest_framework_simplejwt.views import TokenRefreshView
from django.urls import path
from .views import *

urlpatterns = [
    
    path('login/', MyTokenObtainPairView.as_view()),
    path('login/token/refresh', TokenRefreshView.as_view()),
    path('register/', RegisterAPIView.as_view())
]

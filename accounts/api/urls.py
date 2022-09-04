from django.urls import path
from . import views
from .serializers import MyTokenObtainPairView
from rest_framework_simplejwt.views import (
    TokenRefreshView,
)



app_name = 'accounts'
urlpatterns = [ 
    path('register/', views.register_views, name='register'),
     path('token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    
]
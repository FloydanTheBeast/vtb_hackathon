"""hackathon URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from vtb_app.views import *
from vtb_app.viewsets import *
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from rest_framework.routers import DefaultRouter
from vtb_app import viewsets

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'search_history', viewsets.SearchHistoryViewSet)
router.register(r'extra_user_data', viewsets.ExtraUserDataViewSet)

api_urlpatterns = [
    # path('', include('rest_framework.urls')),
    path('accounts/', include('rest_registration.api.urls')),
    path('accounts/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('accounts/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('test/', TestView.as_view()),
    path('car_recognize/', CarRecognizeView.as_view()),
    path('marketplace/', MarketplaceView.as_view()),
    path('car_loan/', CarLoanView.as_view()),
    path('', include(router.urls))
    # path('search_history/', SearchHistoryViewSet.as_view({"get": "list"})),
    # path('search_history/<int:pk>/', SearchHistoryViewSet.as_view({"delete": "destroy"}))
]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(api_urlpatterns))
]

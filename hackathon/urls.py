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
router.register(r'loan_history', viewsets.LoanHistoryViewSet)
router.register(r'extra_user_data', viewsets.ExtraUserDataViewSet)
router.register(r'car_recognize', viewsets.CarRecognizeViewSet, basename='car_recognize')
router.register(r'car_loan', viewsets.CarLoanViewSet, basename='car_loan')

api_urlpatterns = [
    path('accounts/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('accounts/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('test/', TestView.as_view(), name='test'),
    path('accounts/', include('rest_registration.api.urls')),
    path('', include(router.urls))
]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(api_urlpatterns))
]

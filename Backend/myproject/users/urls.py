# users/urls.py
from django.urls import path
from .views import SendOtpView, VerifyOtpView

urlpatterns = [
    path("auth/send-otp", SendOtpView.as_view()),
    path("auth/verify-otp", VerifyOtpView.as_view()),
]

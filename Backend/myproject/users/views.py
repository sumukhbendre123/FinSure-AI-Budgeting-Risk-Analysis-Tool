# users/views.py
from rest_framework import status, views
from rest_framework.response import Response
from security_layer.jwt_auth import JwtService
from security_layer.otp_service import OtpService
from .services import AuthService
from .serializers import SendOtpSerializer, VerifyOtpSerializer

class SendOtpView(views.APIView):
    permission_classes = []  # public

    def post(self, request):
        ser = SendOtpSerializer(data=request.data); ser.is_valid(raise_exception=True)
        svc = AuthService(jwt=JwtService(), otp=OtpService())
        svc.send_otp(ser.validated_data["email"])
        return Response({"detail": "OTP sent"}, status=status.HTTP_200_OK)

class VerifyOtpView(views.APIView):
    permission_classes = []  # public

    def post(self, request):
        ser = VerifyOtpSerializer(data=request.data); ser.is_valid(raise_exception=True)
        svc = AuthService(jwt=JwtService(), otp=OtpService())
        tokens = svc.verify_otp(ser.validated_data["email"], ser.validated_data["code"])
        return Response(tokens, status=status.HTTP_200_OK)

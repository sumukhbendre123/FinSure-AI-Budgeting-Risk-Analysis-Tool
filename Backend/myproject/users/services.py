from dataclasses import dataclass
from django.contrib.auth import get_user_model
import firebase_admin
from firebase_admin import auth as fb_auth, credentials
from security_layer.jwt_auth import JwtService
from security_layer.otp_service import OtpService
from .models import OtpRequest

User = get_user_model()

# Initialize once (SRP: bootstrap kept here, could be moved to AppConfig)
def init_firebase(creds_path: str | None = None):
    if not firebase_admin._apps:
        cred = credentials.Certificate(creds_path) if creds_path else credentials.ApplicationDefault()
        firebase_admin.initialize_app(cred)

@dataclass
class AuthService:
    jwt: JwtService
    otp: OtpService

    def send_otp(self, user_email: str) -> None:
        user, _ = User.objects.get_or_create(username=user_email, defaults={"email": user_email})
        code = self.otp.generate()
        OtpRequest.objects.create(user=user, code_hash=code, expires_at=self.otp.expires_at())
        # TODO: integrate email/SMS provider to deliver `code`

    def verify_otp(self, user_email: str, code: str) -> dict:
        user = User.objects.get(username=user_email)
        req = OtpRequest.objects.filter(user=user, is_used=False).latest("created_at")
        if req.is_valid(code):
            req.mark_used()
            return self.jwt.issue_tokens(user.id)
        raise ValueError("Invalid or expired OTP")

    def verify_firebase_id_token(self, id_token: str) -> dict:
        decoded = fb_auth.verify_id_token(id_token)
        return decoded

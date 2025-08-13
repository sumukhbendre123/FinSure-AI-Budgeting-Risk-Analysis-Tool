from rest_framework_simplejwt.tokens import RefreshToken

class JwtService:
    def issue_tokens(self, user_id: str) -> dict:
        refresh = RefreshToken.for_user_id(user_id)  # DRF-SJ supports user model, or map to a dummy
        return {"access": str(refresh.access_token), "refresh": str(refresh)}

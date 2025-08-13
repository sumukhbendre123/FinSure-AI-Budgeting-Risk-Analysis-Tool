from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone

class UserProfile(AbstractUser):
    # Extend as needed (DRY: reuse Django auth)
    display_name = models.CharField(max_length=120, blank=True)
    settings = models.JSONField(default=dict, blank=True)

class OtpRequest(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    code_hash = models.CharField(max_length=12)  # demo; store hashed in prod
    is_used = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    expires_at = models.DateTimeField()

    def is_valid(self, code: str) -> bool:
        return (not self.is_used) and (self.code_hash == code) and (timezone.now() < self.expires_at)

    def mark_used(self):
        self.is_used = True
        self.save(update_fields=["is_used"])

from django.db import models
from django.conf import settings

class BankToken(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    provider = models.CharField(max_length=50)     # e.g. "plaid"
    access_token = models.TextField()              # encrypted value
    refresh_token = models.TextField(blank=True, null=True)
    expires_at = models.DateTimeField(null=True, blank=True)
    metadata = models.JSONField(default=dict, blank=True)

class BankAccount(models.Model):
    token = models.ForeignKey(BankToken, on_delete=models.CASCADE, related_name="accounts")
    provider_account_id = models.CharField(max_length=128)
    name = models.CharField(max_length=128)

class Transaction(models.Model):
    account = models.ForeignKey(BankAccount, on_delete=models.CASCADE, related_name="transactions")
    external_id = models.CharField(max_length=128, db_index=True)
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    currency = models.CharField(max_length=8, default="INR")
    occurred_at = models.DateTimeField()
    merchant = models.CharField(max_length=255, blank=True)
    raw = models.JSONField(default=dict)
    normalized = models.JSONField(default=dict)
    category = models.CharField(max_length=64, blank=True)
    is_flagged = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

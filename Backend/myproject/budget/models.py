from django.db import models
from django.conf import settings

class BudgetCategory(models.Model):
    name = models.CharField(max_length=64)
    parent = models.ForeignKey("self", null=True, blank=True, on_delete=models.SET_NULL)

class Budget(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    category = models.ForeignKey(BudgetCategory, on_delete=models.CASCADE)
    period = models.CharField(max_length=16, choices=[("MONTHLY","MONTHLY"),("ANNUAL","ANNUAL")])
    limit_amount = models.DecimalField(max_digits=12, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

class Recommendation(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    payload = models.JSONField(default=dict)
    source = models.CharField(max_length=16, default="AI")
    created_at = models.DateTimeField(auto_now_add=True)

class RiskAssessment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    score = models.FloatField()
    factors = models.JSONField(default=dict)
    generated_at = models.DateTimeField(auto_now_add=True)

# transactions/serializers.py
from rest_framework import serializers
from .models import Transaction

class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = ["id","external_id","amount","currency","occurred_at","merchant","category","normalized","created_at"]

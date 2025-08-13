# transactions/services.py
from datetime import datetime, timedelta
from typing import Iterable
from django.db import transaction as dbtx
from .models import BankToken, BankAccount, Transaction
from .connectors.base import BankConnector, TransactionDTO, BankAccountDTO

class TransactionNormalizer:
    def normalize(self, dto: TransactionDTO) -> dict:
        return {
            "id": dto.external_id,
            "amount": dto.amount,
            "currency": dto.currency,
            "datetime": dto.occurred_at.isoformat(),
            "merchant": dto.merchant or "",
        }

class TransactionRepository:
    def bulk_upsert(self, account: BankAccount, txns: Iterable[TransactionDTO], normalizer: TransactionNormalizer):
        objs = []
        for dto in txns:
            objs.append(Transaction(
                account=account,
                external_id=dto.external_id,
                amount=dto.amount,
                currency=dto.currency,
                occurred_at=dto.occurred_at,
                merchant=dto.merchant or "",
                raw=dto.raw,
                normalized=normalizer.normalize(dto),
            ))
        Transaction.objects.bulk_create(objs, ignore_conflicts=True)

class BankingService:
    def __init__(self, connector: BankConnector, repo: TransactionRepository, normalizer: TransactionNormalizer):
        self.connector = connector
        self.repo = repo
        self.normalizer = normalizer

    def sync_user(self, bank_token: BankToken, since_days: int = 45):
        token = {
            "access_token": bank_token.access_token,
            "refresh_token": bank_token.refresh_token,
            "expires_at": bank_token.expires_at,
        }
        accounts: list[BankAccountDTO] = self.connector.fetch_accounts(token)
        with dbtx.atomic():
            for acc in accounts:
                account, _ = BankAccount.objects.get_or_create(
                    token=bank_token, provider_account_id=acc.account_id, defaults={"name": acc.name}
                )
                txns = self.connector.fetch_transactions(token, acc.account_id, datetime.utcnow() - timedelta(days=since_days))
                self.repo.bulk_upsert(account, txns, self.normalizer)

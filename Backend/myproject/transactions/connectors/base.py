# transactions/connectors/base.py
from abc import ABC, abstractmethod
from dataclasses import dataclass
from datetime import datetime
from typing import List, Dict

@dataclass
class BankAccountDTO:
    account_id: str
    name: str

@dataclass
class TransactionDTO:
    external_id: str
    amount: float
    currency: str
    occurred_at: datetime
    merchant: str | None
    raw: Dict

class BankConnector(ABC):
    @abstractmethod
    def exchange_code(self, auth_code: str) -> dict: ...
    @abstractmethod
    def refresh(self, token: dict) -> dict: ...
    @abstractmethod
    def fetch_accounts(self, token: dict) -> List[BankAccountDTO]: ...
    @abstractmethod
    def fetch_transactions(self, token: dict, account_id: str, since: datetime) -> List[TransactionDTO]: ...

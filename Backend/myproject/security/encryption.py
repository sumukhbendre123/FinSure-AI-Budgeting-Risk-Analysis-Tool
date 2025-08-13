from cryptography.fernet import Fernet
import base64, os

class EncryptionService:
    # DIP: Higher layers depend on this abstraction, not cryptography directly
    def __init__(self, key: str | None = None):
        key = key or base64.urlsafe_b64encode(os.urandom(32))
        self._fernet = Fernet(key)

    def encrypt(self, plaintext: str) -> str:
        return self._fernet.encrypt(plaintext.encode()).decode()

    def decrypt(self, ciphertext: str) -> str:
        return self._fernet.decrypt(ciphertext.encode()).decode()

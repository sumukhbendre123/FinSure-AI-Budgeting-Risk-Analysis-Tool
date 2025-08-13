import random, time
from datetime import datetime, timedelta

class OtpService:
    # ISP: Only OTP responsibilities here
    def generate(self) -> str:
        return f"{random.randint(100000, 999999)}"

    def expires_at(self, minutes: int = 10) -> datetime:
        return datetime.utcnow() + timedelta(minutes=minutes)

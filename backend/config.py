from pathlib import Path
from dotenv import load_dotenv
import os

BASE_DIR = Path(__file__).resolve().parent

load_dotenv(
    BASE_DIR / ".env"
)

DATABASE_URL = os.getenv(
    "DATABASE_URL"
)

AML_LIMIT = int(
    os.getenv(
        "AML_LIMIT",
        1000000
    )
)

KYC_REQUIRED = (
    os.getenv(
        "KYC_REQUIRED",
        "True"
    ).lower() == "true"
)

RISK_THRESHOLD = int(
    os.getenv(
        "RISK_THRESHOLD",
        80
    )
)

FRAUD_THRESHOLD = int(
    os.getenv(
        "FRAUD_THRESHOLD",
        85
    )
)
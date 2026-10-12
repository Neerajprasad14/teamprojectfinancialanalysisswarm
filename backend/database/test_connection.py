"""
Database Connection Test
"""

from backend.database.db import (
    engine
)

try:

    with engine.connect():

        print(
            "Database Connected Successfully."
        )

except Exception as error:

    print(
        "Database Connection Failed."
    )

    print(error)
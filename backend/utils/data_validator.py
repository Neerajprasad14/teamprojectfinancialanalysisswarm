"""
Data Validation Module
"""


class DataValidator:

    def validate_transaction(
            self,
            transaction):

        required_fields = [

            "amount",

            "country",

            "kyc_verified"
        ]

        for field in required_fields:

            if field not in transaction:

                return False

        return True

    def validate_customer(
            self,
            customer):

        required_fields = [

            "income",

            "credit_score"
        ]

        for field in required_fields:

            if field not in customer:

                return False

        return True
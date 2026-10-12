"""
Evidence Engine
"""


class EvidenceEngine:

    def generate(
            self,
            transaction):

        evidence = []

        if transaction.get(
            "Amount",
            0
        ) > 1000000:

            evidence.append(
                "Transaction exceeds AML threshold."
            )

        if not transaction.get(
            "kyc_verified",
            False
        ):

            evidence.append(
                "Customer KYC missing."
            )

        if transaction.get(
            "Sender_bank_location"
        ) != transaction.get(
            "Receiver_bank_location"
        ):

            evidence.append(
                "Cross-border transaction detected."
            )

        return evidence
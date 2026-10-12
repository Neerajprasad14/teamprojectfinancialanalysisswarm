from backend.agents.regulation_agent import (
    RegulationAgent
)


class ComplianceAgent:

    def __init__(self):

        self.regulation_agent = (
            RegulationAgent()
        )

    def evaluate(
            self,
            transaction):

        rules = (
            self.regulation_agent
            .get_rules()
        )

        print("\nRules Received:")
        print(rules)

        aml_rules = rules.get(
            "AML",
            {}
        )

        aml_limit = aml_rules.get(
            "AML_LIMIT",
            1000000
        )

        violations = []

        if transaction.get(
            "Amount",
            0
        ) > aml_limit:

            violations.append(
                "AML_THRESHOLD_EXCEEDED"
            )

        if not transaction.get(
            "kyc_verified",
            False
        ):

            violations.append(
                "KYC_MISSING"
            )

        return {

            "agent":
            "ComplianceAgent",

            "violations":
            violations,

            "score":
            len(violations) * 40,

            "confidence":
            0.90
        }
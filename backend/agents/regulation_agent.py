import json
from pathlib import Path


class RegulationAgent:

    def __init__(self):

        rules_path = (
            Path(__file__).resolve().parents[2]
            / "datasets"
            / "regulations"
            / "regulations.json"
        )

        print("\n========== REGULATION AGENT ==========")
        print("Rules File Path:")
        print(rules_path)

        with open(
            rules_path,
            "r",
            encoding="utf-8"
        ) as file:

            self.rules = json.load(file)

        print("\nLoaded Rules:")
        print(self.rules)

    def get_rules(self):

        return self.rules
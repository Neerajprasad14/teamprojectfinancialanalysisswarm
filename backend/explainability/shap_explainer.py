"""
File Name:
shap_explainer.py

Purpose:

Provide Explainable AI capabilities.

What is SHAP?

SHAP calculates feature importance.

Instead of:

Risk Score = 92

We know WHY:

1. High loan amount
2. Low credit score
3. Poor repayment history

Research Contribution:

Explainable Financial Intelligence

Auditors and regulators can understand
how the decision was made.
"""

import shap


class SHAPExplainer:

    """
    SHAP Explanation Engine.
    """

    def explain(
            self,
            model,
            data):

        """
        Generate explanation.

        Inputs:

        model:
            Machine-learning model

        data:
            Input features

        Output:
            SHAP values
        """

        explainer = shap.Explainer(
            model
        )

        return explainer(
            data
        )
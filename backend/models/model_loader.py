"""
File Name:
model_loader.py

Purpose:

Load trained machine learning models
from disk and provide them to agents.

Benefits:

1. Prevent duplicate loading code.
2. Centralized model management.
3. Easier maintenance.
4. Faster debugging.

Research Contribution:

Improves modularity and reproducibility.
"""

import joblib


class ModelLoader:

    @staticmethod
    def load(model_path):
        """
        Load machine learning model.

        Input:
            Path to pkl file

        Output:
            Loaded model object
        """

        return joblib.load(model_path)
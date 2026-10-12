"""
File: statistical_test.py

Purpose:
Evaluate statistical significance.

Used to prove that improvements
are not due to randomness.

Method:
Independent T-Test

Research Contribution:
Provides scientific validation.
"""

from scipy.stats import (
    ttest_ind
)

t_stat, p_value = ttest_ind(

    centralized_scores,

    swarm_scores

)

print(
    "P-Value:",
    p_value
)

if p_value < 0.05:

    print(
        "Statistically Significant"
    )

else:

    print(
        "Not Significant"
    )
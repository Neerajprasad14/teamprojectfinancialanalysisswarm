"""
File Name:
metrics_collector.py

Purpose:

Automatically collect
research evaluation metrics.

Metrics Collected:

1. Accuracy
2. Precision
3. Recall
4. F1 Score
5. Latency
6. Throughput
7. Consensus Time
8. Recovery Time

Research Contribution:

Automates result generation
for the paper.
"""


class MetricsCollector:

    """
    Research Metrics Collector.
    """

    def record(
            self,
            metric,
            value):

        """
        Store metric.

        Input:
            Metric name

        Output:
            Metric record
        """

        print(

            f"{metric} = {value}"

        )
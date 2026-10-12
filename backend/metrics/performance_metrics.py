"""
File Name:
performance_metrics.py

Purpose:

Track system performance.

Metrics:

1. Latency
2. Throughput
3. Agent Utilization
4. Recovery Time
"""


class PerformanceMetrics:

    def calculate_latency(
            self,
            start,
            end):

        return end - start
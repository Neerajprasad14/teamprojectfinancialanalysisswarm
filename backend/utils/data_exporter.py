"""
File Name:
data_exporter.py

Purpose:

Export research results and swarm
predictions into CSV files.

Research Contribution:

Enables reproducible experimentation.
"""

import pandas as pd


class DataExporter:

    def export_csv(
            self,
            data,
            file_name):

        df = pd.DataFrame(data)

        df.to_csv(

            file_name,

            index=False
        )

        print(

            f"{file_name} exported."

        )
from __future__ import annotations

import csv
from datetime import datetime
from pathlib import Path

from wisense.models import SignalSample


class CsvExporter:
    """
    Responsável por exportar amostras do WiSense para CSV.
    """

    def __init__(self, output_directory: str = "data") -> None:
        self.output_directory = Path(output_directory)
        self.output_directory.mkdir(parents=True, exist_ok=True)

    def export(
        self,
        samples: list[SignalSample],
        filename: str | None = None,
    ) -> Path:

        if filename is None:
            filename = datetime.now().strftime(
                "simulated_signal_%Y-%m-%d_%H-%M-%S.csv"
            )

        output_path = self.output_directory / filename

        with output_path.open(
            "w",
            newline="",
            encoding="utf-8",
        ) as file:

            writer = csv.writer(file)

            writer.writerow(
                [
                    "timestamp",
                    "rssi",
                    "movement",
                ]
            )

            for sample in samples:

                writer.writerow(
                    [
                        sample.timestamp.isoformat(),
                        sample.rssi,
                        sample.movement,
                    ]
                )

        return output_path
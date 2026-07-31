from dataclasses import dataclass
from datetime import datetime


@dataclass(slots=True)
class SignalSample:
    """
    Representa uma única leitura do sinal Wi-Fi.
    """

    timestamp: datetime
    rssi: float
    movement: bool = False

    def __str__(self):
        status = "MOVIMENTO" if self.movement else "NORMAL"

        return (
            f"[{self.timestamp.strftime('%H:%M:%S')}] "
            f"RSSI={self.rssi:.2f} dBm | {status}"
        )
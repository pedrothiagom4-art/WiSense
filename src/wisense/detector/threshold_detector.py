from collections import deque
from statistics import mean


class ThresholdDetector:
    """
    Detecta movimento observando quedas bruscas no RSSI.
    """

    def __init__(
        self,
        window_size: int = 10,
        threshold: float = 6.0,
    ) -> None:

        self.window = deque(maxlen=window_size)

        self.threshold = threshold

    def detect(self, rssi: float) -> bool:

        if len(self.window) < self.window.maxlen:

            self.window.append(rssi)

            return False

        baseline = mean(self.window)

        movement = abs(rssi - baseline) >= self.threshold

        self.window.append(rssi)

        return movement
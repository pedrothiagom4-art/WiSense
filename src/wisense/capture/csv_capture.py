from wisense.capture.base import CaptureEngine
from wisense.models import SignalSample


class CsvCapture(CaptureEngine):

    def __init__(self):
        raise NotImplementedError(
            "Será implementado futuramente."
        )

    def read(self) -> SignalSample:
        raise NotImplementedError
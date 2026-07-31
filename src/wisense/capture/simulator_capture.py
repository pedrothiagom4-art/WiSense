from wisense.capture.base import CaptureEngine
from wisense.simulation import SignalSimulator
from wisense.models import SignalSample


class SimulatorCapture(CaptureEngine):

    def __init__(self) -> None:
        self.simulator = SignalSimulator()

    def read(self) -> SignalSample:
        return self.simulator.generate()
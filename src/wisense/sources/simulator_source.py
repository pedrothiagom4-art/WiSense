from wisense.simulation import SignalSimulator
from wisense.sources.signal_source import SignalSource


class SimulatorSource(SignalSource):

    def __init__(self):

        self.simulator = SignalSimulator()

    def read(self):

        return self.simulator.generate()
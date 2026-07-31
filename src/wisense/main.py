import time

from wisense.detector import ThresholdDetector
from wisense.simulation import SignalSimulator


def main():

    simulator = SignalSimulator()

    detector = ThresholdDetector()

    while True:

        sample = simulator.generate()

        detected = detector.detect(sample.rssi)

        print(
            f"{sample.rssi:6.2f} dBm | "
            f"Simulado: {sample.movement} | "
            f"Detectado: {detected}"
        )

        time.sleep(0.3)


if __name__ == "__main__":
    main()
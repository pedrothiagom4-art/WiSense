import time

from wisense.exporters import CsvExporter
from wisense.simulation import SignalSimulator


def main():

    simulator = SignalSimulator()

    exporter = CsvExporter()

    samples = []

    print("WiSense v0.1\n")

    try:

        for _ in range(100):

            sample = simulator.generate()

            samples.append(sample)

            print(sample)

            time.sleep(0.2)

    except KeyboardInterrupt:

        print("\nInterrompido.")

    path = exporter.export(samples)

    print(f"\nCSV salvo em:\n{path.resolve()}")


if __name__ == "__main__":
    main()
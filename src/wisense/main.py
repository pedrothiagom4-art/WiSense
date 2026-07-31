import time

from wisense.sources import SimulatorSource


def main():

    source = SimulatorSource()

    while True:

        sample = source.read()

        print(sample)

        time.sleep(0.5)


if __name__ == "__main__":
    main()
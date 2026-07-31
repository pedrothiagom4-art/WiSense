import time

from wisense.capture import SimulatorCapture


def main():

    capture = SimulatorCapture()

    print("WiSense v0.1")

    while True:

        sample = capture.read()

        print(sample)

        time.sleep(0.5)


if __name__ == "__main__":
    main()
import time

from wisense.scanner import WifiScanner


def main():

    scanner = WifiScanner()

    while True:

        print("=" * 50)

        networks = scanner.scan()

        for network in networks:

            print(

                f"{network['ssid']:<25}"

                f"{network['signal']:>5} dBm"

            )

        time.sleep(5)


if __name__ == "__main__":
    main()
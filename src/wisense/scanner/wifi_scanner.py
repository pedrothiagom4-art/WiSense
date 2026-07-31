from pywifi import PyWiFi


class WifiScanner:

    def __init__(self):

        wifi = PyWiFi()

        self.interface = wifi.interfaces()[0]

    def scan(self):

        self.interface.scan()

        results = self.interface.scan_results()

        networks = []

        for network in results:

            networks.append({

                "ssid": network.ssid,

                "bssid": network.bssid,

                "signal": network.signal,

                "frequency": network.freq,

            })

        return networks
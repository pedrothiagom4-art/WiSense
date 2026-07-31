import subprocess


def get_wifi_info():
    try:
        resultado = subprocess.check_output(
            ["nmcli", "-t", "-f", "ACTIVE,SSID,SIGNAL", "dev", "wifi"],
            text=True
        )

        for linha in resultado.splitlines():
            if linha.startswith("yes:"):
                _, ssid, signal = linha.split(":")
                return {
                    "ssid": ssid,
                    "signal": signal
                }
    
    except Exception as erro:
        print(erro)

    return None


if __name__ == "__main__":
    info = get_wifi_info()

    if info:
        print(f"Rede: {info['ssid']}")
        print(f"Sinal: {info['signal']}%")
    else:
        print("Nenhuma rede encontrada.")
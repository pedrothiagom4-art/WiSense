import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

from wisense.simulation import SignalSimulator

simulator = SignalSimulator()

x = []
y = []

fig, ax = plt.subplots()

def update(frame):

    sample = simulator.generate()

    x.append(len(x))
    y.append(sample.rssi)

    if len(x) > 100:
        x.pop(0)
        y.pop(0)

    ax.clear()

    ax.plot(x, y)

    ax.set_ylim(-80, -30)

    ax.set_title("WiSense - RSSI")

    ax.set_ylabel("dBm")

    ax.set_xlabel("Tempo")


ani = FuncAnimation(
    fig,
    update,
    interval=200,
    cache_frame_data=False
)

plt.show()
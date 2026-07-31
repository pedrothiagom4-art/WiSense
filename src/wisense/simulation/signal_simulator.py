from datetime import datetime
import random

from wisense.models import SignalSample


class SignalSimulator:

    def __init__(self):

        self.base_rssi = -45

        self.noise = 2

        self.movement_probability = 0.08

    def generate(self):

        movement = random.random() < self.movement_probability

        rssi = self.base_rssi + random.uniform(
            -self.noise,
            self.noise
        )

        if movement:

            rssi -= random.uniform(8, 18)

        return SignalSample(

            timestamp=datetime.now(),

            rssi=rssi,

            movement=movement

        )
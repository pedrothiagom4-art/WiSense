import random


class NoiseGenerator:

    def __init__(
        self,
        amplitude: float = 2.0,
        seed: int | None = None,
    ) -> None:

        self.amplitude = amplitude
        self.random = random.Random(seed)

    def generate(self) -> float:

        return self.random.uniform(
            -self.amplitude,
            self.amplitude,
        )
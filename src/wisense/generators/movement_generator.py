import random


class MovementGenerator:

    def __init__(
        self,
        probability: float = 0.08,
        seed: int | None = None,
    ) -> None:

        self.probability = probability
        self.random = random.Random(seed)

    def detect(self) -> bool:

        return (
            self.random.random()
            < self.probability
        )
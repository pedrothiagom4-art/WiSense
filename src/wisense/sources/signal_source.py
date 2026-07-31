from __future__ import annotations

from abc import ABC, abstractmethod

from wisense.models import SignalSample


class SignalSource(ABC):
    """
    Interface para qualquer fonte de sinal do WiSense.
    """

    @abstractmethod
    def read(self) -> SignalSample:
        """
        Retorna uma nova amostra de sinal.
        """
        raise NotImplementedError
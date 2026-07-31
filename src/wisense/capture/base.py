from __future__ import annotations

from abc import ABC, abstractmethod

from wisense.models import SignalSample


class CaptureEngine(ABC):
    """
    Interface para qualquer fonte de dados do WiSense.
    """

    @abstractmethod
    def read(self) -> SignalSample:
        """
        Retorna uma nova amostra.
        """
        raise NotImplementedError
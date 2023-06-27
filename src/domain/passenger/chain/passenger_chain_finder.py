from abc import ABC, abstractmethod
from typing import Optional

from domain.passenger.chain.passenger_chain import PassengerChain


class PassengerChainFinder(ABC):
    @abstractmethod
    def find_by_passenger_id(self, passenger_id: str) -> Optional[PassengerChain]:
        pass

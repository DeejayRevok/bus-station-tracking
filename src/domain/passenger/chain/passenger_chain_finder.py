from typing import Optional, Protocol

from domain.passenger.chain.passenger_chain import PassengerChain


class PassengerChainFinder(Protocol):
    def find_by_passenger_id(self, passenger_id: str) -> Optional[PassengerChain]:
        ...

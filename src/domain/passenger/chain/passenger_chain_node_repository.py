from typing import Protocol

from domain.passenger.chain.passenger_chain_node import PassengerChainNode


class PassengerChainNodeRepository(Protocol):
    def save(self, passenger_chain_node: PassengerChainNode) -> None:
        ...

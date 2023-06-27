from abc import ABC, abstractmethod

from domain.passenger.chain.passenger_chain_node import PassengerChainNode


class PassengerChainNodeRepository(ABC):
    @abstractmethod
    def save(self, passenger_chain_node: PassengerChainNode) -> None:
        pass

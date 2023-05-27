from dataclasses import dataclass
from typing import List, Tuple

from domain.passenger.chain.passenger_chain_node import PassengerChainNode


@dataclass
class PassengerChain:
    edges: List[Tuple[PassengerChainNode, PassengerChainNode]]

from dataclasses import dataclass
from typing import Optional

from domain.passenger.chain.passenger_chain_node_type import PassengerChainNodeType


@dataclass(frozen=True)
class PassengerChainNode:
    id: str
    name: str
    type: PassengerChainNodeType
    root_passenger_id: Optional[str]

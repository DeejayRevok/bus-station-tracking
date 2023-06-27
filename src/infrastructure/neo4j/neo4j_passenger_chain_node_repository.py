from domain.passenger.chain.passenger_chain_node import PassengerChainNode
from domain.passenger.chain.passenger_chain_node_repository import PassengerChainNodeRepository
from infrastructure.neo4j.models.passenger import Passenger


class Neo4jPassengerChainNodeRepository(PassengerChainNodeRepository):
    def save(self, passenger_chain_node: PassengerChainNode) -> None:
        passenger_node = Passenger(
            passenger_id=passenger_chain_node.id, name=passenger_chain_node.name, type=passenger_chain_node.type.value
        )
        passenger_node.save()

        self.__associate_root_passenger(passenger_chain_node, passenger_node)

    def __associate_root_passenger(self, passenger_chain_node: PassengerChainNode, passenger_node: Passenger) -> None:
        if passenger_chain_node.root_passenger_id is None:
            return

        root_passenger_node = Passenger.nodes.get(passenger_id=passenger_chain_node.root_passenger_id)
        passenger_node.root_passenger.connect(root_passenger_node)

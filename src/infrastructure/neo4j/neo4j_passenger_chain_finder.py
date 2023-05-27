from typing import Final, Optional, Set

from domain.passenger.chain.passenger_chain import PassengerChain
from domain.passenger.chain.passenger_chain_node import PassengerChainNode
from domain.passenger.chain.passenger_chain_node_type import PassengerChainNodeType
from infrastructure.neo4j.models.passenger import Passenger


class Neo4jPassengerChainFinder:
    __GRAPH_QUERY: Final[
        str
    ] = """
        MATCH path = (startNode)-[*]-(endNode)
        WHERE id(startNode) = $self
        RETURN path;
        """

    def find_by_passenger_id(self, passenger_id: str) -> Optional[PassengerChain]:
        passenger = Passenger.nodes.get_or_none(passenger_id=passenger_id)
        if passenger is None:
            return None

        result, _ = passenger.cypher(self.__GRAPH_QUERY)
        chain_graph = PassengerChain(edges=[])
        added_relationships: Set[str] = set()
        for paths in result:
            for path in paths:
                for relationship in path.relationships:
                    start_passenger = Passenger.inflate(relationship.start_node)
                    end_passenger = Passenger.inflate(relationship.end_node)

                    relationship_id = f"{start_passenger.passenger_id}-{end_passenger.passenger_id}"
                    if relationship_id in added_relationships:
                        continue

                    self.__add_edge_to_chain(start_passenger, end_passenger, chain_graph)
                    added_relationships.add(f"{start_passenger.passenger_id}-{end_passenger.passenger_id}")

        return chain_graph

    def __add_edge_to_chain(self, start_passenger: Passenger, end_passenger: Passenger, chain: PassengerChain) -> None:
        start_passenger_chain_graph_node = PassengerChainNode(
            id=start_passenger.passenger_id,
            name=start_passenger.name,
            root_passenger_id=None,
            type=PassengerChainNodeType(start_passenger.type),
        )
        end_passenger_chain_graph_node = PassengerChainNode(
            id=end_passenger.passenger_id,
            name=end_passenger.name,
            root_passenger_id=None,
            type=PassengerChainNodeType(end_passenger.type),
        )
        chain.edges.append((start_passenger_chain_graph_node, end_passenger_chain_graph_node))

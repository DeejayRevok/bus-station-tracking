from pypendency.builder import container_builder
from pypendency.definition import Definition


def load() -> None:
    container_builder.set_definition(
        Definition(
            "infrastructure.neo4j.neo4j_passenger_chain_finder.Neo4jPassengerChainFinder",
            "infrastructure.neo4j.neo4j_passenger_chain_finder.Neo4jPassengerChainFinder",
        )
    )
    container_builder.set_definition(
        Definition(
            "infrastructure.neo4j.neo4j_passenger_chain_node_repository.Neo4jPassengerChainNodeRepository",
            "infrastructure.neo4j.neo4j_passenger_chain_node_repository.Neo4jPassengerChainNodeRepository",
        )
    )

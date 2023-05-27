from pypendency.argument import Argument
from pypendency.builder import container_builder
from pypendency.definition import Definition


def load() -> None:
    container_builder.set_definition(
        Definition(
            "application.get_passenger_chain.get_passenger_chain_query_handler.GetPassengerChainQueryHandler",
            "application.get_passenger_chain.get_passenger_chain_query_handler.GetPassengerChainQueryHandler",
            [Argument.no_kw_argument("@infrastructure.neo4j.neo4j_passenger_chain_finder.Neo4jPassengerChainFinder")],
        )
    )

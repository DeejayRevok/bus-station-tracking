from bus_station.query_terminal.query_handler_registry import QueryHandlerRegistry
from pypendency.builder import container_builder


def register() -> None:
    registry: QueryHandlerRegistry = container_builder.get(
        "bus_station.query_terminal.query_handler_registry.QueryHandlerRegistry"
    )
    query_handler_fqns = [
        "application.get_command_trackings.get_command_trackings_query_handler.GetCommandTrackingsQueryHandler",
        "application.get_event_trackings.get_event_trackings_query_handler.GetEventTrackingsQueryHandler",
        "application.get_query_trackings.get_query_trackings_query_handler.GetQueryTrackingsQueryHandler",
        "application.get_passenger_chain.get_passenger_chain_query_handler.GetPassengerChainQueryHandler",
    ]

    for query_handler_fqn in query_handler_fqns:
        registry.register(query_handler_fqn)

from bus_station.query_terminal.registry.query_registry import QueryRegistry
from pypendency.builder import container_builder


def register() -> None:
    registry: QueryRegistry = container_builder.get(
        "bus_station.query_terminal.registry.in_memory_query_registry.InMemoryQueryRegistry"
    )
    query_handler_fqns = [
        "application.get_command_trackings.get_command_trackings_query_handler.GetCommandTrackingsQueryHandler",
        "application.get_event_trackings.get_event_trackings_query_handler.GetEventTrackingsQueryHandler",
        "application.get_query_trackings.get_query_trackings_query_handler.GetQueryTrackingsQueryHandler",
    ]

    for query_handler_fqn in query_handler_fqns:
        handler = container_builder.get(query_handler_fqn)
        registry.register(handler, handler)

from bus_station.query_terminal.query_handler_registry import QueryHandlerRegistry
from yandil.container import default_container

from application.get_command_trackings.get_command_trackings_query_handler import GetCommandTrackingsQueryHandler
from application.get_event_trackings.get_event_trackings_query_handler import GetEventTrackingsQueryHandler
from application.get_passenger_chain.get_passenger_chain_query_handler import GetPassengerChainQueryHandler
from application.get_query_trackings.get_query_trackings_query_handler import GetQueryTrackingsQueryHandler


def register() -> None:
    registry = default_container[QueryHandlerRegistry]
    query_handlers = [
        GetCommandTrackingsQueryHandler,
        GetEventTrackingsQueryHandler,
        GetQueryTrackingsQueryHandler,
        GetPassengerChainQueryHandler,
    ]

    for query_handler in query_handlers:
        registry.register(default_container[query_handler])

from logging import Logger

from bus_station.query_terminal.middleware.implementations.logging_query_middleware import LoggingQueryMiddleware
from bus_station.query_terminal.middleware.implementations.timing_query_middleware import TimingQueryMiddleware
from bus_station.query_terminal.middleware.query_middleware_receiver import QueryMiddlewareReceiver
from yandil.container import default_container


def load() -> None:
    query_middleware_receiver = default_container[QueryMiddlewareReceiver]
    query_middleware_receiver.add_middleware_definition(LoggingQueryMiddleware, default_container[Logger], lazy=False)
    query_middleware_receiver.add_middleware_definition(TimingQueryMiddleware, default_container[Logger], lazy=True)

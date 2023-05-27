from pypendency.argument import Argument
from pypendency.builder import container_builder
from pypendency.definition import Definition


def load() -> None:
    container_builder.set_definition(
        Definition(
            "bus_station.query_terminal.middleware.query_middleware_receiver.QueryMiddlewareReceiver",
            "bus_station.query_terminal.middleware.query_middleware_receiver.QueryMiddlewareReceiver",
        )
    )
    container_builder.set_definition(
        Definition(
            "bus_station.query_terminal.query_handler_registry.QueryHandlerRegistry",
            "bus_station.query_terminal.query_handler_registry.QueryHandlerRegistry",
            [
                Argument(
                    "bus_stop_resolver",
                    "@bus_station.bus_stop.resolvers.pypendency_bus_stop_resolver.PypendencyBusStopResolver",
                ),
            ],
        )
    )
    container_builder.set_definition(
        Definition(
            "bus_station.query_terminal.bus.synchronous.sync_query_bus.SyncQueryBus",
            "bus_station.query_terminal.bus.synchronous.sync_query_bus.SyncQueryBus",
            [
                Argument.no_kw_argument("@bus_station.query_terminal.query_handler_registry.QueryHandlerRegistry"),
                Argument.no_kw_argument(
                    "@bus_station.query_terminal.middleware.query_middleware_receiver.QueryMiddlewareReceiver"
                ),
            ],
        )
    )

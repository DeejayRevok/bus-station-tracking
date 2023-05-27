from pypendency.argument import Argument
from pypendency.builder import container_builder
from pypendency.definition import Definition


def load() -> None:
    container_builder.set_definition(
        Definition(
            "bus_station.event_terminal.middleware.event_middleware_receiver.EventMiddlewareReceiver",
            "bus_station.event_terminal.middleware.event_middleware_receiver.EventMiddlewareReceiver",
        )
    )
    container_builder.set_definition(
        Definition(
            "bus_station.event_terminal.event_consumer_registry.EventConsumerRegistry",
            "bus_station.event_terminal.event_consumer_registry.EventConsumerRegistry",
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
            "bus_station.event_terminal.bus.asynchronous.threaded_event_bus.ThreadedEventBus",
            "bus_station.event_terminal.bus.asynchronous.threaded_event_bus.ThreadedEventBus",
            [
                Argument.no_kw_argument("@bus_station.event_terminal.event_consumer_registry.EventConsumerRegistry"),
                Argument.no_kw_argument(
                    "@bus_station.event_terminal.middleware.event_middleware_receiver.EventMiddlewareReceiver"
                ),
            ],
        )
    )

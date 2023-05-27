from pypendency.argument import Argument
from pypendency.builder import container_builder
from pypendency.definition import Definition


def load() -> None:
    container_builder.set_definition(
        Definition(
            "bus_station.command_terminal.middleware.command_middleware_receiver.CommandMiddlewareReceiver",
            "bus_station.command_terminal.middleware.command_middleware_receiver.CommandMiddlewareReceiver",
        )
    )
    container_builder.set_definition(
        Definition(
            "bus_station.command_terminal.command_handler_registry.CommandHandlerRegistry",
            "bus_station.command_terminal.command_handler_registry.CommandHandlerRegistry",
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
            "bus_station.command_terminal.bus.synchronous.sync_command_bus.SyncCommandBus",
            "bus_station.command_terminal.bus.synchronous.sync_command_bus.SyncCommandBus",
            [
                Argument.no_kw_argument(
                    "@bus_station.command_terminal.command_handler_registry.CommandHandlerRegistry"
                ),
                Argument.no_kw_argument(
                    "@bus_station.command_terminal.middleware.command_middleware_receiver.CommandMiddlewareReceiver"
                ),
            ],
        )
    )

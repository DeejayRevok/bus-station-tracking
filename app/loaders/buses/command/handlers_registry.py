from bus_station.command_terminal.registry.command_registry import CommandRegistry
from pypendency.builder import container_builder


def register() -> None:
    registry: CommandRegistry = container_builder.get(
        "bus_station.command_terminal.registry.in_memory_command_registry.InMemoryCommandRegistry"
    )

    command_handler_fqns = [
        "application.save_command_tracking.save_command_tracking_command_handler.SaveCommandTrackingCommandHandler",
        "application.save_event_tracking.save_event_tracking_command_handler.SaveEventTrackingCommandHandler",
        "application.save_query_tracking.save_query_tracking_command_handler.SaveQueryTrackingCommandHandler",
    ]
    for command_handler_fqn in command_handler_fqns:
        command_handler = container_builder.get(command_handler_fqn)
        registry.register(command_handler, command_handler)

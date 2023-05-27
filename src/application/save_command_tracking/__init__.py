from pypendency.argument import Argument
from pypendency.builder import container_builder
from pypendency.definition import Definition


def load() -> None:
    container_builder.set_definition(
        Definition(
            "application.save_command_tracking.save_command_tracking_command_handler.SaveCommandTrackingCommandHandler",
            "application.save_command_tracking.save_command_tracking_command_handler.SaveCommandTrackingCommandHandler",
            [
                Argument.no_kw_argument(
                    "@infrastructure.sqlalchemy.repositories"
                    ".sqlalchemy_command_tracking_repository.SQLAlchemyCommandTrackingRepository"
                ),
                Argument.no_kw_argument(
                    "@bus_station.event_terminal.bus.asynchronous.threaded_event_bus.ThreadedEventBus"
                ),
            ],
        )
    )

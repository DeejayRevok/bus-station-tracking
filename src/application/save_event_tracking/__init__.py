from pypendency.argument import Argument
from pypendency.builder import container_builder
from pypendency.definition import Definition


def load() -> None:
    container_builder.set_definition(
        Definition(
            "application.save_event_tracking.save_event_tracking_command_handler.SaveEventTrackingCommandHandler",
            "application.save_event_tracking.save_event_tracking_command_handler.SaveEventTrackingCommandHandler",
            [
                Argument.no_kw_argument(
                    "@infrastructure.sqlalchemy.repositories"
                    ".sqlalchemy_event_tracking_repository.SQLAlchemyEventTrackingRepository"
                ),
                Argument.no_kw_argument(
                    "@bus_station.event_terminal.bus.asynchronous.threaded_event_bus.ThreadedEventBus"
                ),
            ],
        )
    )

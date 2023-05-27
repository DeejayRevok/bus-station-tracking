from datetime import datetime
from typing import Optional

from bus_station.command_terminal.command_handler import CommandHandler
from bus_station.event_terminal.bus.event_bus import EventBus

from application.save_event_tracking.save_event_tracking_command import SaveEventTrackingCommand
from domain.event.event_tracking import EventTracking
from domain.event.event_tracking_created_event import EventTrackingCreatedEvent
from domain.event.event_tracking_repository import EventTrackingRepository
from domain.event.missing_event_tracking_start_exception import MissingEventTrackingStartException


class SaveEventTrackingCommandHandler(CommandHandler):
    def __init__(self, event_tracking_repository: EventTrackingRepository, event_bus: EventBus):
        self.__event_tracking_repository = event_tracking_repository
        self.__event_bus = event_bus

    def handle(self, command: SaveEventTrackingCommand) -> None:
        existing_event_tracking = self.__event_tracking_repository.find_by_id(command.id)
        if existing_event_tracking is None:
            self.__validate_command_for_non_existing(command)
            event_tracking = EventTracking(
                id=command.id,
                root_passenger_id=command.passenger_root_id,
                name=command.name,
                executor_name=command.executor_name,
                data=command.data,
                execution_start=self.__get_datetime_from_str(command.execution_start),
                execution_end=self.__get_datetime_from_str(command.execution_end),
                success=command.success,
            )
            self.__event_tracking_repository.save(event_tracking)
            self.__publish_creation_event(event_tracking)
            return

        existing_event_tracking.execution_end = self.__get_datetime_from_str(command.execution_end)
        existing_event_tracking.success = command.success
        self.__event_tracking_repository.save(existing_event_tracking)

    def __validate_command_for_non_existing(self, command: SaveEventTrackingCommand) -> None:
        if command.execution_start is None:
            raise MissingEventTrackingStartException(command.id)

    def __get_datetime_from_str(self, datetime_str: Optional[str]) -> Optional[datetime]:
        if datetime_str is None:
            return None
        return datetime.fromisoformat(datetime_str)

    def __publish_creation_event(self, event_tracking: EventTracking) -> None:
        self.__event_bus.transport(
            EventTrackingCreatedEvent(
                id=event_tracking.id,
                tracking_root_passenger_id=event_tracking.root_passenger_id,
                name=event_tracking.name,
                executor_name=event_tracking.executor_name,
                data=event_tracking.data,
            )
        )

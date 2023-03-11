from datetime import datetime
from typing import Optional

from bus_station.command_terminal.command_handler import CommandHandler

from application.save_event_tracking.save_event_tracking_command import SaveEventTrackingCommand
from domain.event.event_tracking import EventTracking
from domain.event.event_tracking_repository import EventTrackingRepository
from domain.event.missing_event_tracking_start_exception import MissingEventTrackingStartException


class SaveEventTrackingCommandHandler(CommandHandler):
    def __init__(self, event_tracking_repository: EventTrackingRepository):
        self.__event_tracking_repository = event_tracking_repository

    def handle(self, command: SaveEventTrackingCommand) -> None:
        existing_event_tracking = self.__event_tracking_repository.find_by_id(command.id)
        if existing_event_tracking is None:
            self.__validate_command_for_non_existing(command)
            event_tracking = EventTracking(
                id=command.id,
                name=command.name,
                executor_name=command.executor_name,
                data=command.data,
                execution_start=self.__get_datetime_from_str(command.execution_start),
                execution_end=self.__get_datetime_from_str(command.execution_end),
                success=command.success,
            )
            self.__event_tracking_repository.save(event_tracking)
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

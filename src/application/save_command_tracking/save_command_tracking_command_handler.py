from datetime import datetime
from typing import Optional

from bus_station.command_terminal.command_handler import CommandHandler
from bus_station.event_terminal.bus.event_bus import EventBus

from application.save_command_tracking.save_command_tracking_command import SaveCommandTrackingCommand
from domain.command.command_tracking import CommandTracking
from domain.command.command_tracking_created_event import CommandTrackingCreatedEvent
from domain.command.command_tracking_repository import CommandTrackingRepository
from domain.command.missing_command_tracking_start_exception import MissingCommandTrackingStartException


class SaveCommandTrackingCommandHandler(CommandHandler):
    def __init__(self, command_tracking_repository: CommandTrackingRepository, event_bus: EventBus):
        self.__command_tracking_repository = command_tracking_repository
        self.__event_bus = event_bus

    def handle(self, command: SaveCommandTrackingCommand) -> None:
        existing_command_tracking = self.__command_tracking_repository.find_by_id(command.id)

        if existing_command_tracking is None:
            self.__validate_command_for_non_existing(command)
            command_tracking = CommandTracking(
                id=command.id,
                root_passenger_id=command.passenger_root_id,
                name=command.name,
                executor_name=command.executor_name,
                data=command.data,
                execution_start=self.__get_datetime_from_str(command.execution_start),
                execution_end=self.__get_datetime_from_str(command.execution_end),
                success=command.success,
            )
            self.__command_tracking_repository.save(command_tracking)
            self.__publish_creation_event(command_tracking)
            return

        existing_command_tracking.execution_end = self.__get_datetime_from_str(command.execution_end)
        existing_command_tracking.success = command.success
        self.__command_tracking_repository.save(existing_command_tracking)

    def __validate_command_for_non_existing(self, command: SaveCommandTrackingCommand) -> None:
        if command.execution_start is None:
            raise MissingCommandTrackingStartException(command.id)

    def __get_datetime_from_str(self, datetime_str: Optional[str]) -> Optional[datetime]:
        if datetime_str is None:
            return None
        return datetime.fromisoformat(datetime_str)

    def __publish_creation_event(self, command_tracking: CommandTracking) -> None:
        self.__event_bus.transport(
            CommandTrackingCreatedEvent(
                id=command_tracking.id,
                tracking_root_passenger_id=command_tracking.root_passenger_id,
                name=command_tracking.name,
                executor_name=command_tracking.executor_name,
                data=command_tracking.data,
            )
        )

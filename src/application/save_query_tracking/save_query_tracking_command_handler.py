from datetime import datetime
from typing import Optional

from bus_station.command_terminal.command_handler import CommandHandler

from application.save_query_tracking.save_query_tracking_command import SaveQueryTrackingCommand
from domain.query.missing_query_tracking_start_exception import MissingQueryTrackingStartException
from domain.query.query_tracking import QueryTracking
from domain.query.query_tracking_repository import QueryTrackingRepository


class SaveQueryTrackingCommandHandler(CommandHandler):
    def __init__(self, query_tracking_repository: QueryTrackingRepository):
        self.__query_tracking_repository = query_tracking_repository

    def handle(self, command: SaveQueryTrackingCommand) -> None:
        existing_query_tracking = self.__query_tracking_repository.find_by_id(command.id)
        if existing_query_tracking is None:
            self.__validate_command_for_non_existing(command)
            query_tracking = QueryTracking(
                id=command.id,
                name=command.name,
                executor_name=command.executor_name,
                data=command.data,
                execution_start=self.__get_datetime_from_str(command.execution_start),
                execution_end=self.__get_datetime_from_str(command.execution_end),
                success=command.success,
                response_data=command.response_data,
            )
            self.__query_tracking_repository.save(query_tracking)
            return

        existing_query_tracking.execution_end = self.__get_datetime_from_str(command.execution_end)
        existing_query_tracking.success = command.success
        existing_query_tracking.response_data = command.response_data
        self.__query_tracking_repository.save(existing_query_tracking)

    def __validate_command_for_non_existing(self, command: SaveQueryTrackingCommand) -> None:
        if command.execution_start is None:
            raise MissingQueryTrackingStartException(command.id)

    def __get_datetime_from_str(self, datetime_str: Optional[str]) -> Optional[datetime]:
        if datetime_str is None:
            return None
        return datetime.fromisoformat(datetime_str)

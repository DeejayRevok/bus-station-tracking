from datetime import datetime
from typing import Optional

from bus_station.query_terminal.query_handler import QueryHandler
from bus_station.query_terminal.query_response import QueryResponse

from application.get_query_trackings.get_query_trackings_query import GetQueryTrackingsQuery
from domain.passenger.find_passenger_tracking_criteria import FindPassengerTrackingCriteria
from domain.passenger.process_status import ProcessStatus
from domain.query.query_tracking_repository import QueryTrackingRepository


class GetQueryTrackingsQueryHandler(QueryHandler):
    def __init__(self, query_tracking_repository: QueryTrackingRepository):
        self.__query_tracking_repository = query_tracking_repository

    def handle(self, query: GetQueryTrackingsQuery) -> QueryResponse:
        return QueryResponse(
            data=self.__query_tracking_repository.find_by_criteria(self.__get_criteria_from_query(query))
        )

    def __get_criteria_from_query(self, query: GetQueryTrackingsQuery) -> FindPassengerTrackingCriteria:
        return FindPassengerTrackingCriteria(
            from_execution_start=self.__str_to_datetime(query.from_execution_start),
            to_execution_start=self.__str_to_datetime(query.to_execution_start),
            process_status=self.__get_process_status_from_str(query.process_status),
        )

    def __str_to_datetime(self, datetime_str: Optional[str]) -> Optional[datetime]:
        if datetime_str is None:
            return None

        return datetime.fromisoformat(datetime_str)

    def __get_process_status_from_str(self, success_str: Optional[str]) -> Optional[ProcessStatus]:
        if success_str is None:
            return None
        return ProcessStatus(success_str)

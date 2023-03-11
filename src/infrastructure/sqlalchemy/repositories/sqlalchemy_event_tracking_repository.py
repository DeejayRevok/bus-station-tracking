from typing import Iterable, Optional

from sqlalchemy.orm import Query, Session

from domain.event.event_tracking import EventTracking
from domain.event.event_tracking_repository import EventTrackingRepository
from domain.passenger.find_passenger_tracking_criteria import FindPassengerTrackingCriteria
from domain.passenger.process_status import ProcessStatus


class SQLAlchemyEventTrackingRepository(EventTrackingRepository):
    def __init__(
        self,
        sqlalchemy_session: Session,
    ):
        self.__session = sqlalchemy_session

    def save(self, passenger_tracking: EventTracking) -> None:
        try:
            self.__session.merge(passenger_tracking)
            self.__session.commit()
        except Exception as ex:
            self.__session.rollback()
            raise ex

    def find_by_id(self, passenger_tracking_id: str) -> Optional[EventTracking]:
        return self.__session.query(EventTracking).filter_by(id=passenger_tracking_id).one_or_none()

    def find_by_criteria(self, criteria: FindPassengerTrackingCriteria) -> Iterable[EventTracking]:
        query = self.__session.query(EventTracking)

        if criteria.from_execution_start is not None:
            query = query.filter(EventTracking.execution_start >= criteria.from_execution_start)

        if criteria.to_execution_start is not None:
            query = query.filter(EventTracking.execution_start < criteria.to_execution_start)

        if criteria.process_status is not None:
            query = self.__apply_process_status_filter(query, criteria.process_status)

        return query

    def __apply_process_status_filter(self, query: Query, process_status: ProcessStatus) -> Query:
        match process_status:
            case ProcessStatus.SUCCESS:
                return query.filter_by(success=True)
            case ProcessStatus.FAILURE:
                return query.filter_by(success=False)
            case ProcessStatus.UNPROCESSED:
                return query.filter_by(success=None)
            case _:
                raise NotImplementedError("Process status filter not supported")

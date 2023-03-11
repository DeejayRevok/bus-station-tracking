from abc import ABC

from domain.passenger.passenger_tracking_repository import PassengerTrackingRepository
from domain.query.query_tracking import QueryTracking


class QueryTrackingRepository(PassengerTrackingRepository[QueryTracking], ABC):
    pass

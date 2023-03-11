from abc import ABC

from domain.event.event_tracking import EventTracking
from domain.passenger.passenger_tracking_repository import PassengerTrackingRepository


class EventTrackingRepository(PassengerTrackingRepository[EventTracking], ABC):
    pass

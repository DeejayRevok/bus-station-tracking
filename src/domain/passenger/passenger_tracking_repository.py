from abc import ABC, abstractmethod
from typing import Generic, Optional, Sequence, TypeVar

from domain.passenger.find_passenger_tracking_criteria import FindPassengerTrackingCriteria
from domain.passenger.passenger_tracking import PassengerTracking

T = TypeVar("T", bound=PassengerTracking)


class PassengerTrackingRepository(Generic[T], ABC):
    @abstractmethod
    def save(self, passenger_tracking: T) -> None:
        pass

    @abstractmethod
    def find_by_id(self, passenger_tracking_id: str) -> Optional[T]:
        pass

    @abstractmethod
    def find_by_criteria(self, criteria: FindPassengerTrackingCriteria) -> Sequence[T]:
        pass

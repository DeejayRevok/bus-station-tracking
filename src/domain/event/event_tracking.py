from dataclasses import dataclass

from domain.passenger.passenger_tracking import PassengerTracking


@dataclass
class EventTracking(PassengerTracking):
    pass

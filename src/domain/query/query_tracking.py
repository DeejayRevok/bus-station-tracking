from dataclasses import dataclass, field
from typing import Optional

from domain.passenger.passenger_tracking import PassengerTracking


@dataclass
class QueryTracking(PassengerTracking):
    response_data: Optional[dict] = field(default_factory=lambda: None)

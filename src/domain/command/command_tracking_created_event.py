from dataclasses import dataclass
from typing import Optional


@dataclass(frozen=True)
class CommandTrackingCreatedEvent:
    id: str
    tracking_root_passenger_id: Optional[str]
    name: str
    executor_name: str
    data: dict

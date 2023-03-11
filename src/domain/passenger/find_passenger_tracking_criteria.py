from dataclasses import dataclass
from datetime import datetime
from typing import Optional

from domain.passenger.process_status import ProcessStatus


@dataclass(frozen=True)
class FindPassengerTrackingCriteria:
    from_execution_start: Optional[datetime] = None
    to_execution_start: Optional[datetime] = None
    process_status: Optional[ProcessStatus] = None

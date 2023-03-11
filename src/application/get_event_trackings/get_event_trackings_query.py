from dataclasses import dataclass
from typing import Optional

from bus_station.query_terminal.query import Query


@dataclass(frozen=True)
class GetEventTrackingsQuery(Query):
    from_execution_start: Optional[str] = None
    to_execution_start: Optional[str] = None
    process_status: Optional[str] = None

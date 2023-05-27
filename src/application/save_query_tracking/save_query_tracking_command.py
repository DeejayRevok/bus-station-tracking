from dataclasses import dataclass
from typing import Optional

from bus_station.command_terminal.command import Command


@dataclass(frozen=True)
class SaveQueryTrackingCommand(Command):
    id: str
    passenger_root_id: Optional[str]
    name: str
    executor_name: str
    data: dict
    execution_start: Optional[str]
    execution_end: Optional[str]
    success: Optional[bool]
    response_data: Optional[dict]

from __future__ import annotations

from abc import ABC, abstractmethod
from datetime import datetime
from typing import Optional

from bus_station.query_terminal.query import Query


class FetchQueryBuilder(ABC):
    def __init__(self):
        self._from_execution_start: Optional[datetime] = None
        self._to_execution_start: Optional[datetime] = None
        self._process_status: Optional[str] = None

    def with_from_execution_start(self, from_execution_start: datetime) -> FetchQueryBuilder:
        self._from_execution_start = from_execution_start
        return self

    def with_to_execution_start(self, to_execution_start: datetime) -> FetchQueryBuilder:
        self._to_execution_start = to_execution_start
        return self

    def with_process_status(self, process_status: str) -> FetchQueryBuilder:
        self._process_status = process_status
        return self

    @abstractmethod
    def build(self) -> Query:
        pass

    def _datetime_to_str(self, datetime_instance: Optional[datetime]) -> Optional[str]:
        if datetime_instance is None:
            return None
        return datetime_instance.isoformat()

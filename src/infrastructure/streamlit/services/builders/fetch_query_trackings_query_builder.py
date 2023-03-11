from __future__ import annotations

from application.get_query_trackings.get_query_trackings_query import GetQueryTrackingsQuery
from infrastructure.streamlit.services.builders.fetch_query_builder import FetchQueryBuilder


class FetchQueryTrackingsQueryBuilder(FetchQueryBuilder):
    def build(self) -> GetQueryTrackingsQuery:
        return GetQueryTrackingsQuery(
            from_execution_start=self._datetime_to_str(self._from_execution_start),
            to_execution_start=self._datetime_to_str(self._to_execution_start),
            process_status=self._process_status,
        )

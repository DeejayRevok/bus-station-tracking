from application.get_event_trackings.get_event_trackings_query import GetEventTrackingsQuery
from infrastructure.streamlit.services.builders.fetch_query_builder import FetchQueryBuilder


class FetchEventTrackingsQueryBuilder(FetchQueryBuilder):
    def build(self) -> GetEventTrackingsQuery:
        return GetEventTrackingsQuery(
            from_execution_start=self._datetime_to_str(self._from_execution_start),
            to_execution_start=self._datetime_to_str(self._to_execution_start),
            process_status=self._process_status,
        )

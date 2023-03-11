from application.get_command_trackings.get_command_trackings_query import GetCommandTrackingsQuery
from infrastructure.streamlit.services.builders.fetch_query_builder import FetchQueryBuilder


class FetchCommandTrackingsQueryBuilder(FetchQueryBuilder):
    def build(self) -> GetCommandTrackingsQuery:
        return GetCommandTrackingsQuery(
            from_execution_start=self._datetime_to_str(self._from_execution_start),
            to_execution_start=self._datetime_to_str(self._to_execution_start),
            process_status=self._process_status,
        )

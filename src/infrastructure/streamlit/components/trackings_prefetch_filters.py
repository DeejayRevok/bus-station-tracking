from datetime import date, timedelta
from typing import Optional

from streamlit import sidebar


class TrackingsPrefetchFilters:
    def __init__(self, filters_id: str):
        self.__filters_id = filters_id
        self.__from_filter: Optional[date] = None
        self.__to_filter: Optional[date] = None
        self.__status_filter: Optional[str] = None

    @property
    def from_filter(self) -> Optional[date]:
        return self.__from_filter

    @property
    def to_filter(self) -> Optional[date]:
        return self.__to_filter

    @property
    def status_filter(self) -> Optional[str]:
        if self.__status_filter == "":
            return None
        return self.__status_filter

    def build(self):
        self.__build_status_filters()
        self.__build_execution_start_filters()

    def __build_execution_start_filters(self) -> None:
        today = date.today()
        from_column, to_column = sidebar.columns(2)
        self.__from_filter = from_column.date_input(
            "From start date", value=today - timedelta(days=15), key=f"{self.__filters_id}_from_start_date_filter"
        )
        self.__to_filter = to_column.date_input(
            "To start date", value=today + timedelta(days=1), key=f"{self.__filters_id}_to_start_date_filter"
        )

    def __build_status_filters(self) -> None:
        self.__status_filter = sidebar.selectbox(
            "Status", ["", "success", "failure", "unprocessed"], key=f"{self.__filters_id}_status_filter"
        )

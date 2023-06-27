from datetime import date, datetime
from typing import Optional

from bus_station.query_terminal.bus.synchronous.sync_query_bus import SyncQueryBus
from bus_station.query_terminal.query import Query
from pandas import DataFrame, to_datetime
from streamlit import spinner

from infrastructure.sqlalchemy.sqlalchemy_query_response_dataframe_transformer import (
    SQLAlchemyQueryResponseDataframeTransformer,
)
from infrastructure.streamlit.components.trackings_prefetch_filters import TrackingsPrefetchFilters
from infrastructure.streamlit.services.builders.fetch_query_builder import FetchQueryBuilder


class TrackingsDataService:
    def __init__(
        self,
        fetch_query_builder: FetchQueryBuilder,
        trackings_prefetch_filters: TrackingsPrefetchFilters,
        query_bus: Optional[SyncQueryBus] = None,
        response_dataframe_transformer: Optional[SQLAlchemyQueryResponseDataframeTransformer] = None,
    ):
        self.__query_bus = query_bus
        self.__response_dataframe_transformer = response_dataframe_transformer
        self.__fetch_query_builder = fetch_query_builder
        self.__prefetch_filters = trackings_prefetch_filters
        self.__trackings_dataframe: Optional[DataFrame] = None

    @property
    def trackings_dataframe(self) -> DataFrame:
        if self.__trackings_dataframe is None:
            self.__trackings_dataframe = self.__fetch_trackings_dataframe()
        return self.__trackings_dataframe

    def __fetch_trackings_dataframe(self) -> DataFrame:
        with spinner("Loading data..."):
            trackings_query_response = self.__query_bus.transport(self.__build_fetch_query())
            return self.__process_dataframe(self.__response_dataframe_transformer.transform(trackings_query_response))

    def __build_fetch_query(self) -> Query:
        self.__fetch_query_builder.with_from_execution_start(
            self.__date_to_datetime(self.__prefetch_filters.from_filter)
        )
        self.__fetch_query_builder.with_to_execution_start(self.__date_to_datetime(self.__prefetch_filters.to_filter))
        self.__fetch_query_builder.with_process_status(self.__prefetch_filters.status_filter)
        return self.__fetch_query_builder.build()

    def __date_to_datetime(self, date_instance: Optional[date]) -> Optional[datetime]:
        if date_instance is None:
            return None
        return datetime.combine(date_instance, datetime.min.time())

    def __process_dataframe(self, dataframe: DataFrame) -> DataFrame:
        dataframe["passenger_id"] = dataframe["id"]
        dataframe["execution_start"] = to_datetime(dataframe["execution_start"])
        dataframe["execution_end"] = to_datetime(dataframe["execution_end"])
        dataframe["execution_time(ms)"] = (dataframe["execution_end"] - dataframe["execution_start"]).astype(
            "timedelta64[ms]"
        )

        dataframe = dataframe[
            ["passenger_id", "execution_start", "name", "executor_name", "execution_time(ms)", "success", "data"]
        ]
        dataframe = dataframe.sort_values("execution_start", ascending=False)
        return dataframe

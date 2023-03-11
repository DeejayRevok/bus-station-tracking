from pandas import DataFrame, Grouper, concat
from streamlit import bar_chart, columns, set_page_config, title

from infrastructure.streamlit.components.trackings_postfetch_filters import TrackingsPostfetchFilters
from infrastructure.streamlit.components.trackings_prefetch_filters import TrackingsPrefetchFilters
from infrastructure.streamlit.components.trackings_table import TrackingsTable
from infrastructure.streamlit.services.builders.fetch_command_trackings_query_builder import (
    FetchCommandTrackingsQueryBuilder,
)
from infrastructure.streamlit.services.builders.fetch_event_trackings_query_builder import (
    FetchEventTrackingsQueryBuilder,
)
from infrastructure.streamlit.services.builders.fetch_query_trackings_query_builder import (
    FetchQueryTrackingsQueryBuilder,
)
from infrastructure.streamlit.services.trackings_data_service import TrackingsDataService

set_page_config(page_title="Bus station tracking", layout="wide")
title("Bus station tracking")


trackings_prefetch_filters = TrackingsPrefetchFilters("passenger")
trackings_prefetch_filters.build()


command_trackings_service = TrackingsDataService(FetchCommandTrackingsQueryBuilder(), trackings_prefetch_filters)
event_trackings_service = TrackingsDataService(FetchEventTrackingsQueryBuilder(), trackings_prefetch_filters)
query_trackings_service = TrackingsDataService(FetchQueryTrackingsQueryBuilder(), trackings_prefetch_filters)


passengers_tracking_dataframe = concat(
    [
        command_trackings_service.trackings_dataframe,
        event_trackings_service.trackings_dataframe,
        query_trackings_service.trackings_dataframe,
    ],
    ignore_index=True,
)
passengers_tracking_dataframe.sort_values("execution_start", ascending=False)


trackings_postfetch_filters = TrackingsPostfetchFilters(passengers_tracking_dataframe)
trackings_postfetch_filters.build()


command_trackings_dataframe = trackings_postfetch_filters.apply_filters(command_trackings_service.trackings_dataframe)
event_trackings_dataframe = trackings_postfetch_filters.apply_filters(event_trackings_service.trackings_dataframe)
query_trackings_dataframe = trackings_postfetch_filters.apply_filters(query_trackings_service.trackings_dataframe)

command_column, events_column, queries_column = columns(3)
command_column.metric("Commands", len(command_trackings_dataframe))
events_column.metric("Events", len(event_trackings_dataframe))
queries_column.metric("Queries", len(query_trackings_dataframe))


passengers_tracking_dataframe = trackings_postfetch_filters.apply_filters(passengers_tracking_dataframe)

TrackingsTable(passengers_tracking_dataframe).build()


def __group_dataframe_by_execution_start(dataframe: DataFrame, name: str) -> DataFrame:
    result_dataframe = (
        dataframe.groupby(Grouper(key="execution_start", freq="min"))["name"].count().reset_index(name=name)
    )
    result_dataframe = result_dataframe.set_index("execution_start")
    return result_dataframe


grouped_command_trackings_dataframe = __group_dataframe_by_execution_start(
    command_trackings_service.trackings_dataframe, "total_command_trackings"
)
grouped_event_trackings_dataframe = __group_dataframe_by_execution_start(
    event_trackings_service.trackings_dataframe, "total_event_trackings"
)
grouped_query_trackings_dataframe = __group_dataframe_by_execution_start(
    query_trackings_service.trackings_dataframe, "total_query_trackings"
)
total_grouped_trackings_dataframe = grouped_command_trackings_dataframe.join(
    grouped_event_trackings_dataframe, how="outer"
)
total_grouped_trackings_dataframe = total_grouped_trackings_dataframe.join(
    grouped_query_trackings_dataframe, how="outer"
)
bar_chart(
    total_grouped_trackings_dataframe, y=["total_command_trackings", "total_event_trackings", "total_query_trackings"]
)

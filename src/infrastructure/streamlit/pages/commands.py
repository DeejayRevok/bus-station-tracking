from streamlit import columns, set_page_config, title

from infrastructure.streamlit.components.tracking_data_view import TrackingDataView
from infrastructure.streamlit.components.trackings_error_chart import TrackingsErrorChart
from infrastructure.streamlit.components.trackings_execution_time_boxplot import TrackingsExecutionTimeBoxPlot
from infrastructure.streamlit.components.trackings_metrics_bar import TrackingsMetricsBar
from infrastructure.streamlit.components.trackings_postfetch_filters import TrackingsPostfetchFilters
from infrastructure.streamlit.components.trackings_prefetch_filters import TrackingsPrefetchFilters
from infrastructure.streamlit.components.trackings_table import TrackingsTable
from infrastructure.streamlit.components.trackings_total_chart import TrackingsTotalChart
from infrastructure.streamlit.services.builders.fetch_command_trackings_query_builder import (
    FetchCommandTrackingsQueryBuilder,
)
from infrastructure.streamlit.services.trackings_data_service import TrackingsDataService

set_page_config(page_title="Bus station tracking", layout="wide")
title("Commands")

trackings_prefetch_filters = TrackingsPrefetchFilters("command")
trackings_prefetch_filters.build()

trackings_service = TrackingsDataService(FetchCommandTrackingsQueryBuilder(), trackings_prefetch_filters)
trackings_dataframe = trackings_service.trackings_dataframe

trackings_postfetch_filters = TrackingsPostfetchFilters(trackings_dataframe)
trackings_postfetch_filters.build()

trackings_dataframe = trackings_postfetch_filters.apply_filters(trackings_dataframe)

TrackingsMetricsBar(trackings_dataframe).build()

trackings_table = TrackingsTable(trackings_dataframe)
trackings_table.build()

TrackingDataView(trackings_table).build()

TrackingsTotalChart(trackings_dataframe).build()

box_plot_column, error_chart_column = columns(2)
TrackingsExecutionTimeBoxPlot(trackings_dataframe).build(box_plot_column)
TrackingsErrorChart(trackings_dataframe).build(error_chart_column)

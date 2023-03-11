from __future__ import annotations

from pandas import DataFrame
from streamlit import columns


class TrackingsMetricsBar:
    def __init__(self, trackings_dataframe: DataFrame):
        self.__trackings_dataframe = trackings_dataframe

    def build(self) -> None:
        trackings_dataframe = self.__trackings_dataframe

        success_dataframe = trackings_dataframe[trackings_dataframe["success"]]
        errors_dataframe = trackings_dataframe[~trackings_dataframe["success"]]
        unprocessed_dataframe = trackings_dataframe[trackings_dataframe.success.isnull()]
        execution_time_mean = round(trackings_dataframe["execution_time(ms)"].mean(), 2)

        succes_number_column, error_number_column, unprocessed_number_column, execution_mean_column = columns(4)
        succes_number_column.metric("Success", len(success_dataframe))
        error_number_column.metric("Error", len(errors_dataframe))
        unprocessed_number_column.metric("Unprocessed", len(unprocessed_dataframe))
        execution_mean_column.metric("Execution time mean(ms)", execution_time_mean)

from typing import Optional

from numpy import insert
from pandas import DataFrame
from streamlit import sidebar


class TrackingsPostfetchFilters:
    def __init__(self, trackings_dataframe: DataFrame):
        self.__trackings_dataframe = trackings_dataframe
        self.__name_filter: Optional[str] = None
        self.__executor_name_filter: Optional[str] = None

    def build(self):
        self.__build_name_filter(self.__trackings_dataframe)
        self.__build_executor_name_filter(self.__trackings_dataframe)

    def __build_name_filter(self, trackings_dataframe: DataFrame) -> None:
        name_filter_options = trackings_dataframe["name"].unique()
        name_filter_options = insert(name_filter_options, 0, "")
        self.__name_filter = sidebar.selectbox(
            "Name filter:",
            name_filter_options,
        )

    def __build_executor_name_filter(self, trackings_dataframe: DataFrame) -> None:
        executor_name_filter_options = trackings_dataframe["executor_name"].unique()
        executor_name_filter_options = insert(executor_name_filter_options, 0, "")
        self.__executor_name_filter = sidebar.selectbox(
            "Executor name filter:",
            executor_name_filter_options,
        )

    def apply_filters(self, dataframe: DataFrame) -> DataFrame:
        if self.__name_filter:
            dataframe = dataframe[dataframe["name"] == self.__name_filter]

        if self.__executor_name_filter:
            dataframe = dataframe[dataframe["executor_name"] == self.__executor_name_filter]

        return dataframe

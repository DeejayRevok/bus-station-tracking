from pandas import DataFrame, Grouper
from streamlit import bar_chart


class TrackingsTotalChart:
    def __init__(self, trackings_dataframe: DataFrame):
        self.__trackings_dataframe = trackings_dataframe

    def build(self) -> None:
        if len(self.__trackings_dataframe) == 0:
            return

        bar_chart(self.__get_dataframe_to_plot(self.__trackings_dataframe), x="execution_start", y="total_passengers")

    def __get_dataframe_to_plot(self, dataframe: DataFrame) -> DataFrame:
        return (
            dataframe.groupby(Grouper(key="execution_start", freq="min"))["name"]
            .count()
            .reset_index(name="total_passengers")
        )

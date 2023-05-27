from pandas import DataFrame, Grouper
from streamlit.delta_generator import DeltaGenerator


class TrackingsErrorChart:
    def __init__(self, trackings_dataframe: DataFrame):
        self.__trackings_dataframe = trackings_dataframe

    def build(self, container: DeltaGenerator) -> None:
        if len(self.__trackings_dataframe) == 0:
            return

        container.bar_chart(
            self.__get_errors_dataframe(self.__trackings_dataframe), x="execution_start", y="total_errors"
        )

    def __get_errors_dataframe(self, dataframe: DataFrame) -> DataFrame:
        dataframe = dataframe[~dataframe["success"]]
        return (
            dataframe.groupby(Grouper(key="execution_start", freq="min"))["name"]
            .count()
            .reset_index(name="total_errors")
        )

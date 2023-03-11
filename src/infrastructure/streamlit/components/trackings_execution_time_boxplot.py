from altair import Chart
from pandas import DataFrame
from streamlit.delta_generator import DeltaGenerator


class TrackingsExecutionTimeBoxPlot:
    def __init__(self, trackings_dataframe: DataFrame):
        self.__trackings_dataframe = trackings_dataframe

    def build(self, container: DeltaGenerator) -> None:
        chart = (
            Chart(self.__trackings_dataframe, height=350)
            .mark_boxplot(extent="min-max")
            .encode(
                x="execution_time(ms)",
            )
        )

        container.altair_chart(chart, use_container_width=True)

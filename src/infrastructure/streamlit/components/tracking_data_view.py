from streamlit import json

from infrastructure.streamlit.components.trackings_table import TrackingsTable


class TrackingDataView:
    def __init__(self, trackings_table: TrackingsTable):
        self.__trackings_table = trackings_table

    def build(self) -> None:
        tracking_selected = self.__trackings_table.selected_row()
        tracking_selected_data = {}
        if tracking_selected is not None:
            tracking_selected_data = tracking_selected["data"]
        json(tracking_selected_data)

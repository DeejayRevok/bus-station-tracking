from __future__ import annotations

import warnings
from typing import Final, Optional

from pandas import DataFrame
from st_aggrid import AgGrid, ColumnsAutoSizeMode, GridOptionsBuilder, JsCode

warnings.simplefilter(action="ignore", category=FutureWarning)


class TrackingsTable:
    __DEFAULT_GRID_HEIGHT: Final = 300

    def __init__(self, trackings_dataframe: DataFrame):
        self.__trackings_dataframe = trackings_dataframe.copy()
        self.__table_grid: Optional[AgGrid] = None

    def selected_row(self) -> Optional[dict]:
        selected_rows = self.__table_grid["selected_rows"]
        if len(selected_rows) == 0:
            return None
        return selected_rows[0]

    def build(self) -> None:
        grid_options_builder = GridOptionsBuilder.from_dataframe(self.__trackings_dataframe)
        self.__configure_grid_options(grid_options_builder)

        self.__table_grid = AgGrid(
            self.__trackings_dataframe,
            height=self.__DEFAULT_GRID_HEIGHT,
            columns_auto_size_mode=ColumnsAutoSizeMode.FIT_ALL_COLUMNS_TO_VIEW,
            gridOptions=grid_options_builder.build(),
            allow_unsafe_jscode=True,
        )

    def __configure_grid_options(self, grid_options_builder: GridOptionsBuilder) -> GridOptionsBuilder:
        success_style = JsCode(
            """
            function(params) {
                if (params.value == true) {
                    return {
                        'color': 'white',
                        'backgroundColor': 'darkgreen'
                    }
                } else if(params.value == false){
                    return {
                        'color': 'white',
                        'backgroundColor': 'darkred'
                    }
                } else {
                    return {
                        'color': 'black',
                        'backgroundColor': 'yellow'
                    }
                }
            };
            """
        )
        grid_options_builder.configure_column("success", cellStyle=success_style)
        grid_options_builder.configure_column("data", hide=True)
        grid_options_builder.configure_selection("single", use_checkbox=False)
        return grid_options_builder

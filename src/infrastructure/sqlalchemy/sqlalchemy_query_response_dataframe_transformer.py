from bus_station.query_terminal.query_response import QueryResponse
from pandas import DataFrame, read_sql
from sqlalchemy.orm import Query


class SQLAlchemyQueryResponseDataframeTransformer:
    def transform(self, query_response: QueryResponse) -> DataFrame:
        if isinstance(query_response.data, Query) is False:
            raise ValueError(f"Expected Query, got {type(query_response.data)}")
        return read_sql(query_response.data.statement, query_response.data.session.bind)

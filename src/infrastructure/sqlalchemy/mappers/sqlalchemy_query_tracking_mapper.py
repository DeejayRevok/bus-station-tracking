from typing import Type

from sqlalchemy import JSON, Boolean, Column, DateTime, String, Table

from domain.query.query_tracking import QueryTracking
from infrastructure.sqlalchemy.mappers.sqlalchemy_mapper import SQLAlchemyMapper


class SQLAlchemyQueryTrackingMapper(SQLAlchemyMapper):
    @property
    def table(self) -> Table:
        return Table(
            "query_tracking",
            self._db_metadata,
            Column("id", String(255), primary_key=True),
            Column("name", String(255), nullable=False),
            Column("executor_name", String(255), nullable=False),
            Column("data", JSON, nullable=False),
            Column("response_data", JSON, nullable=True),
            Column("execution_start", DateTime, nullable=False),
            Column("execution_end", DateTime, nullable=True),
            Column("success", Boolean, nullable=True),
        )

    @property
    def model(self) -> Type:
        return QueryTracking

from typing import Type

from sqlalchemy import JSON, Boolean, Column, DateTime, String, Table

from domain.command.command_tracking import CommandTracking
from infrastructure.sqlalchemy.mappers.sqlalchemy_mapper import SQLAlchemyMapper


class SQLAlchemyCommandTrackingMapper(SQLAlchemyMapper):
    @property
    def table(self) -> Table:
        return Table(
            "command_tracking",
            self._db_metadata,
            Column("id", String(255), primary_key=True),
            Column("root_passenger_id", String(255), nullable=True),
            Column("name", String(255), nullable=False),
            Column("executor_name", String(255), nullable=False),
            Column("data", JSON, nullable=False),
            Column("execution_start", DateTime, nullable=False),
            Column("execution_end", DateTime, nullable=True),
            Column("success", Boolean, nullable=True),
        )

    @property
    def model(self) -> Type:
        return CommandTracking

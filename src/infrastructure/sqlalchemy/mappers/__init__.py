from pypendency.argument import Argument
from pypendency.builder import container_builder
from pypendency.definition import Definition


def load() -> None:
    container_builder.set_definition(
        Definition(
            "infrastructure.sqlalchemy.mappers.sqlalchemy_command_tracking_mapper.SQLAlchemyCommandTrackingMapper",
            "infrastructure.sqlalchemy.mappers.sqlalchemy_command_tracking_mapper.SQLAlchemyCommandTrackingMapper",
            [Argument.no_kw_argument("@sqlalchemy.MetaData")],
        )
    )
    container_builder.set_definition(
        Definition(
            "infrastructure.sqlalchemy.mappers.sqlalchemy_event_tracking_mapper.SQLAlchemyEventTrackingMapper",
            "infrastructure.sqlalchemy.mappers.sqlalchemy_event_tracking_mapper.SQLAlchemyEventTrackingMapper",
            [Argument.no_kw_argument("@sqlalchemy.MetaData")],
        )
    )
    container_builder.set_definition(
        Definition(
            "infrastructure.sqlalchemy.mappers.sqlalchemy_query_tracking_mapper.SQLAlchemyQueryTrackingMapper",
            "infrastructure.sqlalchemy.mappers.sqlalchemy_query_tracking_mapper.SQLAlchemyQueryTrackingMapper",
            [Argument.no_kw_argument("@sqlalchemy.MetaData")],
        )
    )

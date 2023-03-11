import os

from pypendency.builder import container_builder
from sqlalchemy import MetaData, create_engine
from sqlalchemy.engine import Engine
from sqlalchemy.orm import Session, scoped_session, sessionmaker


def load() -> None:
    container_builder.set("sqlalchemy.MetaData", MetaData())
    database_engine = __create_database_engine()
    container_builder.set("sqlalchemy.engine.Engine", database_engine)
    container_builder.set("sqlalchemy.orm.session.Session", __create_database_session(database_engine))

    container_builder.get(
        "infrastructure.sqlalchemy.mappers.sqlalchemy_command_tracking_mapper.SQLAlchemyCommandTrackingMapper"
    ).map()
    container_builder.get(
        "infrastructure.sqlalchemy.mappers.sqlalchemy_event_tracking_mapper.SQLAlchemyEventTrackingMapper"
    ).map()
    container_builder.get(
        "infrastructure.sqlalchemy.mappers.sqlalchemy_query_tracking_mapper.SQLAlchemyQueryTrackingMapper"
    ).map()


def __create_database_session(database_engine: Engine) -> Session:
    return scoped_session(session_factory=sessionmaker(bind=database_engine))()


def __create_database_engine() -> Engine:
    db_host = os.environ.get("BUS_STATION_TRACKING_DATABASE_HOST")
    db_port = os.environ.get("BUS_STATION_TRACKING_DATABASE_PORT")
    db_user = os.environ.get("BUS_STATION_TRACKING_DATABASE_USER")
    db_password = os.environ.get("BUS_STATION_TRACKING_DATABASE_PASSWORD")
    db_name = os.environ.get("BUS_STATION_TRACKING_DATABASE_NAME")
    engine_uri = f"postgresql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}"
    return create_engine(engine_uri)

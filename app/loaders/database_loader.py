import os

from sqlalchemy import MetaData, create_engine
from sqlalchemy.engine import Engine
from sqlalchemy.orm import Session, scoped_session, sessionmaker
from yandil.container import default_container

from infrastructure.sqlalchemy.mappers.sqlalchemy_command_tracking_mapper import SQLAlchemyCommandTrackingMapper
from infrastructure.sqlalchemy.mappers.sqlalchemy_event_tracking_mapper import SQLAlchemyEventTrackingMapper
from infrastructure.sqlalchemy.mappers.sqlalchemy_query_tracking_mapper import SQLAlchemyQueryTrackingMapper


def load() -> None:
    default_container.add(MetaData)
    database_engine = __create_database_engine()
    default_container[Engine] = database_engine
    default_container[Session] = __create_database_session(database_engine)

    default_container[SQLAlchemyCommandTrackingMapper].map()
    default_container[SQLAlchemyEventTrackingMapper].map()
    default_container[SQLAlchemyQueryTrackingMapper].map()


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

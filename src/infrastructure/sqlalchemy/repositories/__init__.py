from pypendency.argument import Argument
from pypendency.builder import container_builder
from pypendency.definition import Definition


def load() -> None:
    container_builder.set_definition(
        Definition(
            "infrastructure.sqlalchemy.repositories"
            ".sqlalchemy_command_tracking_repository.SQLAlchemyCommandTrackingRepository",
            "infrastructure.sqlalchemy.repositories"
            ".sqlalchemy_command_tracking_repository.SQLAlchemyCommandTrackingRepository",
            [Argument.no_kw_argument("@sqlalchemy.orm.session.Session")],
        )
    )
    container_builder.set_definition(
        Definition(
            "infrastructure.sqlalchemy.repositories"
            ".sqlalchemy_event_tracking_repository.SQLAlchemyEventTrackingRepository",
            "infrastructure.sqlalchemy.repositories"
            ".sqlalchemy_event_tracking_repository.SQLAlchemyEventTrackingRepository",
            [Argument.no_kw_argument("@sqlalchemy.orm.session.Session")],
        )
    )
    container_builder.set_definition(
        Definition(
            "infrastructure.sqlalchemy.repositories"
            ".sqlalchemy_query_tracking_repository.SQLAlchemyQueryTrackingRepository",
            "infrastructure.sqlalchemy.repositories"
            ".sqlalchemy_query_tracking_repository.SQLAlchemyQueryTrackingRepository",
            [Argument.no_kw_argument("@sqlalchemy.orm.session.Session")],
        )
    )

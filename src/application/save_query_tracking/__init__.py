from pypendency.argument import Argument
from pypendency.builder import container_builder
from pypendency.definition import Definition


def load() -> None:
    container_builder.set_definition(
        Definition(
            "application.save_query_tracking.save_query_tracking_command_handler.SaveQueryTrackingCommandHandler",
            "application.save_query_tracking.save_query_tracking_command_handler.SaveQueryTrackingCommandHandler",
            [
                Argument.no_kw_argument(
                    "@infrastructure.sqlalchemy.repositories"
                    ".sqlalchemy_query_tracking_repository.SQLAlchemyQueryTrackingRepository"
                )
            ],
        )
    )

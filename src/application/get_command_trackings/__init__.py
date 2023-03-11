from pypendency.argument import Argument
from pypendency.builder import container_builder
from pypendency.definition import Definition


def load() -> None:
    container_builder.set_definition(
        Definition(
            "application.get_command_trackings.get_command_trackings_query_handler.GetCommandTrackingsQueryHandler",
            "application.get_command_trackings.get_command_trackings_query_handler.GetCommandTrackingsQueryHandler",
            [
                Argument.no_kw_argument(
                    "@infrastructure.sqlalchemy.repositories"
                    ".sqlalchemy_command_tracking_repository.SQLAlchemyCommandTrackingRepository"
                )
            ],
        )
    )

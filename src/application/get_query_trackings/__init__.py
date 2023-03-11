from pypendency.argument import Argument
from pypendency.builder import container_builder
from pypendency.definition import Definition


def load() -> None:
    container_builder.set_definition(
        Definition(
            "application.get_query_trackings.get_query_trackings_query_handler.GetQueryTrackingsQueryHandler",
            "application.get_query_trackings.get_query_trackings_query_handler.GetQueryTrackingsQueryHandler",
            [
                Argument.no_kw_argument(
                    "@infrastructure.sqlalchemy.repositories"
                    ".sqlalchemy_query_tracking_repository.SQLAlchemyQueryTrackingRepository"
                )
            ],
        )
    )

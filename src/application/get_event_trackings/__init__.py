from pypendency.argument import Argument
from pypendency.builder import container_builder
from pypendency.definition import Definition


def load() -> None:
    container_builder.set_definition(
        Definition(
            "application.get_event_trackings.get_event_trackings_query_handler.GetEventTrackingsQueryHandler",
            "application.get_event_trackings.get_event_trackings_query_handler.GetEventTrackingsQueryHandler",
            [
                Argument.no_kw_argument(
                    "@infrastructure.sqlalchemy.repositories"
                    ".sqlalchemy_event_tracking_repository.SQLAlchemyEventTrackingRepository"
                )
            ],
        )
    )

from pypendency.builder import container_builder
from pypendency.definition import Definition

from infrastructure.sqlalchemy.mappers import load as load_mappers
from infrastructure.sqlalchemy.repositories import load as load_repositories


def load() -> None:
    load_mappers()
    load_repositories()
    container_builder.set_definition(
        Definition(
            "infrastructure.sqlalchemy"
            ".sqlalchemy_query_response_dataframe_transformer.SQLAlchemyQueryResponseDataframeTransformer",
            "infrastructure.sqlalchemy"
            ".sqlalchemy_query_response_dataframe_transformer.SQLAlchemyQueryResponseDataframeTransformer",
        )
    )

# pylint: disable= W0611, R0914
from src.infra.database.setting.connection import DBConnectionHandler
from src.data.interfaces.repositories_base import BaseRepositoryInterface
from src.presentation.mappers.mappers_base import BaseMapper

from typing import TypeVar, Dict, Any, List
from sqlalchemy.orm import Session  # noqa


# tipos genericos
M = TypeVar("M")  # models (dominio)
E = TypeVar("E")  # entity (ORM)


class BaseRepository(BaseRepositoryInterface):
    filters = ["nome", "id"]
    atributes = ["nome", "id"]

    def __init__(self):
        self.session = DBConnectionHandler()

    def create(self, model: M, mapper: BaseMapper) -> None:
        with self.session as session:
            try:
                entity = mapper.to_entity(model)
                session.add(entity)
                session.commit()

            except Exception as exception:
                session.rollback()
                raise exception

            finally:
                session.close()

    def get(
        self, entity_class: E, get_filters: Dict[str, Any], mapper: BaseMapper
    ) -> List[M]:

        with self.session as session:
            try:
                query = session.query(entity_class)

                for field, value in get_filters.items():
                    if field in self.filters and hasattr(entity_class, field):
                        colun_attr = getattr(entity_class, field)
                        query = query.filter(colun_attr == value)

                result = query.all()
                lista = []
                for entity_item in result:
                    item = mapper.to_domain(entity_item)
                    lista.append(item)

                return lista

            except Exception as exception:
                session.rollback()
                raise exception

            finally:
                session.close()

    def update(
        self,
        entity_class: E,
        mapper: BaseMapper,
        update_atributes: Dict[str, Any],  # valores para alterar
        update_filters: Dict[str, Any],
    ) -> List[M]:  # valores para busca
        cont = 0

        with self.session as session:
            try:
                query = session.query(entity_class)

                for field, value in update_filters.items():
                    if field in self.filters and hasattr(entity_class, field):
                        column_attr = getattr(entity_class, field)
                        query = query.filter(column_attr == value)
                        cont += 1

                if cont == 0:
                    raise ValueError("Filtros obrigatórios para atualização.")

                respose_query = query.all()
                result = []

                for item_query in respose_query:
                    for attr, value in update_atributes.items():
                        if attr in self.atributes and hasattr(item_query, attr):
                            setattr(item_query, attr, value)
                        else:
                            raise ValueError(
                                "não é permitido fazer alteração nesses campos."
                            )

                    result.append(mapper.to_domain(item_query))

                session.commit()
                return result

            except Exception as exception:
                session.rollback()
                raise exception

            finally:
                session.close()

    def delete(
        self, entity_class: E, mapper: BaseMapper, delete_filters: Dict[str, Any]
    ) -> List[M]:

        cont = 0
        with self.session as session:
            try:
                query = session.query(entity_class)

                for field, value in delete_filters.items():
                    if field in self.filters and hasattr(entity_class, field):
                        cont += 1
                        column_attr = getattr(entity_class, field)
                        query = query.filter(column_attr == value)

                if cont == 0:
                    raise ValueError("Filtros obrigatórios para atualização.")

                response_query = query.all()
                count = len(response_query)
                result = []

                for item_query in response_query:
                    result.append(mapper.to_domain(item_query))
                    session.delete(item_query)

                session.commit()
                return count, result

            except Exception as exception:
                session.rollback()
                raise exception

            finally:
                session.close()

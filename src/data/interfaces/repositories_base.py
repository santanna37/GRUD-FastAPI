from abc import ABC, abstractmethod

from typing import TypeVar, List


# tipos genericos
M = TypeVar("M")  # models (dominio)
E = TypeVar("E")  # entity (ORM)


class BaseRepositoryInterface(ABC):

    @abstractmethod
    def create(self, model, mapper) -> None:
        pass

    @abstractmethod
    def get(self, entity_class, get_filters, mapper) -> List[M]:
        pass

    @abstractmethod
    def update(self, entity_class, mapper, update_atributes, update_filters) -> List[M]:
        pass

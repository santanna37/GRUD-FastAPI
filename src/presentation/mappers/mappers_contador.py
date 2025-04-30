from src.domain.models.models_contador import ContadorModel
from src.infra.database.entities.entities_contador import ContadorEntitie
from .mappers_base import BaseMapper


class ContadorMapper(BaseMapper):
    @staticmethod
    def to_entity(contador: ContadorModel) -> ContadorEntitie:
        entity = BaseMapper.to_domain_from_entity(
            domain_obj=contador, entity_class=ContadorEntitie
        )
        return entity

    @staticmethod
    def to_domain(contador: ContadorEntitie) -> ContadorModel:
        domain = BaseMapper.to_entity_from_domain(
            entity_obj=contador, domain_class=ContadorModel
        )
        return domain

from src.domain.models.models_contador import ContadorModel
from src.infra.database.entities.entities_contador import ContadorEntity
from .mappers_base import BaseMapper


class ContadorMapper(BaseMapper):
    @staticmethod
    def to_entity(contador: ContadorModel) -> ContadorEntity:
        entity = BaseMapper.model_to_entity(
            domain_obj=contador, entity_class=ContadorEntity
        )
        return entity

    @staticmethod
    def to_domain(contador: ContadorEntity) -> ContadorModel:
        domain = BaseMapper.entity_to_model(
            entity_obj=contador, domain_class=ContadorModel
        )
        return domain

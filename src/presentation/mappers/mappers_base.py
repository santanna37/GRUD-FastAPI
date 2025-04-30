from dataclasses import asdict


class BaseMapper:
    """Essa classe tem dois metodos para o mapeamento entre
    um objeto do dominio e uma entidade de banco"""

    @staticmethod
    def to_domain_from_entity(domain_obj, entity_class):
        data = asdict(domain_obj)
        return entity_class(**data)

    @staticmethod
    def to_entity_from_domain(entity_obj, domain_class):
        data = {
            key: getattr(entity_obj, key) for key in domain_class.__annotations__.keys()
        }
        return domain_class(**data)

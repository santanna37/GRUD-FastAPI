from dataclasses import asdict


class BaseMapper:
    """Essa classe tem dois metodos para o mapeamento entre
    um objeto do dominio e uma entidade de banco"""

    @staticmethod
    def model_to_entity(domain_obj, entity_class):
        data = asdict(domain_obj)
        filters_keys = {}
        accepted_keys = entity_class.__table__.columns.keys()

        for field, value in data.items():
            if field in accepted_keys:
                filters_keys[field] = value

        return entity_class(**filters_keys)

    @staticmethod
    def entity_to_model(entity_obj, domain_class):
        data = {}
        domain_fields = domain_class.__annotations__.keys()

        for field in domain_fields:
            if hasattr(entity_obj, field):
                data[field] = getattr(entity_obj, field)

        return domain_class(**data)

        # data = {
        #     key: getattr(entity_obj, key) for key in domain_class.__annotations__.keys()
        # }
        # return domain_class(**data)

from src.domain.models.models_contador import ContadorModel
from src.presentation.mappers.mappers_contador import ContadorMapper
from src.infra.database.entities.entities_contador import ContadorEntity


def test_to_entity():
    model = ContadorModel(id=1, nome="Luiz", email="oi@asd.com")
    entity = ContadorMapper.to_entity(model)
    return print(entity.__dict__)


def test_to_domain():
    entity = ContadorEntity(id=1, nome="luiz2", email="teste")
    model = ContadorMapper.to_domain(entity)
    return print(model)

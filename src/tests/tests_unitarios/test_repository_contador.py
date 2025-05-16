from src.domain.models.models_contador import ContadorModel
from src.presentation.mappers.mappers_contador import ContadorMapper
from src.infra.database.repositories.repositories_contador import ContadorRepository


modelo_contador = ContadorModel(
    nome="teste_repository_contador", email="test_contador_email@gmail.com"
)
mapper = ContadorMapper()


def test_create_contador():
    contador = modelo_contador
    repo = ContadorRepository()
    repo.create(model=contador, mapper=mapper)

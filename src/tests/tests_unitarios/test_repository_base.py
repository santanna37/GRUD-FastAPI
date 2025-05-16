from src.domain.models.models_contador import ContadorModel
from src.infra.database.entities.entities_contador import ContadorEntity
from src.presentation.mappers.mappers_contador import ContadorMapper
from src.infra.database.repositories.repositories_base import BaseRepository

# modelo_contador = ContadorModel(nome= 'teste_repository',
#                                 email='test_email@gmail.com')

# filtro_geral = {'nome':'teste_repository',
#                 'email':'test_email@gmail.com'}

# atribute_geral = {'nome':'teste_repository_contador'}

# update_atrbutes = {'email':'joão@empresa.com'}
# mapper = ContadorMapper()

# def test_create():
#     contador = modelo_contador
#     repo = BaseRepository()
#     repo.create(model= contador, mapper= mapper)

#     print(contador)


# def test_get():
#     filtro = filtro_geral
#     repo = BaseRepository()
#     resposta = repo.get(entity_class=ContadorEntity,
#                         get_filters=filtro,
#                         mapper=mapper)

#     print(resposta)


# def test_update():
#     repo = BaseRepository()
#     resposta = repo.update(entity_class=ContadorEntity,
#                             update_filters=filtro_geral,
#                             update_atributes= update_atrbutes,
#                             mapper=ContadorMapper
#                             )

#     print(resposta)


# def test_delete():
#     del_filtro = {'email': 'joao@empresa.com'}
#     repo = BaseRepository()
#     resposta = repo.delete(entity_class= ContadorEntity,
#                             mapper= ContadorMapper,
#                             delete_filters= del_filtro)

#     print(resposta)


# from src.domain.models.models_contador import ContadorModel
# from src.infra.database.entities.entities_contador import ContadorEntity
# from src.presentation.mappers.mappers_contador import ContadorMapper
# from src.infra.database.repositories.repositories_contador import ContadorRepository


# Instâncias fixas
repo = BaseRepository()
mapper = ContadorMapper()

# Dados para testes
modelo_contador = ContadorModel(nome="teste_repository", email="test_email@gmail.com")
filtro_geral = {"nome": "test", "email": "test_email@gmail.com"}
update_atributes = {"nome": "joao@empresa.com"}
delete_filtro = {"id": 67}


# ---------------------- TEST CREATE ----------------------
def test_create_contador():
    repo.create(model=modelo_contador, mapper=mapper)
    print("\n[CREATE] Inserido:", modelo_contador)


# ---------------------- TEST GET ----------------------
def test_get_contador():
    resultado = repo.get(
        entity_class=ContadorEntity, get_filters=filtro_geral, mapper=mapper
    )
    print("\n[GET] Resultado:", resultado)


# ---------------------- TEST UPDATE ----------------------
def test_update_contador():
    resultado = repo.update(
        entity_class=ContadorEntity,
        update_filters=filtro_geral,
        update_atributes=update_atributes,
        mapper=mapper,
    )
    print("\n[UPDATE] Atualizado:", resultado)


# ---------------------- TEST DELETE ----------------------
def test_delete_contador():
    count, deletados = repo.delete(
        entity_class=ContadorEntity, mapper=mapper, delete_filters=delete_filtro
    )
    print(f"\n[DELETE] Contadores deletados ({count}):", deletados)

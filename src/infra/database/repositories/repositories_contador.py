# pylint: disable=W0246
from src.infra.database.repositories.repositories_base import BaseRepository

# from src.presentation.mappers.mappers_contador import ContadorMapper
# from src.domain.models.models_contador import ContadorModel

from typing import List


class ContadorRepository(BaseRepository):
    fiters: List[str] = ["nome", "email"]
    atributes: List[str] = ["nome", "email"]

    def __init__(self):
        super().__init__()

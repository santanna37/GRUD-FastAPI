from sqlalchemy import Column, Integer, String
from src.infra.database import Base


class ContadorEntitie(Base):
    __tablename__ = "contador"

    id = Column(Integer, autoincrement=True, autoincrement=True)
    nome = Column(String)

    def __repr__(self):
        return f"Users [id = {self.id}], nome = {self.id}"

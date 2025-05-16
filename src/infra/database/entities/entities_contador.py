# pylint: disable=R0903
from sqlalchemy import Column, Integer, String
from src.infra.database.setting.base import Base


class ContadorEntity(Base):
    __tablename__ = "contador"

    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(100), nullable=False)
    email = Column(String(100))

    # def __repr__(self):
    #    return f"Contador [id={self.id}, nome={self.nome}]"

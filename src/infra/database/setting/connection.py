from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


class DBConnectionHandler:
    """CONEXÃO COM O BANCO DE DADOS"""

    def __init__(self) -> None:
        self.__connection_string = "mysql+pymysql://root:senha@localhost:3305/public"

        self.__engine = self.__create_session_engine()
        self.session = None

    def __create_session_engine(self):
        engine = create_engine(self.__connection_string)
        return engine

    def get_engine(self):
        return self.__engine

    def __enter__(self):
        session_make = sessionmaker(bind=self.__engine)
        self.session = session_make()
        return self.session

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.session.close()

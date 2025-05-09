# pylint: disable=W0718

from sqlalchemy import text

from src.infra.database.setting.connection import DBConnectionHandler


def test_create_engine_database():
    db_connection = DBConnectionHandler()
    engine = db_connection.get_engine()
    print(engine)


def test_work_engine_database():
    db_connection = DBConnectionHandler()
    engine = db_connection.get_engine()

    try:
        with engine.connect() as connection:
            result = connection.execute(text("SELECT 1"))
            assert result.scalar() == 1
            print("✅ Conexão com o banco realizada com sucesso.")
    except Exception as e:
        print("❌ Erro na conexão com o banco:", e)
        assert False

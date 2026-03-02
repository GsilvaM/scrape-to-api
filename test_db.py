from sqlalchemy import inspect, text

from src.scrape_to_api.db.session import engine


def main():
    try:
        with engine.connect() as connection:
            result = connection.execute(text("SELECT 1"))
            print("Conexão OK! Resultado:", result.scalar())
    except Exception as e:
        print("Erro na conexão:", e)


inspector = inspect(engine)
print("Tabelas existentes:", inspector.get_table_names())


if __name__ == "__main__":
    main()

from src.scrape_to_api.db.base import Base
from src.scrape_to_api.db.session import engine


def main():
    print('Criando tabelas no banco...')
    Base.metadata.create_all(bind=engine)
    print('Tabelas criadas com sucesso.')


if __name__ == '__main__':
    main()

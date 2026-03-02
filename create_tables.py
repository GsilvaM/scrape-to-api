from src.scrape_to_api.db.base import Base
from src.scrape_to_api.db.session import engine
from src.scrape_to_api.models.book import Book         
from src.scrape_to_api.models.category import Category  


def main():
    print('Criando tabelas no banco...')
    Base.metadata.create_all(bind=engine)
    print('Tabelas criadas com sucesso.')


if __name__ == '__main__':
    main()
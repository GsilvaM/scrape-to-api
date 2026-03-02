from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, MappedColumn, relationship

from src.scrape_to_api.db.base import Base
from src.scrape_to_api.models.book import Book


class Category(Base):
    __tablename__ = 'categories'

    id: Mapped[int] = MappedColumn(
        Integer, primary_key=True, autoincrement=True
    )

    name: Mapped[str] = MappedColumn(String(100), unique=True, nullable=False)

    books: Mapped[list['Book']] = relationship(
        'Book', back_populates='category'
    )

from sqlalchemy.orm import Session

from src.scrape_to_api.models.book import Book
from src.scrape_to_api.models.category import Category


class BookCategory:
    def __init__(self, db: Session):
        self.db = db

    def get_category_by_name(self, name: str) -> Category | None:
        return self.db.query(Category).filter(Category.name == name).first()

    def create_category(self, name: str) -> Category:
        category = Category(name=name)
        self.db.add(category)
        self.db.flush()
        return category

    def get_or_create_category(self, name: str) -> Category:
        category = self.get_category_by_name(name)
        if not category:
            category = self.create_category(name)
        return category

    def exists_by_title(self, title: str) -> bool:
        return self.db.query(
            Book).filter(Book.title == title).first() is not None  # type: ignore

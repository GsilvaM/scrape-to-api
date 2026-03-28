from sqlalchemy.orm import Session

from app.models.book import Book
from app.models.category import Category


class RepoBookCategory:
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
        return (
            self.db.query(Book).filter(Book.title == title).first() is not None
        )

    def create(self, book_data: dict) -> Book:
        book = Book(**book_data)
        self.db.add(book)
        return book

    def get_all(self, skip: int = 0, limit: int = 100) -> list[Book]:
        return self.db.query(Book).offset(skip).limit(limit).all()

    def get_by_id(self, book_id: int) -> Book | None:
        return self.db.query(Book).filter(Book.id == book_id).first()

    def get_books_by_category(self, category_name: str) -> list[Book]:
        return (
            self.db
            .query(Book)
            .join(Category)
            .filter(Category.name == category_name)
            .all()
        )

    def get_all_categories(self) -> list[Category]:
        return self.db.query(Category).all()

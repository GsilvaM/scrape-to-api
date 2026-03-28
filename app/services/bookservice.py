from decimal import Decimal, InvalidOperation

from sqlalchemy.orm import Session

from app.repositories.book_repository import RepoBookCategory


class BookService:
    def __init__(self, db: Session):
        self.repo = RepoBookCategory(db)
        self.db = db

    @staticmethod
    def _parse_price(price_str: str) -> Decimal:
        clean_price = price_str.replace('£', '').replace('$', '').strip()
        try:
            return Decimal(clean_price)
        except InvalidOperation:
            return Decimal('0.00')

    def save_books(self, books_data: list[dict], category_name: str) -> dict:
        created = 0
        skipped = 0

        category = self.repo.get_or_create_category(category_name)
        for data in books_data:
            if self.repo.exists_by_title(data['title']):
                skipped += 1
                continue

            self.repo.create({
                'title': data['title'],
                'price': self._parse_price(data['price']),
                'rating': data['rating'],
                'available': data['availability'].lower() == 'in stock',
                'cover_url': data.get('image_url', 'sem-imagem.jpg'),
                'category_id': category.id,
            })
            created += 1
        self.db.commit()
        return {'created': created, 'skipped': skipped}

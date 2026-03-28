from unittest.mock import MagicMock, patch

import pytest
from fastapi.testclient import TestClient

from app.db.session import get_db
from app.main import app

client = TestClient(app)

HTTP_OK = 200
HTTP_NOT_FOUND = 404


@pytest.fixture
def mock_db():
    db = MagicMock()
    app.dependency_overrides[get_db] = lambda: db
    yield db
    app.dependency_overrides.clear()


def test_get_books_return_200(mock_db):
    book = MagicMock()
    book.id = 1
    book.title = 'Dune'
    book.price = 9.99
    book.rating = 3
    book.available = True
    book.cover_url = None
    book.source_url = None
    book.category_id = 1

    with patch('app.api.books_router.RepoBookCategory') as mock_repo:
        mock_repo.return_value.get_all.return_value = [book]
        response = client.get('/api/books')

    assert response.status_code == HTTP_OK
    assert response.json()[0]['title'] == 'Dune'


def test_get_book_by_id_return_404(mock_db):
    with patch('app.api.books_router.RepoBookCategory') as mock_repo:
        mock_repo.return_value.get_by_id.return_value = None
        response = client.get('/api/books/999')

    assert response.status_code == HTTP_NOT_FOUND

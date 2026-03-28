from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.repositories.book_repository import RepoBookCategory
from app.schemas.book import BookResponse
from app.scraper.books_scraper import scrape_books

router = APIRouter()


@router.get('/books', response_model=list[BookResponse])
def get_books(db: Session = Depends(get_db)):
    repo = RepoBookCategory(db)
    return repo.get_all()


@router.get('/books/{book_id}', response_model=BookResponse)
def get_book_by_id(book_id: int, db: Session = Depends(get_db)):
    repo = RepoBookCategory(db)
    book = repo.get_by_id(book_id)
    if not book:
        raise HTTPException(status_code=404, detail='Livro não encontrado')
    return book


@router.get('/categories')
def get_categories(db: Session = Depends(get_db)):
    repo = RepoBookCategory(db)
    return repo.get_all_categories()


@router.post('/scrape')
async def scraping():
    await scrape_books()
    return {'message': ' Scraping concluido com sucesso!'}

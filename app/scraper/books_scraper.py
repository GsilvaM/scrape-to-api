import asyncio

import httpx

from app.db.session import SessionLocal
from app.scraper.parser import parse_books_page
from app.services.bookservice import BookService

BASE_URL = 'https://books.toscrape.com/catalogue/page-{}.html'


async def scrape_books():
    total_created = 0
    total_skipped = 0

    async with httpx.AsyncClient(timeout=30.0) as client:
        for page in range(1, 51):
            print(f'Scraping página {page}/50...')

            response = await client.get(BASE_URL.format(page))
            response.raise_for_status()

            books = parse_books_page(response.text)

            db = SessionLocal()
            try:
                service = BookService(db)
                result = service.save_books(books, category_name='general')
                total_created += result['created']
                total_skipped += result['skipped']
            finally:
                db.close()

    print('\n✅ Scraping concluído!')
    print(f'   Criados : {total_created}')
    print(f'   Pulados : {total_skipped}')


if __name__ == '__main__':
    asyncio.run(scrape_books())

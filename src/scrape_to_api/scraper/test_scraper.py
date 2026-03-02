import asyncio

from scrape_to_api.scraper.books_scraper import scrape_books


async def main():
    books = await scrape_books()
    print(f"Total de livros coletados: {len(books)}")
    print(books[0])
    for book in books:
          print(book['title'])

if __name__ == "__main__":
        asyncio.run(main())

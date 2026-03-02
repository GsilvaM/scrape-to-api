import httpx

from scrape_to_api.scraper.parser import parse_books_page

BASE_URL = "https://books.toscrape.com/catalogue/page-{}.html"


async def scrape_books():
    all_books_list = []
    async with httpx.AsyncClient() as client:
        for page in range(1, 51):
            url = BASE_URL.format(page)
            response = await client.get(url)
            response.raise_for_status()
            books = parse_books_page(response.text)
            all_books_list.extend(books)

    return all_books_list

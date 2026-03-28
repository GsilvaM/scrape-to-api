from bs4 import BeautifulSoup

rating_map = {
    'One': 1,
    'Two': 2,
    'Three': 3,
    'Four': 4,
    'Five': 5,
}


class RatingParseError(Exception):
    pass


def parse_book_data(book_tag):
    title = book_tag.h3.a['title']
    price = book_tag.select_one('.price_color').text.strip()
    availability = book_tag.select_one('.availability').text.strip()
    rating_text = book_tag.p['class'][1]
    rating = rating_map.get(rating_text, None)
    image_url = book_tag.img['src']

    return {
        'title': title,
        'price': price,
        'availability': availability,
        'rating': rating,
        'image_url': image_url,
    }


def parse_books_page(html: str):
    soup = BeautifulSoup(html, 'lxml')
    books = soup.select('article.product_pod')
    return [parse_book_data(book) for book in books]

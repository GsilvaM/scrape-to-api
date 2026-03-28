from bs4 import BeautifulSoup

from app.scraper.parser import parse_book_data, parse_books_page

RATING_THREE = 3
RATING_FIVE = 5
TOTAL_BOOKS = 2


def make_book_html(
    title: str, price: str, rating: str, availability: str
) -> str:
    """Cria um HTML falso de livro para os testes."""
    return f"""
    <article class="product_pod">
        <div class="image_container">
            <a href="book.html">
                <img src="cover.jpg" alt="{title}" class="thumbnail"/>
            </a>
        </div>
        <p class="star-rating {rating}"></p>
        <h3><a href="book.html" title="{title}">{title}</a></h3>
        <div class="product_price">
            <p class="price_color">{price}</p>
            <p class="instock availability">{availability}</p>
        </div>
    </article>
    """


def test_parse_book_data_retorna_campos_corretos():
    html = make_book_html(
        title='Dune',
        price='£39.45',
        rating='Three',
        availability='In stock',
    )
    soup = BeautifulSoup(html, 'lxml')
    book_tag = soup.select_one('article.product_pod')

    result = parse_book_data(book_tag)

    assert result['title'] == 'Dune'
    assert result['price'] == '£39.45'
    assert result['rating'] == RATING_THREE
    assert result['availability'] == 'In stock'
    assert result['image_url'] == 'cover.jpg'


def test_parse_books_page_retorna_lista_de_livros():
    html = f"""
    <html><body>
        {make_book_html('Dune', '£39.45', 'Three', 'In stock')}
        {make_book_html('1984', '£25.00', 'Five', 'In stock')}
    </body></html>
    """

    result = parse_books_page(html)

    assert len(result) == TOTAL_BOOKS
    assert result[0]['title'] == 'Dune'
    assert result[1]['title'] == '1984'
    assert result[1]['rating'] == RATING_FIVE

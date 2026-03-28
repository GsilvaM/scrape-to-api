from decimal import Decimal

from pydantic import BaseModel


class BookResponse(BaseModel):
    id: int
    title: str
    price: Decimal
    rating: int
    available: bool
    cover_url: str | None
    source_url: str | None

    model_config = {'from_attributes': True}

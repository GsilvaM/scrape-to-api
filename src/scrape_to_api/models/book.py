from decimal import Decimal

from sqlalchemy import (
    DECIMAL,
    Boolean,
    DateTime,
    ForeignKey,
    Integer,
    String,
    Text,
)
from sqlalchemy.orm import Mapped, MappedColumn, relationship
from sqlalchemy.sql import func

from src.scrape_to_api.db.base import Base


class Book(Base):
    __tablename__ = 'books'

    id: Mapped[int] = MappedColumn(
        Integer, autoincrement=True, primary_key=True
    )

    title: Mapped[str] = MappedColumn(String(500), unique=True, nullable=True)

    price: Mapped[Decimal] = MappedColumn(DECIMAL(10, 2), nullable=False)

    rating: Mapped[int] = MappedColumn(Integer, nullable=False)

    available: Mapped[bool] = MappedColumn(Boolean, default=True)

    cover_url: Mapped[str | None] = MappedColumn(Text, nullable=True)

    source_url: Mapped[str | None] = MappedColumn(Text, nullable=True)

    category_id: Mapped[int | None] = MappedColumn(
        Integer, ForeignKey('categories.id'), nullable=True
    )

    category: Mapped['Category | None'] = relationship(
        'Category', back_populates='books'
    )

    created_at: Mapped[DateTime] = MappedColumn(
        DateTime(timezone=True), server_default=func.now()
    )

    updated_at: Mapped[DateTime] = MappedColumn(
        DateTime(timezone=True), server_default=func.now(), onupdate=func.now()
    )

from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker

from src.scrape_to_api.settings.db_config import settings

engine = create_engine(settings.database_url, pool_pre_ping=True, echo=False)

SessionLocal = sessionmaker(autoflush=False, autocommit=False, bind=engine)


def get_db():
    db: Session = SessionLocal()

    try:
        yield db
    finally:
        db.close()

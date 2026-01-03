from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase

# ---------- Base (DUY NHẤT) ----------
class Base(DeclarativeBase):
    pass


DATABASE_URL = "postgresql://postgres:Hxs03122003@localhost:5432/test_db"

engine = create_engine(
    DATABASE_URL,
    echo=True
)

SessionLocal = sessionmaker(
    bind=engine,
    autocommit=False,
    autoflush=False
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

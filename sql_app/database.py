from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import declarative_base, sessionmaker

SQLALCHEMY_DATABASE_URL = "sqlite+aiosqlite:///aiosqlite_demo.db"

engine = create_async_engine(SQLALCHEMY_DATABASE_URL, echo=False)
SessionLocal = sessionmaker(
    engine, expire_on_commit=False, class_=AsyncSession
)

Base = declarative_base()

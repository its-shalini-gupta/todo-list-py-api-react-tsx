
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# DATABASE_URL = "postgresql+psycopg2://postgres:12345@192.168.8.250:5432/chetak_dev"
DATABASE_URL = "postgresql+psycopg2://postgres:root@localhost/student_db"


# ✅ Define a single Declarative Base
class Base(DeclarativeBase):
    pass

# ✅ Create SQLAlchemy Engine
engine = create_engine(DATABASE_URL)

# ✅ Create Session
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# ✅ Dependency to get the database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

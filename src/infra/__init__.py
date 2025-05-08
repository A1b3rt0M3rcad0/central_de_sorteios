from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import dotenv
import os

dotenv.load_dotenv()

DATABASE_URL = os.getenv('BATABASE_URL')

engine = create_engine(
    url=DATABASE_URL,
    future=True
)

session = sessionmaker(
    bind=engine,
    autocommit=False,
    autoflush=False,
    future=True
)
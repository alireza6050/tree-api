import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# This ensures DB is always placed where you want it
BASE_DIR = "/Users/alirezatahsini/Downloads/Challenge/"
DB_PATH = os.path.abspath(os.path.join(BASE_DIR, "..", "tree.db"))
DATABASE_URL = f"sqlite:///{DB_PATH}"

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()
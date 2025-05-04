# Sets up the SQLite database connection and ORM base
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# Define the base directory for placing the SQLite database file
BASE_DIR = "."
# Construct the full path to the database file
DB_PATH = os.path.abspath(os.path.join(BASE_DIR, "tree.db"))
# Create the SQLite database URL
DATABASE_URL = f"sqlite:///{DB_PATH}"

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Ganti dengan username, password, host, dbname milikmu
# DATABASE_URL = "postgresql+psycopg2://postgres:agus@localhost:5432/data_mahasiswa"
DATABASE_URL = "postgresql+psycopg2://postgres@localhost:5432/data_mahasiswa"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
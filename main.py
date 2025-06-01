from fastapi import FastAPI
from database.config import engine
from models.models import Base
from routes import mahasiswa

app = FastAPI()

# Buat semua tabel
Base.metadata.create_all(bind=engine)

# Include router
app.include_router(mahasiswa.router)

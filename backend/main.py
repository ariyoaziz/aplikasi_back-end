from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from database.config import engine
from models.models import Base
from routes import mahasiswa

app = FastAPI()

# Buat semua tabel
Base.metadata.create_all(bind=engine)

# Setup CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include router
app.include_router(mahasiswa.router, prefix="/api")

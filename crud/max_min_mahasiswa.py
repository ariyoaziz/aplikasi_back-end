from sqlalchemy.orm import Session
from models.models import Mahasiswa
from sqlalchemy import func

def get_max_ipk(db: Session):
    return db.query(func.max(Mahasiswa.ipk)).scalar()

def get_min_ipk(db: Session):
    return db.query(func.min(Mahasiswa.ipk)).scalar()

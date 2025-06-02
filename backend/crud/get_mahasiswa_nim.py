from sqlalchemy.orm import Session
from models.models import Mahasiswa

def get_mahasiswa_by_nim(db: Session, nim: str):
    return db.query(Mahasiswa).filter(Mahasiswa.nim == nim).first()

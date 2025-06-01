from sqlalchemy.orm import Session
from models.models import Mahasiswa

def count_all_mahasiswa(db: Session):
    return db.query(Mahasiswa).count()

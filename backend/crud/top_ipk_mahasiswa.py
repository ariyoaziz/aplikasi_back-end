from sqlalchemy.orm import Session
from models.models import Mahasiswa

def top5_mahasiswa(db: Session):
    return db.query(Mahasiswa).order_by(Mahasiswa.ipk.desc()).limit(5).all()

from sqlalchemy.orm import Session
from models.models import Mahasiswa

def mahasiswa_tanpa_nama(db: Session):
    return db.query(Mahasiswa).filter(Mahasiswa.nama == None).all()

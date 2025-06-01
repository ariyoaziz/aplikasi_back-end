from sqlalchemy.orm import Session
from models.models import Mahasiswa
from sqlalchemy import func

def count_per_angkatan(db: Session):
    hasil = db.query(Mahasiswa.angkatan, func.count(Mahasiswa.nim).label('jumlah'))\
              .group_by(Mahasiswa.angkatan).all()
    # hasil adalah list tuple (angkatan, jumlah)
    return [{"angkatan": angkatan, "jumlah": jumlah} for angkatan, jumlah in hasil]

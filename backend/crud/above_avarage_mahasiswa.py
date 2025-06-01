from sqlalchemy.orm import Session
from models.models import Mahasiswa
from sqlalchemy import func

def get_mahasiswa_above_average(db: Session):
    avg_ipk = db.query(func.avg(Mahasiswa.ipk)).scalar()
    return db.query(Mahasiswa).filter(Mahasiswa.ipk > avg_ipk).all()

from sqlalchemy.orm import Session
from models.models import Mahasiswa
from sqlalchemy import func

def get_average_ipk(db: Session):
    return db.query(func.avg(Mahasiswa.ipk)).scalar()

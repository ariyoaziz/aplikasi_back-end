from sqlalchemy.orm import Session
from models.models import Mahasiswa
from sqlalchemy import func

def get_mahasiswa_statistics(db: Session):
    total = db.query(func.count(Mahasiswa.nim)).scalar()

    # Karena tidak ada flag 'deleted' atau 'active', kita anggap semua data aktif
    active = total
    deleted = 0

    return {
        "total": total,
        "active": active,
        "deleted": deleted
    }

from sqlalchemy.orm import Session
from models.models import Mahasiswa

def get_all_jurusan(db: Session):
    hasil = db.query(Mahasiswa.jurusan).distinct().all()
    # hasil adalah list of tuple, misal [('Informatika',), ('Sistem Informasi',)]
    return [{"jurusan": jurusan[0]} for jurusan in hasil]
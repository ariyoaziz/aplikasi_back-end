from sqlalchemy.orm import Session
from models.models import Mahasiswa
from schema.schema import MahasiswaUpdate

def update_mahasiswa(db: Session, nim: str, mahasiswa_data: MahasiswaUpdate):
    # Cari data mahasiswa berdasarkan nim
    mahasiswa = db.query(Mahasiswa).filter(Mahasiswa.nim == nim).first()
    if not mahasiswa:
        return None  # atau raise exception kalau mau

    # Update field sesuai input
    mahasiswa.nama = mahasiswa_data.nama
    mahasiswa.jurusan = mahasiswa_data.jurusan
    mahasiswa.angkatan = mahasiswa_data.angkatan
    mahasiswa.ipk = mahasiswa_data.ipk

    # Commit perubahan
    db.commit()
    db.refresh(mahasiswa)
    return mahasiswa

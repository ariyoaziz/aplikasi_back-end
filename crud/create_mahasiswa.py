from fastapi import HTTPException, status
from models.models import Mahasiswa
from schema.schema import MahasiswaCreate
from sqlalchemy.orm import Session

def create_mahasiswa(db: Session, mahasiswa: MahasiswaCreate):
    # cek apakah nim sudah ada
    existing = db.query(Mahasiswa).filter(Mahasiswa.nim == mahasiswa.nim).first()
    if existing:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="NIM sudah terdaftar, gunakan NIM lain"
        )
    db_mahasiswa = Mahasiswa(
        nim=mahasiswa.nim,
        nama=mahasiswa.nama,
        jurusan=mahasiswa.jurusan,
        angkatan=mahasiswa.angkatan,
        ipk=mahasiswa.ipk
    )
    db.add(db_mahasiswa)
    db.commit()
    db.refresh(db_mahasiswa)
    return db_mahasiswa

from sqlalchemy.orm import Session
from models.models import Mahasiswa
from fastapi import HTTPException

def delete_mahasiswa(db: Session, nim: str):
    mahasiswa = db.query(Mahasiswa).filter(Mahasiswa.nim == nim).first()

    if not mahasiswa:
        raise HTTPException(status_code=404, detail="Mahasiswa dengan NIM tersebut tidak ditemukan")

    db.delete(mahasiswa)
    db.commit()

    return {"message": f"Mahasiswa dengan NIM {nim} berhasil dihapus"}

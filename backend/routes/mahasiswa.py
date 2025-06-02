from fastapi import APIRouter, Depends, Query, HTTPException
from sqlalchemy.orm import Session
from database.config import SessionLocal
from crud import *

from schema.schema import *
from typing import List

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/mahasiswa", response_model=List[MahasiswaSchema])
def read_mahasiswa(
    nim: str = Query(None),
    nama: str = Query(None),
    jurusan: str = Query(None),
    angkatan: int = Query(None),
    ipk_min: float = Query(None),
    ipk_max: float = Query(None),
    db: Session = Depends(get_db)
):
    return get_mahasiswa(
        db,
        nim=nim,
        nama=nama,
        jurusan=jurusan,
        angkatan=angkatan,
        ipk_min=ipk_min,
        ipk_max=ipk_max
    )

@router.post("/mahasiswa", response_model=MahasiswaSchema)
def add_mahasiswa(mahasiswa: MahasiswaCreate, db: Session = Depends(get_db)):
    return create_mahasiswa(db, mahasiswa)

@router.get("/mahasiswa/statistics")
def read_statistics(db: Session = Depends(get_db)):
    return get_mahasiswa_statistics(db)

@router.get("/mahasiswa/{nim}", response_model=MahasiswaSchema)
def route_get_mahasiswa_by_nim(nim: str, db: Session = Depends(get_db)):
    mahasiswa = get_mahasiswa_by_nim(db, nim)
    if not mahasiswa:
        raise HTTPException(status_code=404, detail="Mahasiswa tidak ditemukan")
    return mahasiswa

@router.put("/mahasiswa/{nim}", response_model=MahasiswaSchema)
def put_mahasiswa(nim: str, mahasiswa_data: MahasiswaUpdate, db: Session = Depends(get_db)):
    updated = update_mahasiswa(db, nim, mahasiswa_data)
    if not updated:
        raise HTTPException(status_code=404, detail="Mahasiswa tidak ditemukan")
    return updated

@router.delete("/mahasiswa/{nim}")
def remove_mahasiswa(nim: str, db: Session = Depends(get_db)):
    return delete_mahasiswa(db, nim)


@router.get("/mahasiswa/count")
def get_jumlah_mahasiswa(db: Session = Depends(get_db)):
    return {"total": count_all_mahasiswa(db)}

@router.get("/mahasiswa/jurusan", response_model=List[JurusanSchema])
def ambil_jurusan(db: Session = Depends(get_db)):
    return get_all_jurusan(db)

@router.get("/mahasiswa/ipk/average")
def average_ipk(db: Session = Depends(get_db)):
    return {"rata_rata_ipk": get_average_ipk(db)}

@router.get("/mahasiswa/ipk/max")
def max_ipk(db: Session = Depends(get_db)):
    return {"ipk_tertinggi": get_max_ipk(db)}

@router.get("/mahasiswa/ipk/min")
def min_ipk(db: Session = Depends(get_db)):
    return {"ipk_terendah": get_min_ipk(db)}

@router.get("/mahasiswa/group/angkatan")
def jumlah_per_angkatan(db: Session = Depends(get_db)):
    return count_per_angkatan(db)

@router.get("/mahasiswa/ipk/above-average")
def mahasiswa_diatas_rerata(db: Session = Depends(get_db)):
    return get_mahasiswa_above_average(db)

@router.get("/mahasiswa/top5")
def get_top5_mahasiswa(db: Session = Depends(get_db)):
    return top5_mahasiswa(db)

@router.get("/mahasiswa/namakosong")
def get_mahasiswa_namakosong(db: Session = Depends(get_db)):
    return mahasiswa_tanpa_nama(db)


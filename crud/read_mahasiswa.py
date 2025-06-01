from sqlalchemy.orm import Session
from models.models import Mahasiswa

def get_mahasiswa(
    db: Session,
    nim: str = None,
    nama: str = None,
    jurusan: str = None,
    angkatan: int = None,
    ipk_min: float = None,
    ipk_max: float = None
):
    query = db.query(Mahasiswa)

    if nim:
        query = query.filter(Mahasiswa.nim.ilike(f"%{nim}%"))
    if nama:
        query = query.filter(Mahasiswa.nama.ilike(f"%{nama}%"))
    if jurusan:
        query = query.filter(Mahasiswa.jurusan.ilike(f"%{jurusan}%"))
    if angkatan:
        query = query.filter(Mahasiswa.angkatan == angkatan)
    if ipk_min is not None:
        query = query.filter(Mahasiswa.ipk >= ipk_min)
    if ipk_max is not None:
        query = query.filter(Mahasiswa.ipk <= ipk_max)

    query = query.order_by(Mahasiswa.nim.asc())  # atau .order_by(asc(Mahasiswa.nim))

    return query.all()


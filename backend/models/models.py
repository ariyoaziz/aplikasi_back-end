from sqlalchemy import Column, Integer, String, Numeric
from database.config import Base

class Mahasiswa(Base):
    __tablename__ = "mahasiswa"

    nim = Column(String(20), primary_key=True, nullable=False)
    nama = Column(String(100))
    jurusan = Column(String(100))
    angkatan = Column(Integer)
    ipk = Column(Numeric)

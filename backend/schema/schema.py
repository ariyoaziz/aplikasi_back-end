from pydantic import BaseModel, Field, validator
from typing import Optional

class MahasiswaCreate(BaseModel):
    nim: str = Field(..., pattern=r'^\d+$', description="NIM harus angka saja tanpa huruf/simbol")
    nama: str
    jurusan: str
    angkatan: int = Field(..., ge=1000, le=9999, description="Angkatan harus 4 digit tahun")
    ipk: float = Field(..., ge=0.0, le=4.0, description="IPK maksimal 4.0")

    @validator('angkatan')
    def validate_angkatan_length(cls, v):
        if len(str(v)) != 4:
            raise ValueError('Angkatan harus 4 digit')
        return v
    
class MahasiswaUpdate(BaseModel):
    nama: Optional[str] = None
    jurusan: Optional[str] = None
    angkatan: Optional[int] = Field(None, ge=1000, le=9999, description="Tahun angkatan harus 4 digit")
    ipk: Optional[float] = Field(None, ge=0.0, le=4.0, description="IPK maksimal 4.0")

class JurusanSchema(BaseModel):
    jurusan: str

    class Config:
        from_attributes = True

class CountPerAngkatanSchema(BaseModel):
    angkatan: int
    jumlah: int  # jumlah mahasiswa per angkatan

    class Config:
        orm_mode = True


class MahasiswaSchema(BaseModel):
    nim: str
    nama: Optional[str]
    jurusan: Optional[str]
    angkatan: Optional[int]
    ipk: Optional[float]

    class Config:
        from_attributes = True

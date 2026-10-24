from typing import Optional

from pydantic import BaseModel, Field

EMAIL_PATTERN = r"^[^@\s]+@[^@\s]+\.[^@\s]+$"


class PenggunaIn(BaseModel):
    nama: str = Field(min_length=1, max_length=100)
    email: str = Field(max_length=100, pattern=EMAIL_PATTERN)


class PenggunaPatch(BaseModel):
    nama: Optional[str] = Field(default=None, min_length=1, max_length=100)
    email: Optional[str] = Field(default=None, max_length=100, pattern=EMAIL_PATTERN)


class KategoriIn(BaseModel):
    nama_kategori: str = Field(min_length=1, max_length=50)


class KategoriPatch(BaseModel):
    nama_kategori: Optional[str] = Field(default=None, min_length=1, max_length=50)


class MateriIn(BaseModel):
    judul: str = Field(min_length=1, max_length=150)
    isi: str = Field(min_length=1)
    id_kategori: int
    id_pengguna: int


class MateriPatch(BaseModel):
    judul: Optional[str] = Field(default=None, min_length=1, max_length=150)
    isi: Optional[str] = Field(default=None, min_length=1)
    id_kategori: Optional[int] = None
    id_pengguna: Optional[int] = None


class BookmarkIn(BaseModel):
    id_pengguna: int
    id_materi: int


class RiwayatIn(BaseModel):
    id_pengguna: int
    id_materi: int

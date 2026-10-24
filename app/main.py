from fastapi import FastAPI, HTTPException, Request
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from psycopg2 import errors as pgerr
from starlette.exceptions import HTTPException as StarletteHTTPException

from . import schemas
from .crud import build_router

app = FastAPI(
    title="TemanBelajar API",
    description="REST API platform belajar: materi, kategori, bookmark, dan riwayat baca.",
    version="1.0.0",
)


# ---------- Penanganan error: semua error berformat {"error": "..."} ----------
@app.exception_handler(StarletteHTTPException)
async def http_error(_: Request, exc: StarletteHTTPException):
    return JSONResponse({"error": exc.detail}, status_code=exc.status_code)


@app.exception_handler(RequestValidationError)
async def validation_error(_: Request, exc: RequestValidationError):
    err = exc.errors()[0]
    field = ".".join(str(p) for p in err["loc"] if p not in ("body", "path", "query"))
    if err["type"] == "missing":
        msg = f"Field {field} wajib diisi"
    else:
        msg = f"Field {field} tidak valid: {err['msg']}"
    return JSONResponse({"error": msg}, status_code=400)


@app.exception_handler(pgerr.UniqueViolation)
async def unique_error(_: Request, exc: pgerr.UniqueViolation):
    return JSONResponse({"error": "Data sudah ada (duplikat)"}, status_code=409)


@app.exception_handler(pgerr.ForeignKeyViolation)
async def fk_error(_: Request, exc: pgerr.ForeignKeyViolation):
    msg = (exc.diag.message_detail or "").lower()
    if "still referenced" in msg:
        text = "Data tidak bisa dihapus karena masih dipakai oleh data lain"
    else:
        text = "Data referensi (id_pengguna / id_materi / id_kategori) tidak ditemukan"
    return JSONResponse({"error": text}, status_code=409 if "still" in msg else 400)


@app.exception_handler(Exception)
async def server_error(_: Request, exc: Exception):
    return JSONResponse({"error": "Terjadi kesalahan pada server"}, status_code=500)


# ---------- Routes ----------
@app.get("/", tags=["Root"])
def root():
    return {
        "message": "TemanBelajar API berjalan",
        "docs": "/docs",
        "endpoints": ["/pengguna", "/kategori", "/materi", "/bookmark", "/riwayat"],
    }


app.include_router(
    build_router(
        prefix="/pengguna", tag="Pengguna", table="pengguna", pk="id_pengguna",
        label="Pengguna", create_model=schemas.PenggunaIn, patch_model=schemas.PenggunaPatch,
    )
)
app.include_router(
    build_router(
        prefix="/kategori", tag="Kategori", table="kategori", pk="id_kategori",
        label="Kategori", create_model=schemas.KategoriIn, patch_model=schemas.KategoriPatch,
    )
)
app.include_router(
    build_router(
        prefix="/materi", tag="Materi", table="materi", pk="id_materi", label="Materi",
        create_model=schemas.MateriIn, patch_model=schemas.MateriPatch,
        select_sql=(
            "SELECT materi.*, kategori.nama_kategori, pengguna.nama AS nama_pengguna "
            "FROM materi "
            "JOIN kategori ON kategori.id_kategori = materi.id_kategori "
            "JOIN pengguna ON pengguna.id_pengguna = materi.id_pengguna"
        ),
        filters=["id_kategori", "id_pengguna"],
    )
)
app.include_router(
    build_router(
        prefix="/bookmark", tag="Bookmark", table="bookmark", pk="id_bookmark",
        label="Bookmark", create_model=schemas.BookmarkIn,
        select_sql=(
            "SELECT bookmark.*, materi.judul, pengguna.nama AS nama_pengguna "
            "FROM bookmark "
            "JOIN materi ON materi.id_materi = bookmark.id_materi "
            "JOIN pengguna ON pengguna.id_pengguna = bookmark.id_pengguna"
        ),
        filters=["id_pengguna", "id_materi"],
    )
)
app.include_router(
    build_router(
        prefix="/riwayat", tag="Riwayat Materi", table="riwayat_materi", pk="id_riwayat",
        label="Riwayat", create_model=schemas.RiwayatIn,
        select_sql=(
            "SELECT riwayat_materi.*, materi.judul, pengguna.nama AS nama_pengguna "
            "FROM riwayat_materi "
            "JOIN materi ON materi.id_materi = riwayat_materi.id_materi "
            "JOIN pengguna ON pengguna.id_pengguna = riwayat_materi.id_pengguna"
        ),
        filters=["id_pengguna", "id_materi"],
    )
)

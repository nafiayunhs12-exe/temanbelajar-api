"""Pembuat router CRUD generik supaya kode tiap resource tidak berulang."""
from typing import Optional, Sequence, Type

from fastapi import APIRouter, HTTPException, Request
from pydantic import BaseModel

from .db import get_cursor


def build_router(
    *,
    prefix: str,
    tag: str,
    table: str,
    pk: str,
    label: str,
    create_model: Type[BaseModel],
    patch_model: Optional[Type[BaseModel]] = None,
    select_sql: Optional[str] = None,
    filters: Sequence[str] = (),
) -> APIRouter:
    """Buat router GET (list & detail), POST, PUT/PATCH (opsional), DELETE."""
    router = APIRouter(prefix=prefix, tags=[tag])
    base = select_sql or f"SELECT * FROM {table}"
    pk_col = f"{table}.{pk}"

    def fetch_one(cur, row_id: int):
        cur.execute(f"{base} WHERE {pk_col} = %s", (row_id,))
        row = cur.fetchone()
        if not row:
            raise HTTPException(404, f"{label} dengan id {row_id} tidak ditemukan")
        return row

    @router.get("", summary=f"Daftar {label}")
    def list_items(request: Request):
        where, params = [], []
        for col in filters:
            val = request.query_params.get(col)
            if val is not None:
                try:
                    params.append(int(val))
                except ValueError:
                    raise HTTPException(400, f"Parameter {col} harus berupa angka")
                where.append(f"{table}.{col} = %s")
        sql = base + (" WHERE " + " AND ".join(where) if where else "")
        with get_cursor() as cur:
            cur.execute(f"{sql} ORDER BY {pk_col}", params)
            rows = cur.fetchall()
        return {"message": f"Daftar {label} berhasil diambil", "total": len(rows), "data": rows}

    @router.get("/{item_id}", summary=f"Detail {label}")
    def get_item(item_id: int):
        with get_cursor() as cur:
            row = fetch_one(cur, item_id)
        return {"message": f"{label} berhasil diambil", "data": row}

    @router.post("", status_code=201, summary=f"Tambah {label}")
    def create_item(body: create_model):  # type: ignore[valid-type]
        data = body.model_dump()
        cols = ", ".join(data)
        marks = ", ".join(["%s"] * len(data))
        with get_cursor() as cur:
            cur.execute(
                f"INSERT INTO {table} ({cols}) VALUES ({marks}) RETURNING {pk}",
                list(data.values()),
            )
            new_id = cur.fetchone()[pk]
            row = fetch_one(cur, new_id)
        return {"message": f"{label} berhasil ditambahkan", "data": row}

    def _update(item_id: int, data: dict):
        if not data:
            raise HTTPException(400, "Tidak ada field yang dikirim untuk diubah")
        sets = ", ".join(f"{c} = %s" for c in data)
        with get_cursor() as cur:
            fetch_one(cur, item_id)
            cur.execute(
                f"UPDATE {table} SET {sets} WHERE {pk} = %s",
                [*data.values(), item_id],
            )
            row = fetch_one(cur, item_id)
        return {"message": f"{label} berhasil diperbarui", "data": row}

    if patch_model is not None:

        @router.put("/{item_id}", summary=f"Ubah seluruh data {label}")
        def put_item(item_id: int, body: create_model):  # type: ignore[valid-type]
            return _update(item_id, body.model_dump())

        @router.patch("/{item_id}", summary=f"Ubah sebagian data {label}")
        def patch_item(item_id: int, body: patch_model):  # type: ignore[valid-type]
            return _update(item_id, body.model_dump(exclude_unset=True))

    @router.delete("/{item_id}", summary=f"Hapus {label}")
    def delete_item(item_id: int):
        with get_cursor() as cur:
            row = fetch_one(cur, item_id)
            cur.execute(f"DELETE FROM {table} WHERE {pk} = %s", (item_id,))
        return {"message": f"{label} berhasil dihapus", "data": row}

    return router

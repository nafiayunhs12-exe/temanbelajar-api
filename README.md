# TemanBelajar API

REST API untuk platform **TemanBelajar**: pengguna membuat dan membaca materi belajar yang dikelompokkan per kategori, menyimpan materi ke bookmark, dan memiliki riwayat materi yang pernah dibaca.

Dibangun dengan **Python + FastAPI**, database **PostgreSQL** (online), dan di-deploy ke **Vercel**.

- **URL Deployment** : https://temanbelajar-api.vercel.app  *(contoh; ganti dengan URL deployment milikmu jika berbeda)*
- **Swagger UI**     : https://temanbelajar-api.vercel.app/docs

## ERD / Skema Database

5 tabel yang berelasi lewat foreign key. File sumber: [`schema.sql`](schema.sql), [`docs/erd.dbml`](docs/erd.dbml) (tempel ke dbdiagram.io untuk gambar ERD).

```mermaid
erDiagram
    pengguna ||--o{ materi : "menulis"
    kategori ||--o{ materi : "mengelompokkan"
    pengguna ||--o{ bookmark : "menyimpan"
    materi   ||--o{ bookmark : "disimpan"
    pengguna ||--o{ riwayat_materi : "membaca"
    materi   ||--o{ riwayat_materi : "dibaca"

    pengguna { int id_pengguna PK
               string nama
               string email UK }
    kategori { int id_kategori PK
               string nama_kategori }
    materi   { int id_materi PK
               string judul
               text isi
               int id_kategori FK
               int id_pengguna FK }
    bookmark { int id_bookmark PK
               int id_pengguna FK
               int id_materi FK }
    riwayat_materi { int id_riwayat PK
               int id_pengguna FK
               int id_materi FK
               timestamp tanggal_dibaca }
```

Relasi: `pengguna` 1–N `materi`, `kategori` 1–N `materi`, dan `pengguna` N–M `materi` lewat tabel pivot `bookmark` (unik per pasangan) serta `riwayat_materi`.

## Ringkasan Endpoint

| Resource | GET (list/detail) | POST | PUT / PATCH | DELETE |
|---|---|---|---|---|
| `/pengguna` | ✅ | ✅ | ✅ | ✅ |
| `/kategori` | ✅ | ✅ | ✅ | ✅ |
| `/materi` | ✅ (filter `id_kategori`, `id_pengguna`) | ✅ | ✅ | ✅ |
| `/bookmark` | ✅ (filter `id_pengguna`, `id_materi`) | ✅ | – | ✅ |
| `/riwayat` | ✅ (filter `id_pengguna`, `id_materi`) | ✅ | – | ✅ |

Format sukses: `{"message": "...", "data": ...}`. Format error: `{"error": "..."}` dengan status `400` (input salah / referensi tidak ada), `404` (tidak ditemukan), `409` (duplikat / masih dipakai data lain), `500` (error server).

## Dokumentasi Endpoint

### Daftar Pengguna
- Method       : GET
- URL          : https://temanbelajar-api.vercel.app/pengguna
- Deskripsi    : Mengambil semua data pengguna
- Response Sukses (200):
```json
{
  "message": "Daftar pengguna berhasil diambil",
  "total": 1,
  "data": [
    {
      "id_pengguna": 1,
      "nama": "Nafia Yunu",
      "email": "nafia@example.com"
    }
  ]
}
```

### Detail Pengguna
- Method       : GET
- URL          : https://temanbelajar-api.vercel.app/pengguna/1
- Deskripsi    : Mengambil satu pengguna berdasarkan id
- Response Sukses (200):
```json
{
  "message": "Pengguna berhasil diambil",
  "data": {
    "id_pengguna": 1,
    "nama": "Nafia Yunu",
    "email": "nafia@example.com"
  }
}
```
- Response Error (404):
```json
{
  "error": "Pengguna dengan id 999 tidak ditemukan"
}
```

### Tambah Pengguna
- Method       : POST
- URL          : https://temanbelajar-api.vercel.app/pengguna
- Deskripsi    : Menambahkan pengguna baru
- Headers      : Content-Type: application/json
- Request Body :
```json
{
  "nama": "Dina Putri",
  "email": "dina@example.com"
}
```
- Response Sukses (201):
```json
{
  "message": "Pengguna berhasil ditambahkan",
  "data": {
    "id_pengguna": 10,
    "nama": "Nafia Yunu",
    "email": "nafia@example.com"
  }
}
```
- Response Error (400):
```json
{
  "error": "Field nama wajib diisi"
}
```

### Ubah Seluruh Pengguna
- Method       : PUT
- URL          : https://temanbelajar-api.vercel.app/pengguna/1
- Deskripsi    : Mengganti seluruh data pengguna (semua field wajib dikirim)
- Headers      : Content-Type: application/json
- Request Body :
```json
{
  "nama": "Dina Putri",
  "email": "dina@example.com"
}
```
- Response Sukses (200):
```json
{
  "message": "Pengguna berhasil diperbarui",
  "data": {
    "id_pengguna": 1,
    "nama": "Dina Putri",
    "email": "dina@example.com"
  }
}
```
- Response Error (400):
```json
{
  "error": "Field nama wajib diisi"
}
```

### Ubah Sebagian Pengguna
- Method       : PATCH
- URL          : https://temanbelajar-api.vercel.app/pengguna/1
- Deskripsi    : Mengubah sebagian field pengguna
- Headers      : Content-Type: application/json
- Request Body :
```json
{
  "nama": "Dina Putri Aulia"
}
```
- Response Sukses (200):
```json
{
  "message": "Pengguna berhasil diperbarui",
  "data": {
    "id_pengguna": 1,
    "nama": "Dina Putri Aulia",
    "email": "nafia@example.com"
  }
}
```
- Response Error (400):
```json
{
  "error": "Tidak ada field yang dikirim untuk diubah"
}
```

### Hapus Pengguna
- Method       : DELETE
- URL          : https://temanbelajar-api.vercel.app/pengguna/10
- Deskripsi    : Menghapus pengguna berdasarkan id
- Response Sukses (200):
```json
{
  "message": "Pengguna berhasil dihapus",
  "data": {
    "id_pengguna": 10,
    "nama": "Nafia Yunu",
    "email": "nafia@example.com"
  }
}
```
- Response Error (409):
```json
{
  "error": "Data tidak bisa dihapus karena masih dipakai oleh data lain"
}
```

### Daftar Kategori
- Method       : GET
- URL          : https://temanbelajar-api.vercel.app/kategori
- Deskripsi    : Mengambil semua data kategori
- Response Sukses (200):
```json
{
  "message": "Daftar kategori berhasil diambil",
  "total": 1,
  "data": [
    {
      "id_kategori": 1,
      "nama_kategori": "Pemrograman"
    }
  ]
}
```

### Detail Kategori
- Method       : GET
- URL          : https://temanbelajar-api.vercel.app/kategori/1
- Deskripsi    : Mengambil satu kategori berdasarkan id
- Response Sukses (200):
```json
{
  "message": "Kategori berhasil diambil",
  "data": {
    "id_kategori": 1,
    "nama_kategori": "Pemrograman"
  }
}
```
- Response Error (404):
```json
{
  "error": "Kategori dengan id 999 tidak ditemukan"
}
```

### Tambah Kategori
- Method       : POST
- URL          : https://temanbelajar-api.vercel.app/kategori
- Deskripsi    : Menambahkan kategori baru
- Headers      : Content-Type: application/json
- Request Body :
```json
{
  "nama_kategori": "Sains"
}
```
- Response Sukses (201):
```json
{
  "message": "Kategori berhasil ditambahkan",
  "data": {
    "id_kategori": 10,
    "nama_kategori": "Pemrograman"
  }
}
```
- Response Error (400):
```json
{
  "error": "Field nama_kategori wajib diisi"
}
```

### Ubah Seluruh Kategori
- Method       : PUT
- URL          : https://temanbelajar-api.vercel.app/kategori/1
- Deskripsi    : Mengganti seluruh data kategori (semua field wajib dikirim)
- Headers      : Content-Type: application/json
- Request Body :
```json
{
  "nama_kategori": "Sains"
}
```
- Response Sukses (200):
```json
{
  "message": "Kategori berhasil diperbarui",
  "data": {
    "id_kategori": 1,
    "nama_kategori": "Sains"
  }
}
```
- Response Error (400):
```json
{
  "error": "Field nama_kategori wajib diisi"
}
```

### Ubah Sebagian Kategori
- Method       : PATCH
- URL          : https://temanbelajar-api.vercel.app/kategori/1
- Deskripsi    : Mengubah sebagian field kategori
- Headers      : Content-Type: application/json
- Request Body :
```json
{
  "nama_kategori": "Sains Dasar"
}
```
- Response Sukses (200):
```json
{
  "message": "Kategori berhasil diperbarui",
  "data": {
    "id_kategori": 1,
    "nama_kategori": "Sains Dasar"
  }
}
```
- Response Error (400):
```json
{
  "error": "Tidak ada field yang dikirim untuk diubah"
}
```

### Hapus Kategori
- Method       : DELETE
- URL          : https://temanbelajar-api.vercel.app/kategori/10
- Deskripsi    : Menghapus kategori berdasarkan id
- Response Sukses (200):
```json
{
  "message": "Kategori berhasil dihapus",
  "data": {
    "id_kategori": 10,
    "nama_kategori": "Pemrograman"
  }
}
```
- Response Error (409):
```json
{
  "error": "Data tidak bisa dihapus karena masih dipakai oleh data lain"
}
```

### Daftar Materi
- Method       : GET
- URL          : https://temanbelajar-api.vercel.app/materi?id_kategori=1&id_pengguna=1
- Deskripsi    : Mengambil semua data materi (opsional filter query: ?id_kategori=1&id_pengguna=1)
- Response Sukses (200):
```json
{
  "message": "Daftar materi berhasil diambil",
  "total": 1,
  "data": [
    {
      "id_materi": 1,
      "judul": "Dasar Python",
      "isi": "Variabel, tipe data, percabangan, dan perulangan.",
      "id_kategori": 1,
      "id_pengguna": 1,
      "nama_kategori": "Pemrograman",
      "nama_pengguna": "Nafia Yunu"
    }
  ]
}
```
- Response Error (400):
```json
{
  "error": "Parameter id_pengguna harus berupa angka"
}
```

### Detail Materi
- Method       : GET
- URL          : https://temanbelajar-api.vercel.app/materi/1
- Deskripsi    : Mengambil satu materi berdasarkan id
- Response Sukses (200):
```json
{
  "message": "Materi berhasil diambil",
  "data": {
    "id_materi": 1,
    "judul": "Dasar Python",
    "isi": "Variabel, tipe data, percabangan, dan perulangan.",
    "id_kategori": 1,
    "id_pengguna": 1,
    "nama_kategori": "Pemrograman",
    "nama_pengguna": "Nafia Yunu"
  }
}
```
- Response Error (404):
```json
{
  "error": "Materi dengan id 999 tidak ditemukan"
}
```

### Tambah Materi
- Method       : POST
- URL          : https://temanbelajar-api.vercel.app/materi
- Deskripsi    : Menambahkan materi baru
- Headers      : Content-Type: application/json
- Request Body :
```json
{
  "judul": "Pengenalan HTML",
  "isi": "Struktur dasar halaman web.",
  "id_kategori": 1,
  "id_pengguna": 1
}
```
- Response Sukses (201):
```json
{
  "message": "Materi berhasil ditambahkan",
  "data": {
    "id_materi": 10,
    "judul": "Dasar Python",
    "isi": "Variabel, tipe data, percabangan, dan perulangan.",
    "id_kategori": 1,
    "id_pengguna": 1,
    "nama_kategori": "Pemrograman",
    "nama_pengguna": "Nafia Yunu"
  }
}
```
- Response Error (400):
```json
{
  "error": "Field judul wajib diisi"
}
```

### Ubah Seluruh Materi
- Method       : PUT
- URL          : https://temanbelajar-api.vercel.app/materi/1
- Deskripsi    : Mengganti seluruh data materi (semua field wajib dikirim)
- Headers      : Content-Type: application/json
- Request Body :
```json
{
  "judul": "Pengenalan HTML",
  "isi": "Struktur dasar halaman web.",
  "id_kategori": 1,
  "id_pengguna": 1
}
```
- Response Sukses (200):
```json
{
  "message": "Materi berhasil diperbarui",
  "data": {
    "id_materi": 1,
    "judul": "Pengenalan HTML",
    "isi": "Struktur dasar halaman web.",
    "id_kategori": 1,
    "id_pengguna": 1,
    "nama_kategori": "Pemrograman",
    "nama_pengguna": "Nafia Yunu"
  }
}
```
- Response Error (400):
```json
{
  "error": "Field judul wajib diisi"
}
```

### Ubah Sebagian Materi
- Method       : PATCH
- URL          : https://temanbelajar-api.vercel.app/materi/1
- Deskripsi    : Mengubah sebagian field materi
- Headers      : Content-Type: application/json
- Request Body :
```json
{
  "judul": "Pengenalan HTML & CSS"
}
```
- Response Sukses (200):
```json
{
  "message": "Materi berhasil diperbarui",
  "data": {
    "id_materi": 1,
    "judul": "Pengenalan HTML & CSS",
    "isi": "Variabel, tipe data, percabangan, dan perulangan.",
    "id_kategori": 1,
    "id_pengguna": 1,
    "nama_kategori": "Pemrograman",
    "nama_pengguna": "Nafia Yunu"
  }
}
```
- Response Error (400):
```json
{
  "error": "Tidak ada field yang dikirim untuk diubah"
}
```

### Hapus Materi
- Method       : DELETE
- URL          : https://temanbelajar-api.vercel.app/materi/10
- Deskripsi    : Menghapus materi berdasarkan id
- Response Sukses (200):
```json
{
  "message": "Materi berhasil dihapus",
  "data": {
    "id_materi": 10,
    "judul": "Dasar Python",
    "isi": "Variabel, tipe data, percabangan, dan perulangan.",
    "id_kategori": 1,
    "id_pengguna": 1,
    "nama_kategori": "Pemrograman",
    "nama_pengguna": "Nafia Yunu"
  }
}
```
- Response Error (409):
```json
{
  "error": "Data tidak bisa dihapus karena masih dipakai oleh data lain"
}
```

### Daftar Bookmark
- Method       : GET
- URL          : https://temanbelajar-api.vercel.app/bookmark?id_pengguna=1
- Deskripsi    : Mengambil semua data bookmark (opsional filter query: ?id_pengguna=1)
- Response Sukses (200):
```json
{
  "message": "Daftar bookmark berhasil diambil",
  "total": 1,
  "data": [
    {
      "id_bookmark": 1,
      "id_pengguna": 1,
      "id_materi": 2,
      "judul": "Pengenalan SQL",
      "nama_pengguna": "Nafia Yunu"
    }
  ]
}
```
- Response Error (400):
```json
{
  "error": "Parameter id_pengguna harus berupa angka"
}
```

### Detail Bookmark
- Method       : GET
- URL          : https://temanbelajar-api.vercel.app/bookmark/1
- Deskripsi    : Mengambil satu bookmark berdasarkan id
- Response Sukses (200):
```json
{
  "message": "Bookmark berhasil diambil",
  "data": {
    "id_bookmark": 1,
    "id_pengguna": 1,
    "id_materi": 2,
    "judul": "Pengenalan SQL",
    "nama_pengguna": "Nafia Yunu"
  }
}
```
- Response Error (404):
```json
{
  "error": "Bookmark dengan id 999 tidak ditemukan"
}
```

### Tambah Bookmark
- Method       : POST
- URL          : https://temanbelajar-api.vercel.app/bookmark
- Deskripsi    : Menambahkan bookmark baru
- Headers      : Content-Type: application/json
- Request Body :
```json
{
  "id_pengguna": 1,
  "id_materi": 3
}
```
- Response Sukses (201):
```json
{
  "message": "Bookmark berhasil ditambahkan",
  "data": {
    "id_bookmark": 10,
    "id_pengguna": 1,
    "id_materi": 2,
    "judul": "Pengenalan SQL",
    "nama_pengguna": "Nafia Yunu"
  }
}
```
- Response Error (400):
```json
{
  "error": "Field id_materi wajib diisi"
}
```

### Hapus Bookmark
- Method       : DELETE
- URL          : https://temanbelajar-api.vercel.app/bookmark/10
- Deskripsi    : Menghapus bookmark berdasarkan id
- Response Sukses (200):
```json
{
  "message": "Bookmark berhasil dihapus",
  "data": {
    "id_bookmark": 10,
    "id_pengguna": 1,
    "id_materi": 2,
    "judul": "Pengenalan SQL",
    "nama_pengguna": "Nafia Yunu"
  }
}
```
- Response Error (404):
```json
{
  "error": "Bookmark dengan id 999 tidak ditemukan"
}
```

### Daftar Riwayat
- Method       : GET
- URL          : https://temanbelajar-api.vercel.app/riwayat?id_pengguna=1
- Deskripsi    : Mengambil semua data riwayat (opsional filter query: ?id_pengguna=1)
- Response Sukses (200):
```json
{
  "message": "Daftar riwayat berhasil diambil",
  "total": 1,
  "data": [
    {
      "id_riwayat": 1,
      "id_pengguna": 1,
      "id_materi": 1,
      "tanggal_dibaca": "2026-10-23T09:30:00",
      "judul": "Dasar Python",
      "nama_pengguna": "Nafia Yunu"
    }
  ]
}
```
- Response Error (400):
```json
{
  "error": "Parameter id_pengguna harus berupa angka"
}
```

### Detail Riwayat
- Method       : GET
- URL          : https://temanbelajar-api.vercel.app/riwayat/1
- Deskripsi    : Mengambil satu riwayat berdasarkan id
- Response Sukses (200):
```json
{
  "message": "Riwayat berhasil diambil",
  "data": {
    "id_riwayat": 1,
    "id_pengguna": 1,
    "id_materi": 1,
    "tanggal_dibaca": "2026-10-23T09:30:00",
    "judul": "Dasar Python",
    "nama_pengguna": "Nafia Yunu"
  }
}
```
- Response Error (404):
```json
{
  "error": "Riwayat dengan id 999 tidak ditemukan"
}
```

### Tambah Riwayat
- Method       : POST
- URL          : https://temanbelajar-api.vercel.app/riwayat
- Deskripsi    : Menambahkan riwayat baru
- Headers      : Content-Type: application/json
- Request Body :
```json
{
  "id_pengguna": 1,
  "id_materi": 2
}
```
- Response Sukses (201):
```json
{
  "message": "Riwayat berhasil ditambahkan",
  "data": {
    "id_riwayat": 10,
    "id_pengguna": 1,
    "id_materi": 1,
    "tanggal_dibaca": "2026-10-23T09:30:00",
    "judul": "Dasar Python",
    "nama_pengguna": "Nafia Yunu"
  }
}
```
- Response Error (400):
```json
{
  "error": "Field id_pengguna wajib diisi"
}
```

### Hapus Riwayat
- Method       : DELETE
- URL          : https://temanbelajar-api.vercel.app/riwayat/10
- Deskripsi    : Menghapus riwayat berdasarkan id
- Response Sukses (200):
```json
{
  "message": "Riwayat berhasil dihapus",
  "data": {
    "id_riwayat": 10,
    "id_pengguna": 1,
    "id_materi": 1,
    "tanggal_dibaca": "2026-10-23T09:30:00",
    "judul": "Dasar Python",
    "nama_pengguna": "Nafia Yunu"
  }
}
```
- Response Error (404):
```json
{
  "error": "Riwayat dengan id 999 tidak ditemukan"
}
```

## Menjalankan Secara Lokal

1. Siapkan database PostgreSQL (lokal atau online seperti Neon/Supabase), lalu jalankan:
   ```bash
   psql "$DATABASE_URL" -f schema.sql
   psql "$DATABASE_URL" -f seed.sql   # opsional, data contoh
   ```
2. Buat virtual environment dan install dependensi:
   ```bash
   python -m venv .venv && source .venv/bin/activate
   pip install -r requirements.txt
   ```
3. Atur environment variable (lihat `.env.example`):
   ```bash
   export DATABASE_URL="postgresql://USER:PASSWORD@HOST/DBNAME?sslmode=require"
   ```
4. Jalankan server:
   ```bash
   uvicorn app.main:app --reload
   ```
   Buka http://127.0.0.1:8000/docs.

## Deploy ke Vercel

1. Buat database di Neon atau Supabase, jalankan `schema.sql` (dan `seed.sql`) lewat SQL editor mereka.
2. Push repo ke GitHub, lalu import ke Vercel.
3. Di **Settings → Environment Variables** tambahkan `DATABASE_URL` (connection string database). Jangan menaruhnya di kode.
4. Deploy. `vercel.json` mengarahkan semua request ke `api/index.py`.

## Pengujian

Import [`docs/TemanBelajar.postman_collection.json`](docs/TemanBelajar.postman_collection.json) ke Postman / Thunder Client, ubah variabel `base_url` ke URL Vercel, lalu jalankan semua request. Setiap request sudah punya tes status code.

## Struktur Project

```
app/main.py      aplikasi FastAPI, routes, penanganan error
app/crud.py      pembuat router CRUD generik
app/schemas.py   validasi request (Pydantic)
app/db.py        koneksi PostgreSQL
api/index.py     entry point Vercel
schema.sql       struktur tabel
seed.sql         data contoh
```


## Checklist Pengumpulan

- [x] Database minimal 5 tabel
- [x] Relasi foreign key
- [x] CRUD lengkap pada resource utama `materi`
- [x] GET, POST, PUT, PATCH, DELETE
- [x] JSON request/response
- [x] Validasi input
- [x] Error 400, 404, 409, 500
- [x] ERD dalam `docs/erd.dbml`
- [x] Postman Collection dalam `docs/TemanBelajar.postman_collection.json`
- [x] Dokumentasi endpoint dalam `docs/endpoints.md`
- [x] Konfigurasi Vercel
- [x] Isi `DATABASE_URL` di environment Vercel
- [x] Pastikan deployment Vercel aktif
- [x] Test menggunakan URL Vercel
- [x] Screenshot hasil testing untuk bukti pengumpulan
- [x] Upload repository ke GitHub
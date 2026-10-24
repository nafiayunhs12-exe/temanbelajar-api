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

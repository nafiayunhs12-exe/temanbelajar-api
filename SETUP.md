# Panduan Setup TemanBelajar

## A. Database PostgreSQL
1. Buat database PostgreSQL online (misalnya Supabase/Neon).
2. Jalankan `schema.sql`.
3. Jalankan `seed.sql`.
4. Salin connection string PostgreSQL sebagai `DATABASE_URL`.

## B. Jalankan lokal
```bash
python -m venv .venv
# Windows:
.venv\Scripts\activate
# macOS/Linux:
# source .venv/bin/activate

pip install -r requirements.txt
```

Buat `.env`:
```env
DATABASE_URL=postgresql://username:password@host:5432/database
```

Jalankan:
```bash
uvicorn app.main:app --reload
```

Buka:
- API: http://127.0.0.1:8000
- Swagger: http://127.0.0.1:8000/docs

## C. Vercel
1. Push folder ini ke GitHub.
2. Import repository ke Vercel.
3. Tambahkan Environment Variable `DATABASE_URL`.
4. Deploy.
5. Tes URL deployment melalui browser, Swagger, atau Postman.

## D. ERD
Buka `docs/erd.dbml`, lalu tempel isinya ke dbdiagram.io untuk membuat gambar ERD.

## E. Postman
Import:
`docs/TemanBelajar.postman_collection.json`

Sebelum testing, sesuaikan base URL jika deployment bukan:
`https://temanbelajar-api.vercel.app`

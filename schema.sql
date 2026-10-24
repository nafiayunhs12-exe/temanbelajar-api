-- Struktur Database TemanBelajar
-- PostgreSQL

-- Tabel pengguna
CREATE TABLE pengguna (
    id_pengguna SERIAL PRIMARY KEY,
    nama VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL
);

-- Tabel kategori materi
CREATE TABLE kategori (
    id_kategori SERIAL PRIMARY KEY,
    nama_kategori VARCHAR(50) NOT NULL
);

-- Tabel materi
CREATE TABLE materi (
    id_materi SERIAL PRIMARY KEY,
    judul VARCHAR(150) NOT NULL,
    isi TEXT NOT NULL,
    id_kategori INT NOT NULL,
    id_pengguna INT NOT NULL,
    FOREIGN KEY (id_kategori) REFERENCES kategori(id_kategori),
    FOREIGN KEY (id_pengguna) REFERENCES pengguna(id_pengguna)
);

-- Tabel materi yang disimpan pengguna
CREATE TABLE bookmark (
    id_bookmark SERIAL PRIMARY KEY,
    id_pengguna INT NOT NULL,
    id_materi INT NOT NULL,
    FOREIGN KEY (id_pengguna) REFERENCES pengguna(id_pengguna),
    FOREIGN KEY (id_materi) REFERENCES materi(id_materi),
    UNIQUE (id_pengguna, id_materi)
);

-- Tabel riwayat materi yang dibaca
CREATE TABLE riwayat_materi (
    id_riwayat SERIAL PRIMARY KEY,
    id_pengguna INT NOT NULL,
    id_materi INT NOT NULL,
    tanggal_dibaca TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (id_pengguna) REFERENCES pengguna(id_pengguna),
    FOREIGN KEY (id_materi) REFERENCES materi(id_materi)
);

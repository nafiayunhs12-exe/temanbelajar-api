-- Data contoh (jalankan setelah schema.sql)
INSERT INTO pengguna (nama, email) VALUES
  ('Nafia Yunu', 'nafia@example.com'),
  ('Budi Santoso', 'budi@example.com'),
  ('Citra Lestari', 'citra@example.com');

INSERT INTO kategori (nama_kategori) VALUES
  ('Pemrograman'), ('Matematika'), ('Bahasa Inggris');

INSERT INTO materi (judul, isi, id_kategori, id_pengguna) VALUES
  ('Dasar Python', 'Variabel, tipe data, percabangan, dan perulangan.', 1, 1),
  ('Pengenalan SQL', 'SELECT, INSERT, UPDATE, DELETE, dan JOIN.', 1, 2),
  ('Aljabar Linear Dasar', 'Vektor, matriks, dan operasinya.', 2, 3),
  ('Simple Past Tense', 'Pola kalimat dan contoh penggunaan.', 3, 1);

INSERT INTO bookmark (id_pengguna, id_materi) VALUES (1, 2), (2, 1), (3, 4);

INSERT INTO riwayat_materi (id_pengguna, id_materi) VALUES (1, 1), (1, 2), (2, 3);

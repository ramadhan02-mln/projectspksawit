# SPK Pemilihan Lokasi Pendirian Pabrik Kelapa Sawit - MOORA

## Isi project
- `app.py`: antarmuka Streamlit dengan struktur navigasi lima halaman yang dipertahankan dari project awal.
- `data.py`: alternatif lokasi, kriteria, bobot, dan jenis kriteria.
- `moora.py`: perhitungan normalisasi vektor dan nilai optimasi MOORA berbobot.
- `test_moora.py`: uji sederhana perhitungan.
- `requirements.txt`: dependensi Python.
- `JALANKAN_APLIKASI.bat`: instalasi dependensi dan menjalankan aplikasi pada Windows.

## Menjalankan di Windows
1. Ekstrak seluruh ZIP ke folder yang mudah ditemukan.
2. Pastikan Python 3.10 atau lebih baru sudah terpasang dan opsi **Add Python to PATH** diaktifkan.
3. Pastikan komputer terhubung ke internet untuk pemasangan library pada proses pertama.
4. Klik dua kali `JALANKAN_APLIKASI.bat`.
5. Tunggu sampai Streamlit membuka alamat aplikasi pada browser. Jika browser tidak terbuka otomatis, buka alamat lokal yang ditampilkan di terminal (biasanya `http://localhost:8501`).

## Menjalankan manual (Windows/macOS/Linux)
```bash
python -m venv .venv
# Windows:
.venv\\Scripts\\activate
# macOS/Linux:
source .venv/bin/activate
python -m pip install -r requirements.txt
python -m streamlit run app.py
```

## Menguji perhitungan
```bash
python test_moora.py
```

## Catatan akademik penting
- UI dan pola navigasi awal dipertahankan: Dashboard, Data Alternatif, Data Kriteria, Normalisasi, dan Hasil Perangkingan. Label dan konten diubah dari seleksi beasiswa KIP-K/SAW menjadi pemilihan lokasi pabrik kelapa sawit/MOORA.
- Dataset di `data.py` merupakan data simulasi yang mengikuti rancangan Bab III, bukan data survei lapangan.
- Bobot: C1 0,24; C2 0,27; C3 0,19; C4 0,14; C5 0,16.
- Klasifikasi saat ini: C1 Cost, C2 Benefit, C3 Cost, C4 Benefit, C5 Benefit. Definisi operasional C1 dan C3 perlu dikonfirmasi. Jika angka yang lebih besar pada kedua kriteria tersebut berarti lahan/air semakin tersedia atau semakin baik, klasifikasinya semestinya Benefit, bukan Cost. Perubahan klasifikasi akan mengubah hasil perangkingan.
- MOORA di project ini menggunakan normalisasi vektor dan penjumlahan berbobot untuk Benefit dikurangi Cost (weighted MOORA). Pastikan penjelasan Bab III/IV menyebut varian berbobot ini secara konsisten.
- Aplikasi merupakan alat bantu analisis, bukan pengganti survei teknis, kajian lingkungan, tata ruang, ketersediaan bahan baku, dan evaluasi kelayakan lokasi oleh pihak berwenang.

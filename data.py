import pandas as pd

# Alternatif lokasi sesuai rancangan pembahasan Bab III.
# Nilai di bawah merupakan DATA SIMULASI, bukan hasil survei lapangan.
data_alternatif = {
    "Alternatif": [
        "A1 - Molosipat Utara",
        "A2 - Botu",
        "A3 - Bolihutuo",
        "A4 - Bilonlantunga",
        "A5 - Pinontoyonga",
    ],
    "C1": [50, 50, 40, 30, 50],
    "C2": [50, 40, 50, 30, 50],
    "C3": [50, 50, 40, 30, 50],
    "C4": [50, 40, 50, 30, 50],
    "C5": [50, 30, 40, 50, 30],
}

df_alternatif = pd.DataFrame(data_alternatif)

data_kriteria = {
    "Kode": ["C1", "C2", "C3", "C4", "C5"],
    "Kriteria": [
        "Luas Lahan",
        "Kedekatan dengan Sumber Bahan Baku",
        "Ketersediaan Sumber Air",
        "Akses Jalan",
        "Kedekatan dengan Pelabuhan",
    ],
    "Bobot": [0.24, 0.27, 0.19, 0.14, 0.16],
    "Jenis": ["Cost", "Benefit", "Cost", "Benefit", "Benefit"],
}

df_kriteria = pd.DataFrame(data_kriteria)

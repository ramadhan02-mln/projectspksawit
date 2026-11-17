import pandas as pd
from data import df_alternatif, df_kriteria


def hitung_moora(alternatif=None, kriteria=None):
    """
    Menghitung MOORA dengan normalisasi vektor dan pembobotan kriteria.
    Nilai optimasi = jumlah (bobot x normalisasi) benefit
                    - jumlah (bobot x normalisasi) cost.
    """
    alternatif = df_alternatif.copy() if alternatif is None else alternatif.copy()
    kriteria = df_kriteria.copy() if kriteria is None else kriteria.copy()

    kode = kriteria["Kode"].tolist()
    matriks = alternatif.set_index("Alternatif")[kode].astype(float)

    if matriks.empty:
        raise ValueError("Data alternatif belum tersedia.")
    if (matriks < 0).any().any():
        raise ValueError("Nilai matriks keputusan tidak boleh negatif.")
    if kriteria["Bobot"].isna().any() or (kriteria["Bobot"] < 0).any():
        raise ValueError("Bobot harus berupa angka nonnegatif.")
    if abs(float(kriteria["Bobot"].sum()) - 1.0) > 1e-6:
        raise ValueError("Total bobot kriteria harus sama dengan 1.00.")
    if not set(kriteria["Jenis"]).issubset({"Benefit", "Cost"}):
        raise ValueError("Jenis kriteria harus Benefit atau Cost.")

    penyebut = (matriks.pow(2).sum(axis=0)).pow(0.5)
    if (penyebut == 0).any():
        raise ValueError("Terdapat kriteria dengan seluruh nilai nol.")

    normalisasi = matriks.div(penyebut, axis=1)
    bobot = kriteria.set_index("Kode")["Bobot"]
    normalisasi_terbobot = normalisasi.mul(bobot, axis=1)

    benefit = kriteria.loc[kriteria["Jenis"] == "Benefit", "Kode"].tolist()
    cost = kriteria.loc[kriteria["Jenis"] == "Cost", "Kode"].tolist()

    nilai_benefit = normalisasi_terbobot[benefit].sum(axis=1) if benefit else 0
    nilai_cost = normalisasi_terbobot[cost].sum(axis=1) if cost else 0
    nilai_optimasi = nilai_benefit - nilai_cost

    hasil = pd.DataFrame({
        "Alternatif": matriks.index,
        "Nilai Benefit": nilai_benefit.values if hasattr(nilai_benefit, "values") else [nilai_benefit] * len(matriks),
        "Nilai Cost": nilai_cost.values if hasattr(nilai_cost, "values") else [nilai_cost] * len(matriks),
        "Nilai Optimasi": nilai_optimasi.values if hasattr(nilai_optimasi, "values") else [nilai_optimasi] * len(matriks),
    })
    hasil = hasil.sort_values("Nilai Optimasi", ascending=False).reset_index(drop=True)
    hasil.insert(0, "Peringkat", range(1, len(hasil) + 1))

    penyebut_df = pd.DataFrame({
        "Kode": penyebut.index,
        "Penyebut Normalisasi": penyebut.values,
    })
    return normalisasi, normalisasi_terbobot, penyebut_df, hasil

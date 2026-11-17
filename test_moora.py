from moora import hitung_moora

normalisasi, terbobot, penyebut, ranking = hitung_moora()

assert normalisasi.shape == (5, 5)
assert terbobot.shape == (5, 5)
assert len(ranking) == 5
assert ranking["Peringkat"].tolist() == [1, 2, 3, 4, 5]
assert ranking["Nilai Optimasi"].is_monotonic_decreasing
print("Uji MOORA berhasil.")
print(ranking.to_string(index=False))

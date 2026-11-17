import streamlit as st
import pandas as pd
from data import df_alternatif, df_kriteria
from moora import hitung_moora

st.set_page_config(page_title="SPK Lokasi Pabrik Kelapa Sawit", page_icon="🌴", layout="wide", initial_sidebar_state="expanded")

st.markdown("""
<style>

/* =====================================================
    GLOBAL
===================================================== */

.stApp {
    background: linear-gradient(
        135deg,
        #F4FDFF 0%,
        #FFFFFF 50%,
        #E9FAFD 100%
    ) !important;
    color: #31596A;
    font-family: 'Segoe UI', sans-serif;
}

[data-testid="stAppViewContainer"] {
    background: transparent !important;
}

[data-testid="stMain"] {
    background: transparent !important;
}

[data-testid="stMainBlockContainer"] {
    padding-top: 2rem;
    padding-bottom: 3rem;
    max-width: 1500px;
}

[data-testid="stHeader"] {
    background: rgba(255,255,255,0.95) !important;
}

/* =====================================================
    SIDEBAR
===================================================== */

[data-testid="stSidebar"] {
    background: linear-gradient(
        180deg,
        #08B8D0 0%,
        #06A9C5 50%,
        #078DAF 100%
    ) !important;
    border-right: 1px solid #079BB5;
}

[data-testid="stSidebar"] > div:first-child {
    background: transparent !important;
    padding-top: 2rem;
}

[data-testid="stSidebar"] h3 {
    color: #FFFFFF !important;
    font-weight: 900 !important;
    letter-spacing: 1px;
}

[data-testid="stSidebar"] p {
    color: #E8FCFF !important;
}

[data-testid="stSidebar"] hr {
    border-color: rgba(255,255,255,0.3) !important;
}

[data-testid="stSidebar"] .stRadio label {
    color: #FFFFFF !important;
    font-weight: 600;
}

[data-testid="stSidebar"] .stRadio div[role="radiogroup"] {
    gap: 9px;
}

[data-testid="stSidebar"] .stRadio div[role="radiogroup"] label {
    background: rgba(255,255,255,0.13);
    border: 1px solid rgba(255,255,255,0.25);
    border-radius: 11px;
    padding: 11px 13px;
    transition: all 0.2s ease;
}

[data-testid="stSidebar"] .stRadio div[role="radiogroup"] label:hover {
    background: rgba(255,255,255,0.28);
    border-color: #FFFFFF;
}

[data-testid="stSidebar"] .stRadio div[role="radiogroup"] label:has(input:checked) {
    background: #FFFFFF !important;
    border-color: #FFFFFF !important;
    box-shadow: 0 3px 12px rgba(0,70,90,0.15);
}

[data-testid="stSidebar"] .stRadio div[role="radiogroup"] label:has(input:checked) p {
    color: #0789A8 !important;
    font-weight: 800 !important;
}

.sidebar-method {
    background: #FFFFFF;
    border: 1px solid rgba(255,255,255,0.8);
    border-radius: 12px;
    padding: 14px;
    color: #0789A8;
    font-weight: 800;
    box-shadow: 0 4px 12px rgba(0,70,90,0.08);
}

.sidebar-method small {
    display: block;
    color: #64818D;
    font-size: 11px;
    font-weight: 500;
    margin-top: 5px;
}

/* =====================================================
    HEADING
===================================================== */

h1 {
    color: #0789A8 !important;
    font-weight: 900 !important;
    letter-spacing: -0.8px;
}

h2 {
    color: #087F9B !important;
    font-weight: 800 !important;
}

h3 {
    color: #087F9B !important;
    font-weight: 750 !important;
}

[data-testid="stMarkdownContainer"] h1,
[data-testid="stMarkdownContainer"] h2,
[data-testid="stMarkdownContainer"] h3 {
    color: #087F9B !important;
}

p {
    color: #52717D;
}

/* =====================================================
    METRIC CARDS
===================================================== */

[data-testid="stMetric"] {
    background: linear-gradient(
        145deg,
        #FFFFFF 0%,
        #F0FCFE 100%
    ) !important;
    border: 1px solid #A4E7EF;
    border-bottom: 4px solid #12B8D0;
    border-radius: 16px;
    padding: 20px 22px;
    box-shadow: 0 5px 16px rgba(0,160,190,0.08);
    transition: all 0.2s ease;
}

[data-testid="stMetric"]:hover {
    transform: translateY(-3px);
    box-shadow: 0 8px 20px rgba(0,160,190,0.14);
}

[data-testid="stMetricLabel"] {
    color: #52717D !important;
    font-weight: 700 !important;
}

[data-testid="stMetricValue"] {
    color: #0789A8 !important;
    font-weight: 900 !important;
}

/* =====================================================
    DATAFRAME
===================================================== */

[data-testid="stDataFrame"] {
    background: #FFFFFF !important;
    border: 1px solid #A4E7EF !important;
    border-radius: 13px;
    overflow: hidden;
    box-shadow: 0 3px 12px rgba(0,150,180,0.06);
}

/* =====================================================
    TABS
===================================================== */

.stTabs [data-baseweb="tab-list"] {
    background: #E5F9FC !important;
    border: 1px solid #A4E7EF;
    border-radius: 12px;
    padding: 6px;
    gap: 6px;
}

.stTabs [data-baseweb="tab"] {
    background: transparent;
    border-radius: 9px;
    color: #087F9B !important;
    font-weight: 700;
}

.stTabs [aria-selected="true"] {
    background: #FFFFFF !important;
    color: #079CB9 !important;
    box-shadow: 0 2px 7px rgba(0,120,150,0.12);
}

/* =====================================================
    BUTTON
===================================================== */

.stButton button,
.stDownloadButton button {
    background: linear-gradient(
        100deg,
        #08B4CD,
        #04A1C0
    ) !important;
    color: #FFFFFF !important;
    border: 1px solid #079DB9 !important;
    border-radius: 10px;
    padding: 10px 19px;
    font-weight: 800;
    transition: all 0.2s ease;
    box-shadow: 0 3px 10px rgba(0,150,180,0.16);
}

.stButton button:hover,
.stDownloadButton button:hover {
    background: linear-gradient(
        100deg,
        #078CA9,
        #067F9D
    ) !important;
    border-color: #067F9D !important;
    color: #FFFFFF !important;
    box-shadow: 0 5px 15px rgba(0,120,150,0.25);
}

/* =====================================================
    INPUT
===================================================== */

.stTextInput input,
.stNumberInput input,
.stSelectbox div[data-baseweb="select"] {
    background: #FFFFFF !important;
    border: 1px solid #8DDFEA !important;
    border-radius: 9px;
    color: #31596A !important;
}

/* =====================================================
    ALERT
===================================================== */

[data-testid="stAlert"] {
    border-radius: 12px;
    border: 1px solid #91DFE9;
}

/* =====================================================
    DIVIDER
===================================================== */

hr {
    border-color: #D0EDF1 !important;
}

/* =====================================================
    CHART
===================================================== */

[data-testid="stVegaLiteChart"],
[data-testid="stArrowVegaLiteChart"],
[data-testid="stVegaLiteChartContainer"] {
    background: #FFFFFF !important;
    border: 1px solid #A4E7EF !important;
    border-radius: 14px;
    padding: 12px;
    box-shadow: 0 4px 13px rgba(0,150,180,0.06);
}

/* =====================================================
    CAPTION
===================================================== */

.stCaption {
    color: #64818D !important;
}

/* =====================================================
    DOWNLOAD
===================================================== */

.stDownloadButton {
    margin-top: 10px;
}

/* =====================================================
    SCROLLBAR
===================================================== */

::-webkit-scrollbar {
    width: 8px;
}

::-webkit-scrollbar-thumb {
    background: #20C2D8;
    border-radius: 10px;
}

::-webkit-scrollbar-track {
    background: #EAFBFD;
}

/* =====================================================
    CUSTOM COMPONENTS
===================================================== */

.winner-card {
    background: linear-gradient(
        110deg,
        #08B8D0 0%,
        #13C8D9 55%,
        #66E0E8 100%
    );
    border: 1px solid #08B3CA;
    border-radius: 16px;
    padding: 25px 28px;
    margin-bottom: 20px;
    box-shadow: 0 6px 18px rgba(0,160,190,0.15);
}

.winner-label {
    color: #E9FDFF !important;
    font-size: 13px;
    font-weight: 900;
    letter-spacing: 1.5px;
}

.winner-name {
    color: #FFFFFF !important;
    font-size: 25px;
    font-weight: 900;
    margin-top: 9px;
}

.winner-score {
    color: #E8FCFF !important;
    font-size: 14px;
    margin-top: 7px;
}

.winner-score b {
    color: #FFFFFF !important;
    font-size: 17px;
}

.info-card {
    background: linear-gradient(
        120deg,
        #FFFFFF,
        #EAFBFD
    );
    border: 1px solid #A4E7EF;
    border-left: 5px solid #08B5CF;
    border-radius: 13px;
    padding: 22px;
    line-height: 1.8;
    color: #416575 !important;
}

.formula-card {
    background: linear-gradient(
        140deg,
        #FFFFFF,
        #F0FCFE
    );
    border: 1px solid #A4E7EF;
    border-radius: 13px;
    padding: 22px;
    min-height: 150px;
    box-shadow: 0 3px 12px rgba(0,150,180,0.05);
}

.formula-title {
    color: #0789A8 !important;
    font-size: 18px;
    font-weight: 900;
}

.formula-description {
    color: #52717D !important;
    margin-top: 10px;
    line-height: 1.7;
}

.stApp,
[data-testid="stMain"],
[data-testid="stMainBlockContainer"],
[data-testid="stVerticalBlock"] {
    color-scheme: light;
}

@media (max-width: 768px) {
    [data-testid="stMainBlockContainer"] {
        padding-left: 1rem;
        padding-right: 1rem;
    }
    .winner-name {
        font-size: 20px;
    }
    .formula-card {
        min-height: auto;
    }
}

</style>
""", unsafe_allow_html=True)


# =====================================================
# DATA DINAMIS (disimpan selama sesi aplikasi berjalan)
# =====================================================
def normalisasi_bobot(df):
    df = df.copy()
    if df.empty:
        return df
    bobot = pd.to_numeric(df["Bobot"], errors="coerce").fillna(0).clip(lower=0)
    total = float(bobot.sum())
    df["Bobot"] = bobot / total if total > 0 else 1.0 / len(df)
    return df

if "alternatif_data" not in st.session_state:
    st.session_state.alternatif_data = df_alternatif.copy()
if "kriteria_data" not in st.session_state:
    st.session_state.kriteria_data = df_kriteria.copy()
if "editor_version" not in st.session_state:
    st.session_state.editor_version = 0

df_alt = st.session_state.alternatif_data.copy()
df_krit = st.session_state.kriteria_data.copy()
kode_kriteria = df_krit["Kode"].tolist()

def validasi_data(alternatif, kriteria):
    if kriteria.empty:
        return "Tambahkan minimal satu kriteria terlebih dahulu."
    if alternatif.empty:
        return "Tambahkan minimal satu alternatif lokasi terlebih dahulu."
    if alternatif["Alternatif"].astype(str).str.strip().eq("").any():
        return "Nama alternatif tidak boleh kosong."
    if alternatif["Alternatif"].duplicated().any():
        return "Nama alternatif tidak boleh duplikat."
    if kriteria["Kriteria"].astype(str).str.strip().eq("").any():
        return "Nama kriteria tidak boleh kosong."
    bobot = pd.to_numeric(kriteria["Bobot"], errors="coerce")
    if bobot.isna().any() or (bobot < 0).any():
        return "Bobot harus berupa angka nonnegatif."
    if abs(float(bobot.sum()) - 1.0) > 1e-6:
        return "Total bobot harus 1.00. Gunakan tombol Normalisasi Bobot."
    if not set(kriteria["Jenis"]).issubset({"Benefit", "Cost"}):
        return "Jenis kriteria hanya boleh Benefit atau Cost."
    for kode in kriteria["Kode"]:
        nilai = pd.to_numeric(alternatif[kode], errors="coerce")
        if nilai.isna().any():
            return f"Nilai pada {kode} harus berupa angka."
        if (nilai < 0).any():
            return f"Nilai pada {kode} tidak boleh negatif."
    return None

# Pastikan kolom numerik dan kolom mengikuti kriteria yang masih aktif.
for kode in kode_kriteria:
    if kode not in df_alt.columns:
        df_alt[kode] = 0.0
df_alt = df_alt[["Alternatif"] + kode_kriteria]
error_data = validasi_data(df_alt, df_krit)
normalisasi = normalisasi_terbobot = penyebut = ranking = None
if error_data is None:
    try:
        normalisasi, normalisasi_terbobot, penyebut, ranking = hitung_moora(df_alt, df_krit)
    except Exception as exc:
        error_data = str(exc)

total_alternatif = len(df_alt)
total_kriteria = len(df_krit)
total_bobot = float(pd.to_numeric(df_krit["Bobot"], errors="coerce").fillna(0).sum()) if not df_krit.empty else 0.0

# SIDEBAR
with st.sidebar:
    st.markdown("### 🌴 PALM OIL DSS")
    st.caption("DECISION SUPPORT SYSTEM")
    st.markdown("---")
    menu = st.radio("Navigasi Utama", ["Dashboard", "Data Alternatif", "Data Kriteria", "Normalisasi MOORA", "Hasil Perangkingan"], label_visibility="collapsed")
    st.markdown("---")
    st.markdown("**METODE ANALISIS**")
    st.markdown("""<div class="sidebar-method">Multi-Objective Optimization on the basis of Ratio Analysis<small>Metode pengambilan keputusan (MOORA)</small></div>""", unsafe_allow_html=True)
    st.markdown("---")
    st.caption("© 2026 Palm Oil Decision Support")
    st.caption("WHITE & CYAN EDITION")

if menu == "Dashboard":
    st.title("Overview Dashboard")
    st.caption("Pusat informasi dan hasil analisis pemilihan lokasi pendirian pabrik kelapa sawit menggunakan metode MOORA.")
    c1, c2, c3 = st.columns(3)
    c1.metric("Total Alternatif Lokasi", total_alternatif)
    c2.metric("Total Kriteria", total_kriteria)
    c3.metric("Total Bobot", f"{total_bobot:.2f}")
    st.divider()
    if error_data:
        st.warning(error_data)
        st.info("Perbaiki data melalui menu Data Alternatif dan Data Kriteria.")
    elif ranking is not None and not ranking.empty:
        terbaik = ranking.iloc[0]
        st.markdown(f'''<div class="winner-card"><div class="winner-label">🏆 LOKASI DENGAN NILAI OPTIMASI TERTINGGI</div><div class="winner-name">{terbaik["Alternatif"]}</div><div class="winner-score">Nilai Optimasi: <b>{terbaik["Nilai Optimasi"]:.4f}</b> | Peringkat 1</div></div>''', unsafe_allow_html=True)
        ca, cb = st.columns([1.3, 1])
        with ca:
            st.subheader("Visualisasi Hasil")
            st.bar_chart(ranking.set_index("Alternatif")[["Nilai Optimasi"]], height=320, color="#08B8D0")
        with cb:
            st.subheader("Peringkat Lokasi")
            st.dataframe(ranking[["Peringkat", "Alternatif", "Nilai Optimasi"]].style.format({"Nilai Optimasi": "{:.4f}"}), use_container_width=True, hide_index=True, height=320)
    st.divider()
    st.subheader("Tentang Sistem")
    st.markdown("""<div class="info-card">Aplikasi <b style="color:#0789A8;">Palm Oil Decision Support</b> merupakan sistem pendukung keputusan pemilihan lokasi pendirian pabrik kelapa sawit menggunakan metode <b>MOORA</b>. Alternatif, kriteria, bobot, dan jenis kriteria dapat dikelola langsung melalui aplikasi.</div>""", unsafe_allow_html=True)
    st.warning("Data awal merupakan data simulasi. Ganti dengan data survei yang dapat dipertanggungjawabkan sebelum digunakan untuk keputusan nyata.")

elif menu == "Data Alternatif":
    st.title("Data Alternatif Lokasi")
    st.caption("Edit nilai langsung pada tabel. Gunakan tombol + pada tabel untuk menambah baris dan ikon hapus untuk menghapus baris.")
    st.metric("Jumlah Alternatif", total_alternatif)
    edited = st.data_editor(df_alt, key=f"alt_editor_{st.session_state.editor_version}", num_rows="dynamic", use_container_width=True, hide_index=True,
        column_config={"Alternatif": st.column_config.TextColumn("Nama Alternatif", required=True), **{k: st.column_config.NumberColumn(k, min_value=0, step=1, format="%.2f") for k in kode_kriteria}})
    if not edited.equals(df_alt):
        edited["Alternatif"] = edited["Alternatif"].fillna("").astype(str).str.strip()
        edited = edited[edited["Alternatif"].ne("")].copy()
        for k in kode_kriteria:
            edited[k] = pd.to_numeric(edited[k], errors="coerce").fillna(0)
        st.session_state.alternatif_data = edited.reset_index(drop=True)
        st.rerun()
    st.caption("Perubahan disimpan selama sesi aplikasi berjalan. Unduh data bila ingin menyimpan salinan di komputer.")

    # Fitur hapus alternatif melalui antarmuka aplikasi.
    st.divider()
    st.subheader("Hapus Alternatif Lokasi")
    if not st.session_state.alternatif_data.empty:
        daftar_alternatif = st.session_state.alternatif_data["Alternatif"].astype(str).tolist()
        pilihan_hapus = st.selectbox(
            "Pilih nama alternatif yang akan dihapus",
            options=daftar_alternatif,
            key=f"hapus_alternatif_{st.session_state.editor_version}",
        )
        if st.button("🗑️ Hapus Alternatif Terpilih", key="btn_hapus_alternatif"):
            sisa_alternatif = st.session_state.alternatif_data[
                st.session_state.alternatif_data["Alternatif"].astype(str) != pilihan_hapus
            ].copy().reset_index(drop=True)
            st.session_state.alternatif_data = sisa_alternatif
            st.session_state.editor_version += 1
            st.rerun()
    else:
        st.info("Tidak ada alternatif lokasi yang tersedia untuk dihapus.")

    st.download_button("⬇ Unduh Data Alternatif CSV", data=df_alt.to_csv(index=False).encode("utf-8-sig"), file_name="data_alternatif.csv", mime="text/csv")
    st.info("Data awal adalah simulasi, bukan hasil survei lapangan.")

elif menu == "Data Kriteria":
    st.title("Pengaturan Kriteria dan Bobot")
    st.caption("Edit nama, bobot, dan jenis kriteria. Tambah atau hapus kriteria melalui bagian di bawah tabel.")
    st.metric("Total Bobot Saat Ini", f"{total_bobot:.2f}")
    edited_k = st.data_editor(df_krit, key=f"criteria_editor_{st.session_state.editor_version}", use_container_width=True, hide_index=True, disabled=["Kode"],
        column_config={"Kode": st.column_config.TextColumn("Kode", help="Dibuat otomatis"), "Kriteria": st.column_config.TextColumn("Nama Kriteria", required=True), "Bobot": st.column_config.NumberColumn("Bobot", min_value=0.0, max_value=1.0, step=0.01, format="%.2f"), "Jenis": st.column_config.SelectboxColumn("Jenis", options=["Benefit", "Cost"], required=True)})
    if not edited_k.equals(df_krit):
        edited_k["Kriteria"] = edited_k["Kriteria"].fillna("").astype(str).str.strip()
        edited_k["Bobot"] = pd.to_numeric(edited_k["Bobot"], errors="coerce").fillna(0)
        st.session_state.kriteria_data = edited_k.reset_index(drop=True)
        st.rerun()

    bobot_now = float(pd.to_numeric(st.session_state.kriteria_data["Bobot"], errors="coerce").fillna(0).sum()) if not st.session_state.kriteria_data.empty else 0
    ca, cb = st.columns([1, 2])
    with ca:
        if st.button("⚖️ Normalisasi Bobot", use_container_width=True):
            st.session_state.kriteria_data = normalisasi_bobot(st.session_state.kriteria_data)
            st.rerun()
    with cb:
        if abs(bobot_now - 1) < 1e-6:
            st.success("Total bobot valid: 1.00")
        else:
            st.warning(f"Total bobot {bobot_now:.2f}; klik Normalisasi Bobot agar total menjadi 1.00.")

    st.divider()
    st.subheader("Tambah Kriteria Baru")
    with st.form("add_criteria_form", clear_on_submit=True):
        nama_baru = st.text_input("Nama Kriteria", placeholder="Contoh: Jarak ke Permukiman")
        ca, cb = st.columns(2)
        with ca:
            bobot_baru = st.number_input("Bobot Awal", min_value=0.01, max_value=1.0, value=0.10, step=0.01)
        with cb:
            jenis_baru = st.selectbox("Jenis", ["Benefit", "Cost"])
        submit_add = st.form_submit_button("＋ Tambahkan Kriteria")
    if submit_add:
        current = st.session_state.kriteria_data.copy()
        if not nama_baru.strip():
            st.error("Nama kriteria wajib diisi.")
        elif not current.empty and current["Kriteria"].str.casefold().eq(nama_baru.strip().casefold()).any():
            st.error("Nama kriteria sudah ada.")
        else:
            kode_baru = f"C{max([int(x[1:]) for x in current['Kode']] + [0]) + 1}"
            if not current.empty:
                old_sum = float(current["Bobot"].sum())
                current["Bobot"] = (current["Bobot"] / old_sum * (1-bobot_baru)) if old_sum > 0 else (1-bobot_baru)/len(current)
            row = pd.DataFrame([{"Kode": kode_baru, "Kriteria": nama_baru.strip(), "Bobot": bobot_baru, "Jenis": jenis_baru}])
            st.session_state.kriteria_data = pd.concat([current, row], ignore_index=True)
            st.session_state.kriteria_data = normalisasi_bobot(st.session_state.kriteria_data)
            st.session_state.alternatif_data[kode_baru] = 0.0
            st.session_state.editor_version += 1
            st.rerun()

    st.subheader("Hapus Kriteria")
    if not st.session_state.kriteria_data.empty:
        labels = {r["Kode"]: f"{r['Kode']} - {r['Kriteria']}" for _, r in st.session_state.kriteria_data.iterrows()}
        hapus_kode = st.selectbox("Pilih kriteria", list(labels), format_func=lambda x: labels[x])
        if st.button("🗑️ Hapus Kriteria Terpilih"):
            sisa = st.session_state.kriteria_data[st.session_state.kriteria_data["Kode"] != hapus_kode].copy().reset_index(drop=True)
            st.session_state.alternatif_data = st.session_state.alternatif_data.drop(columns=[hapus_kode], errors="ignore")
            # Kode disusun ulang agar berurutan dan konsisten dengan kolom matriks.
            old_codes = sisa["Kode"].tolist()
            mapping = {old: f"C{i+1}" for i, old in enumerate(old_codes)}
            sisa["Kode"] = sisa["Kode"].map(mapping)
            st.session_state.alternatif_data = st.session_state.alternatif_data.rename(columns=mapping)
            st.session_state.kriteria_data = normalisasi_bobot(sisa) if not sisa.empty else sisa
            st.session_state.editor_version += 1
            st.rerun()
    st.warning("Benefit: skor lebih tinggi berarti lebih baik. Cost: skor lebih tinggi berarti biaya/kerugian lebih besar.")

elif menu == "Normalisasi MOORA":
    st.title("Proses Normalisasi MOORA")
    st.caption("Matriks dan hasil normalisasi mengikuti data alternatif serta kriteria terbaru.")
    if error_data:
        st.error(error_data)
    else:
        t1, t2, t3, t4 = st.tabs(["Matriks Keputusan", "Penyebut", "Normalisasi", "Normalisasi Terbobot"])
        with t1:
            st.dataframe(df_alt.set_index("Alternatif")[kode_kriteria], use_container_width=True)
        with t2:
            st.dataframe(penyebut, use_container_width=True, hide_index=True)
        with t3:
            st.dataframe(normalisasi.round(4), use_container_width=True)
            st.download_button("⬇ Download Normalisasi CSV", data=normalisasi.to_csv().encode("utf-8-sig"), file_name="normalisasi_moora.csv", mime="text/csv")
        with t4:
            st.dataframe(normalisasi_terbobot.round(4), use_container_width=True)
        st.subheader("Rumus Normalisasi")
        st.latex(r"x_{ij}^* = \frac{x_{ij}}{\sqrt{\sum_{i=1}^m x_{ij}^2}}")
        st.subheader("Rumus Nilai Optimasi Berbobot")
        st.latex(r"Y_i = \sum_{j \in Benefit} w_j x_{ij}^* - \sum_{j \in Cost} w_j x_{ij}^*")

elif menu == "Hasil Perangkingan":
    st.title("Hasil Perangkingan Lokasi")
    st.caption("Peringkat dihitung ulang otomatis dari data terbaru.")
    if error_data:
        st.error(error_data)
    elif ranking is not None and not ranking.empty:
        terbaik = ranking.iloc[0]
        ca, cb = st.columns(2)
        ca.metric("Lokasi Peringkat Pertama", terbaik["Alternatif"])
        cb.metric("Nilai Optimasi Tertinggi", f"{terbaik['Nilai Optimasi']:.4f}")
        st.dataframe(ranking.style.format({"Nilai Benefit": "{:.4f}", "Nilai Cost": "{:.4f}", "Nilai Optimasi": "{:.4f}"}), use_container_width=True, hide_index=True)
        st.bar_chart(ranking.set_index("Alternatif")["Nilai Optimasi"], height=350, color="#08B8D0")
        st.download_button("⬇ Unduh Hasil Perangkingan", data=ranking.to_csv(index=False).encode("utf-8-sig"), file_name="hasil_perangkingan_moora.csv", mime="text/csv")

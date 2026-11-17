@echo off
setlocal
cd /d "%~dp0"
echo ==========================================
echo   SPK PEMILIHAN LOKASI PABRIK KELAPA SAWIT
echo   MOORA - Setup dan Menjalankan Aplikasi
echo ==========================================
where python >nul 2>nul
if errorlevel 1 (
  echo Python belum ditemukan. Instal Python 3.10 atau lebih baru dan aktifkan Add Python to PATH.
  pause
  exit /b 1
)
if not exist ".venv\Scripts\python.exe" (
  echo Membuat virtual environment...
  python -m venv .venv
  if errorlevel 1 (
    echo Gagal membuat virtual environment.
    pause
    exit /b 1
  )
)
call ".venv\Scripts\activate.bat"
echo Memasang dependensi...
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
if errorlevel 1 (
  echo Gagal memasang dependensi. Periksa koneksi internet dan versi Python.
  pause
  exit /b 1
)
echo Membuka aplikasi pada browser...
python -m streamlit run app.py
pause

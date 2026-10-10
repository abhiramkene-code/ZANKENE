@echo off
TITLE ZANKENE V10 Production Engine Launcher
echo =================================================================
echo 👑 STARTING ZANKENE V10 ENTERPRISE ECOSYSTEM ENGINE 👑
echo =================================================================
echo.

:: 1. Activate Virtual Environment
call venv\Scripts\activate

:: 2. Start FastAPI REST Backend in Background
echo ⚡ Launching FastAPI REST Engine on http://127.0.0.1:8000 ...
start /B venv\Scripts\python.exe -m uvicorn zankene.api:app --host 127.0.0.1 --port 8000 --reload

:: Wait 3 seconds for backend initialization
timeout /t 3 /nobreak > nul

:: 3. Start Streamlit Mission Control Dashboard
echo 🚀 Launching Mission Control Dashboard on http://localhost:8501 ...
venv\Scripts\python.exe -m streamlit run zankene_dashboard.py

pause
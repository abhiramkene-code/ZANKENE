@echo off
TITLE ZANKENE Mobile Server Launcher
echo =================================================================
echo 📱 STARTING ZANKENE V10 MOBILE INTERFACE SERVER 📱
echo =================================================================
echo.

call venv\Scripts\activate

echo 🚀 Launching Mobile Web Controller on Port 8502...
venv\Scripts\python.exe -m streamlit run zankene/mobile_ui.py --server.port 8502 --server.address 0.0.0.0

pause
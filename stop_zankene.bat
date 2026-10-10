@echo off
TITLE ZANKENE Shutdown Controller
echo =================================================================
echo 🛑 STOPPING ALL ZANKENE ENGINE SERVICES 🛑
echo =================================================================
echo.

taskkill /FI "WINDOWTITLE eq ZANKENE V10 Production Engine Launcher*" /F
taskkill /IM uvicorn.exe /F
taskkill /IM streamlit.exe /F

echo.
echo ✅ All ZANKENE services stopped successfully.
pause
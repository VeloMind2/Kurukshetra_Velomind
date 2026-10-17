@echo off
echo ======================================================================
echo   Starting SkillTrace AI - Adaptive Learning & Assessment Portal
echo ======================================================================
echo.

echo Starting Python Backend Server on http://localhost:8000 ...
start "SkillTrace AI Backend" python server.py 8000

timeout /t 2 /nobreak >nul

echo Starting Vite Frontend on http://localhost:5173 ...
start "SkillTrace AI Frontend" cmd /k "npx vite --host 0.0.0.0 --port 5173"

timeout /t 2 /nobreak >nul

echo Opening browser at http://localhost:5173 ...
start http://localhost:5173

echo.
echo ======================================================================
echo   Portal is LIVE:
echo   - Web App UI:  http://localhost:5173/
echo   - Backend API: http://localhost:8000/api/health
echo ======================================================================

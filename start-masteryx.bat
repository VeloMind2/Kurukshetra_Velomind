@echo off
set "PATH=%USERPROFILE%\.nodejs\node-v20.18.0-win-x64;%PATH%"
echo Starting MASTERYX Adaptive Learning & Assessment Platform...
echo Open your browser at http://localhost:5173/
npm run dev -- --host 0.0.0.0 --port 5173
pause

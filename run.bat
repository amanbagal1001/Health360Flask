@echo off
title Health360 Flask Server
echo ==================================================
echo   Starting Health360 Healthcare Analytics Server
echo ==================================================
echo.
echo Opening website in your default browser...
start "" http://127.0.0.1:5000
echo.
echo Running Flask server (Press Ctrl+C to stop)...
python app.py
pause

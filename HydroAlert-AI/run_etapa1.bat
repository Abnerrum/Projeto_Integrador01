@echo off
chcp 65001 >nul
cd /d "%~dp0"
python -m iot.sensor_simulator --ciclos 10
pause

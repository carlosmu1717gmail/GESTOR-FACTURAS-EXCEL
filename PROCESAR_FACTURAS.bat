@echo off
chcp 65001 >nul
cls
echo ===================================================
echo   AUTO GESTOR FACTURAS
echo   Procesamiento automático de facturas
echo ===================================================
echo.
echo Procesando facturas de c:\FACTURAS...
echo.

python FICHEROS\procesar_todas.py

echo.
echo ===================================================
echo   Proceso completado
echo   Revisa el archivo facturas.xlsx
echo ===================================================
echo.
pause

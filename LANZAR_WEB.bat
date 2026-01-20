@echo off
chcp 65001 >nul
cls
echo ===================================================
echo   AUTO GESTOR FACTURAS - INTERFAZ WEB
echo   Lanzando aplicacion web en tu navegador...
echo ===================================================
echo.
echo Instalando dependencias necesarias...
python -m pip install -q streamlit pandas
echo.
echo Abriendo interfaz web...
echo.
echo ===================================================
echo   La aplicacion se abrira en tu navegador
echo   URL: http://localhost:8501
echo ===================================================
echo.
echo Para DETENER la aplicacion: Presiona CTRL+C
echo.

cd FICHEROS
streamlit run app.py

@echo off
chcp 65001 >nul
cls
echo ===================================================
echo   AUTO GESTOR FACTURAS - INTERFAZ WEB REMOTA
echo   Lanzando aplicacion accesible desde otros PCs
echo ===================================================
echo.
echo Instalando dependencias necesarias...
python -m pip install -q streamlit pandas
echo.
echo Detectando tu direccion IP local...
echo.

REM Obtener IP local
for /f "tokens=2 delims=:" %%a in ('ipconfig ^| findstr /c:"IPv4"') do (
    set IP=%%a
    goto :found
)
:found
set IP=%IP:~1%

echo ===================================================
echo   APLICACION INICIADA - ACCESO REMOTO HABILITADO
echo.
echo   En ESTE ordenador, abre:
echo   http://localhost:8501
echo.
echo   Desde OTROS ordenadores en la red, abre:
echo   http://%IP%:8501
echo ===================================================
echo.
echo IMPORTANTE: Asegurate de que el Firewall de Windows
echo             permita conexiones en el puerto 8501
echo.
echo Para DETENER la aplicacion: Presiona CTRL+C
echo.

cd FICHEROS
streamlit run app.py --server.address=0.0.0.0 --server.port=8501

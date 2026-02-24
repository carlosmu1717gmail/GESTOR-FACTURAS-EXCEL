@echo off
chcp 65001 >nul
cls
echo ===================================================
echo   INSTALADOR DE DEPENDENCIAS - GESTOR FACTURAS
echo ===================================================
echo.
echo Comprobando Python...
python --version
if errorlevel 1 (
    echo.
    echo [ERROR] Python no está instalado o no está en el PATH.
    echo Por favor, instala Python desde python.org y marca "Add Python to PATH".
    pause
    exit /b
)

echo.
echo Instalando librerias necesarias...
python -m pip install --upgrade pip
python -m pip install -r FICHEROS\requirements.txt

if errorlevel 1 (
    echo.
    echo [ERROR] Hubo un problema al instalar las dependencias.
    pause
    exit /b
)

echo.
echo ===================================================
echo   INSTALACION COMPLETADA CON EXITO
echo ===================================================
echo.
echo Ahora puedes ejecutar:
echo   - PROCESAR_FACTURAS.bat (Para consola)
echo   - LANZAR_WEB.bat        (Para web)
echo.
pause

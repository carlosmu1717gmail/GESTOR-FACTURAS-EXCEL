@echo off
chcp 65001 >nul
cls
echo ===================================================
echo   AUTO GESTOR FACTURAS - MODO WEB PARA PC
echo   Preparando entorno por primera vez...
echo ===================================================
echo.

REM Comprobar si Python está instalado
python --version >nul 2>&1
if %ERRORLEVEL% NEQ 0 (
    echo [ERROR] No se ha detectado Python en este ordenador.
    echo.
    echo Para usar la Version Web, necesitas instalar Python desde Microsoft Store
    echo o desde python.org (Marca la casilla 'Add Python to PATH').
    echo.
    echo SI NO QUIERES INSTALAR NADA: Usa el archivo "Arrastrar_JSON_Aqui.bat"
    echo que incluido en esta carpeta (solo procesa datos, no tiene interfaz visual).
    pause
    exit
)

echo Verificando librerias necesarias...
echo (Esto solo tarda la primera vez)
echo.

pip install -q streamlit pandas google-generativeai python-dotenv pillow openpyxl

echo.
echo ===================================================
echo   INICIANDO APLICACION...
echo   Se abrira en tu navegador automaticamente.
echo ===================================================
echo.
echo Para CERRAR la aplicacion: Cierra la ventana negra.
echo.

streamlit run app.py
pause

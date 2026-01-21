@echo off
chcp 65001 >nul
cls
echo ===================================================
echo   AUTO GESTOR FACTURAS - INSTALACION AUTOMATICA
echo ===================================================
echo.

REM Verificar Python
echo [1/5] Verificando Python...
python --version >nul 2>&1
if %ERRORLEVEL% NEQ 0 (
    echo.
    echo ERROR: Python no está instalado
    echo.
    echo Descarga Python 3.9+ desde: https://www.python.org/downloads/
    echo IMPORTANTE: Marca la opcion "Add Python to PATH" durante instalacion
    echo.
    pause
    exit /b 1
)
python --version
echo    ✓ Python instalado correctamente
echo.

REM Verificar pip
echo [2/5] Verificando pip...
python -m pip --version >nul 2>&1
if %ERRORLEVEL% NEQ 0 (
    echo    ERROR: pip no está instalado
    pause
    exit /b 1
)
echo    ✓ pip disponible
echo.

REM Instalar dependencias
echo [3/5] Instalando dependencias Python...
echo    Esto puede tardar un par de minutos...
echo.
python -m pip install --upgrade pip
python -m pip install -r FICHEROS\requirements.txt
if %ERRORLEVEL% NEQ 0 (
    echo.
    echo ERROR: No se pudieron instalar las dependencias
    pause
    exit /b 1
)
echo    ✓ Dependencias instaladas
echo.

REM Crear archivo .env
echo [4/5] Configurando API Key de Gemini...
if exist .env (
    echo    ✓ Archivo .env ya existe
) else (
    copy .env.example .env >nul
    echo    ✓ Archivo .env creado desde plantilla
    echo.
    echo    IMPORTANTE: Debes editar el archivo .env
    echo    y agregar tu GEMINI_API_KEY
    echo.
    echo    Obten tu API Key gratuita en: https://ai.google.dev
)
echo.

REM Crear carpeta de facturas
echo [5/5] Creando estructura de carpetas...
if not exist "C:\FACTURAS" (
    mkdir "C:\FACTURAS"
    echo    ✓ Carpeta C:\FACTURAS creada
) else (
    echo    ✓ Carpeta C:\FACTURAS ya existe
)
echo.

echo ===================================================
echo   INSTALACION COMPLETADA
echo ===================================================
echo.
echo SIGUIENTE PASO:
echo.
echo 1. Edita el archivo .env con tu editor de texto
echo 2. Pega tu GEMINI_API_KEY (consiguela en https://ai.google.dev)
echo 3. Guarda el archivo .env
echo.
echo LUEGO PUEDES USAR:
echo   - PROCESAR_FACTURAS.bat   (modo linea de comandos)
echo   - LANZAR_WEB.bat          (interfaz web local)
echo   - LANZAR_WEB_REMOTO.bat   (interfaz web acceso red)
echo.
echo ===================================================
echo.
pause

@echo off
chcp 65001 >nul
cls
echo ===================================================
echo   ACTUALIZAR REPOSITORIO DESDE GITHUB
echo ===================================================
echo.

REM Verificar si Git está instalado
where git >nul 2>&1
if %ERRORLEVEL% NEQ 0 (
    echo ERROR: Git no está instalado
    echo.
    echo Este script requiere Git para actualizar desde GitHub
    echo Descarga Git desde: https://git-scm.com/download/win
    echo.
    pause
    exit /b 1
)

echo Este script descargará las ultimas actualizaciones desde GitHub
echo.
echo ADVERTENCIA: Se perderán cambios locales no guardados
echo.
set /p confirm="¿Continuar? (S/N): "
if /i not "%confirm%"=="S" (
    echo Operación cancelada
    pause
    exit /b 0
)

echo.
echo [1/3] Guardando cambios locales (stash)...
git stash
echo.

echo [2/3] Descargando actualizaciones desde GitHub...
git pull origin main
if %ERRORLEVEL% NEQ 0 (
    echo.
    echo ERROR: No se pudo actualizar desde GitHub
    echo Verifica tu conexión a Internet y que el repositorio exista
    pause
    exit /b 1
)
echo.

echo [3/3] Reinstalando dependencias actualizadas...
python -m pip install -r FICHEROS\requirements.txt --upgrade
echo.

echo ===================================================
echo   ACTUALIZACION COMPLETADA
echo ===================================================
echo.
echo Tu aplicación está ahora actualizada a la última versión
echo.
pause

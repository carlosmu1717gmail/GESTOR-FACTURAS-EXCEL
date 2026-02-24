@echo off
REM Script para facilitar el uso del Procesador de Facturas
REM Arrastra un archivo JSON sobre este icono para procesarlo

if "%~1"=="" (
    echo Por favor, arrastra un archivo JSON sobre este icono.
    pause
    exit /b
)

echo Procesando el archivo: %~1
echo Destino: %~dp0

"%~dp0ProcesadorFacturas.exe" "%~1" "%~dp0."

if %ERRORLEVEL% EQU 0 (
    echo.
    echo PROCESO COMPLETADO CON EXITO.
) else (
    echo.
    echo OCURRIO UN ERROR.
)

pause

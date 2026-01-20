@echo off
chcp 65001 >nul
cls
echo ==========================================
echo   SUBIENDO A GITHUB
echo ==========================================
echo.

REM Verificar si Git está instalado
where git >nul 2>&1
if %ERRORLEVEL% NEQ 0 (
    echo ERROR: Git no está instalado
    echo.
    echo Descarga Git desde: https://git-scm.com/download/win
    echo O instala con: winget install Git.Git
    echo.
    pause
    exit /b 1
)

echo 1. Inicializando Git...
git init

echo.
echo 2. Configurando usuario Git...
set /p userName="   Tu nombre: "
set /p userEmail="   Tu email: "

git config user.name "%userName%"
git config user.email "%userEmail%"

echo.
echo 3. Añadiendo archivos...
git add .

echo.
echo 4. Creando commit inicial...
git commit -m "Initial commit: AutoGestor Facturas con IA (Gemini 3 Pro)"

echo.
echo 5. Configurando rama principal...
git branch -M main

echo.
echo 6. Vinculando con GitHub...
set /p githubUser="   Tu usuario de GitHub: "
set repoUrl=https://github.com/%githubUser%/ANTIGRAVITY-GESTOR-FACTURAS.git

git remote add origin %repoUrl%

echo.
echo 7. Subiendo a GitHub...
echo    (Ingresa tu usuario y Personal Access Token cuando se solicite)
echo.
git push -u origin main

echo.
echo ==========================================
echo   COMPLETADO
echo   Repositorio: %repoUrl%
echo ==========================================
echo.
pause

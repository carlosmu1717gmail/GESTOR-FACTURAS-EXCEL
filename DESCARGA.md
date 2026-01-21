# 📥 Descarga sin Git

Si **no tienes Git instalado** y quieres descargar la aplicación:

## Opción 1: Descarga ZIP desde GitHub

1. **Ve al repositorio en GitHub:**
   ```
   https://github.com/carlosmu1717gmail/ANTIGRAVITY-GESTOR-FACTURAS
   ```

2. **Descarga el código:**
   - Clic en el botón verde **"Code"** 
   - Selecciona **"Download ZIP"**
   
3. **Descomprime:**
   - Haz clic derecho en el archivo descargado
   - Selecciona **"Extraer todo..."**
   - Elige una ubicación (ej: `C:\AutoGestorFacturas`)

4. **Abre la carpeta descomprimida** y continúa con el [QUICKSTART.md](QUICKSTART.md)

---

## Opción 2: Descarga Directa con PowerShell

Abre PowerShell y ejecuta:

```powershell
# Crear carpeta de destino
New-Item -ItemType Directory -Path "C:\AutoGestorFacturas" -Force

# Descargar ZIP
Invoke-WebRequest -Uri "https://github.com/carlosmu1717gmail/ANTIGRAVITY-GESTOR-FACTURAS/archive/refs/heads/main.zip" -OutFile "C:\AutoGestorFacturas\repo.zip"

# Descomprimir
Expand-Archive -Path "C:\AutoGestorFacturas\repo.zip" -DestinationPath "C:\AutoGestorFacturas" -Force

# Limpiar ZIP
Remove-Item "C:\AutoGestorFacturas\repo.zip"

# Abrir carpeta
cd "C:\AutoGestorFacturas\ANTIGRAVITY-GESTOR-FACTURAS-main"

Write-Host "✓ Descarga completada!"
Write-Host "Ahora ejecuta: INSTALAR.bat"
```

---

## ⏭️ Siguiente Paso

Una vez descargado, ejecuta:
```
INSTALAR.bat
```

Y sigue la [Guía de Instalación](QUICKSTART.md)
